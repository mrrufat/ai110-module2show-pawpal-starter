"""Logic layer for PawPal+. Backend classes for owners, pets, tasks, and scheduling."""

from dataclasses import dataclass, field
from datetime import date, timedelta
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    is_completed: bool = False
    pet: Optional["Pet"] = None
    next_due: Optional[date] = None

    def mark_completed(self):
        """Mark this task as completed."""
        self.is_completed = True

    def mark_incomplete(self):
        """Mark this task as not completed."""
        self.is_completed = False


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    special_needs: Optional[str] = None
    owner: Optional["Owner"] = None
    tasks: List[Task] = field(default_factory=list)

    def add_task(self, task: Task):
        """Assign a task to this pet."""
        task.pet = self
        self.tasks.append(task)

    def remove_task(self, task: Task):
        """Remove a task from this pet."""
        self.tasks.remove(task)

    def get_tasks(self) -> List[Task]:
        """Return this pet's list of tasks."""
        return self.tasks


@dataclass
class Owner:
    name: str
    contact_info: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self, pet: Pet):
        """Add a pet to this owner's list of pets."""
        pet.owner = self
        self.pets.append(pet)

    def remove_pet(self, pet: Pet):
        """Remove a pet from this owner's list of pets."""
        self.pets.remove(pet)

    def get_all_tasks(self) -> List[Task]:
        """Return the combined tasks of all this owner's pets."""
        all_tasks = []
        for pet in self.pets:
            all_tasks.extend(pet.get_tasks())
        return all_tasks


class Scheduler:
    """The 'brain' that retrieves, organizes, and manages tasks across pets."""

    def __init__(self, owner: Owner):
        self.owner = owner

    def get_all_tasks(self) -> List[Task]:
        """Return every task across all of the owner's pets."""
        return self.owner.get_all_tasks()

    def get_pending_tasks(self) -> List[Task]:
        """Return only the tasks that are not yet completed."""
        return [task for task in self.get_all_tasks() if not task.is_completed]

    def get_tasks_by_pet(self, pet: Pet) -> List[Task]:
        """Return the tasks belonging to a specific pet."""
        return pet.get_tasks()

    def _parse_time(self, time_value: str) -> tuple[int, int]:
        """Convert an HH:MM string into a sortable tuple of hours and minutes."""
        hours, minutes = time_value.split(":")
        return int(hours), int(minutes)

    def sort_by_time(self) -> List[Task]:
        """Return all tasks ordered from earliest to latest using their HH:MM time values."""
        return sorted(self.get_all_tasks(), key=lambda task: self._parse_time(task.time))

    def organize_by_time(self) -> List[Task]:
        """Return all tasks sorted chronologically by time for display in the schedule."""
        return self.sort_by_time()

    def filter_tasks(self, pet_name: Optional[str] = None, is_completed: Optional[bool] = None) -> List[Task]:
        """Filter tasks by pet name and/or completion state, returning a focused task list."""
        tasks = self.get_all_tasks()

        if pet_name is not None:
            tasks = [task for task in tasks if task.pet and task.pet.name.lower() == pet_name.lower()]

        if is_completed is not None:
            tasks = [task for task in tasks if task.is_completed is is_completed]

        return tasks

    def detect_conflicts(self) -> List[str]:
        """Return lightweight warnings whenever two pending tasks share the same time slot."""
        warnings = []
        tasks = [task for task in self.get_all_tasks() if not task.is_completed]

        for index, task in enumerate(tasks):
            for other_task in tasks[index + 1 :]:
                if task.time == other_task.time:
                    pet_name = task.pet.name if task.pet else "Unknown"
                    other_pet_name = other_task.pet.name if other_task.pet else "Unknown"
                    warnings.append(
                        f"Conflict: {task.description} ({pet_name}) and {other_task.description} ({other_pet_name}) both occur at {task.time}."
                    )

        return warnings

    def mark_task_complete(self, task: Task):
        """Mark a task complete and create the next recurring instance for daily or weekly tasks."""
        task.mark_completed()

        if task.frequency.lower() == "daily":
            next_due = date.today() + timedelta(days=1)
        elif task.frequency.lower() == "weekly":
            next_due = date.today() + timedelta(days=7)
        else:
            return None

        next_task = Task(
            description=task.description,
            time=task.time,
            frequency=task.frequency,
            pet=task.pet,
            next_due=next_due,
        )
        if task.pet is not None:
            task.pet.add_task(next_task)
        return next_task
