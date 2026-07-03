"""Temporary testing ground to verify pawpal_system logic in the terminal."""

from pawpal_system import Owner, Pet, Scheduler, Task

owner = Owner(name="Jordan", contact_info="jordan@example.com")

mochi = Pet(name="Mochi", breed="Shiba Inu", age=3)
biscuit = Pet(name="Biscuit", breed="Golden Retriever", age=5)

owner.add_pet(mochi)
owner.add_pet(biscuit)

# Add tasks out of order to show sorting and filtering in action.
mochi.add_task(Task(description="Morning walk", time="08:00", frequency="daily"))
mochi.add_task(Task(description="Feeding", time="08:30", frequency="daily"))
biscuit.add_task(Task(description="Vet checkup", time="14:00", frequency="monthly"))
biscuit.add_task(Task(description="Grooming", time="08:00", frequency="weekly"))

scheduler = Scheduler(owner)

print("Today's Schedule:")
for task in scheduler.sort_by_time():
    print(f"  {task.time} — {task.description} ({task.pet.name}) [{task.frequency}]")

print("\nPending tasks for Mochi:")
for task in scheduler.filter_tasks(pet_name="Mochi", is_completed=False):
    print(f"  - {task.description} at {task.time}")

print("\nConflicts:")
for warning in scheduler.detect_conflicts():
    print(f"  - {warning}")

print("\nCompleting the morning walk creates the next occurrence:")
daily_task = mochi.get_tasks()[0]
scheduler.mark_task_complete(daily_task)
print(f"  - Completed: {daily_task.description}")
print(f"  - Next task: {mochi.get_tasks()[-1].description} due {mochi.get_tasks()[-1].next_due}")
