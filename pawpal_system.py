"""Logic layer for PawPal+. Backend classes for owners, pets, tasks, and schedules."""

from dataclasses import dataclass, field
from typing import List, Optional


@dataclass
class Pet:
    name: str
    breed: str
    age: int
    special_needs: Optional[str] = None

    def get_assigned_tasks(self):
        pass

    def get_daily_schedule(self):
        pass


@dataclass
class Task:
    name: str
    duration: int
    priority: str
    time_constraints: Optional[str] = None

    def create(self):
        pass

    def edit(self):
        pass

    def delete(self):
        pass


@dataclass
class Owner:
    name: str
    contact_info: str
    preferred_start_time: str
    preferred_end_time: str
    pets: List[Pet] = field(default_factory=list)

    def add_pet(self):
        pass

    def manage_tasks(self):
        pass

    def generate_daily_plan(self):
        pass


class Schedule:
    def __init__(self, date: str):
        self.date = date
        self.ordered_tasks: List[Task] = []
        self.total_duration: int = 0
        self.reasoning: str = ""

    def generate_from_tasks(self):
        pass

    def display_plan(self):
        pass

    def reorder_by_priority(self):
        pass
