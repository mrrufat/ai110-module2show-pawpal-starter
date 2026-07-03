"""Logic layer for PawPal+. Backend classes for owners, pets, tasks, and scheduling."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Task:
    description: str
    time: str
    frequency: str
    is_completed: bool = False
    pet: Optional["Pet"] = None

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

    def organize_by_time(self) -> List[Task]:
        """Return all tasks sorted chronologically by time."""
        return sorted(self.get_all_tasks(), key=lambda task: task.time)

    def mark_task_complete(self, task: Task):
        """Mark the given task as completed."""
        task.mark_completed()
