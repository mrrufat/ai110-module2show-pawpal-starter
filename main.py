"""Temporary testing ground to verify pawpal_system logic in the terminal."""

from pawpal_system import Owner, Pet, Task, Scheduler

owner = Owner(name="Jordan", contact_info="jordan@example.com")

mochi = Pet(name="Mochi", breed="Shiba Inu", age=3)
biscuit = Pet(name="Biscuit", breed="Golden Retriever", age=5)

owner.add_pet(mochi)
owner.add_pet(biscuit)

mochi.add_task(Task(description="Morning walk", time="08:00", frequency="daily"))
mochi.add_task(Task(description="Feeding", time="08:30", frequency="daily"))
biscuit.add_task(Task(description="Vet checkup", time="14:00", frequency="monthly"))

scheduler = Scheduler(owner)

print("Today's Schedule:")
for task in scheduler.organize_by_time():
    print(f"  {task.time} — {task.description} ({task.pet.name}) [{task.frequency}]")
