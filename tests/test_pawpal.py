from datetime import date, timedelta

from pawpal_system import Owner, Pet, Scheduler, Task


def test_task_completion():
    task = Task(description="Morning walk", time="08:00", frequency="daily")
    assert task.is_completed is False

    task.mark_completed()

    assert task.is_completed is True


def test_task_addition_increases_pet_task_count():
    pet = Pet(name="Mochi", breed="Shiba Inu", age=3)
    assert len(pet.get_tasks()) == 0

    pet.add_task(Task(description="Feeding", time="08:30", frequency="daily"))

    assert len(pet.get_tasks()) == 1


def test_scheduler_sorts_tasks_by_time():
    owner = Owner(name="Jordan", contact_info="jordan@example.com")
    pet = Pet(name="Mochi", breed="Shiba Inu", age=3)
    owner.add_pet(pet)
    pet.add_task(Task(description="Brush", time="09:00", frequency="daily"))
    pet.add_task(Task(description="Feed", time="08:00", frequency="daily"))
    pet.add_task(Task(description="Walk", time="08:30", frequency="daily"))

    scheduler = Scheduler(owner)
    ordered = scheduler.sort_by_time()

    assert [task.description for task in ordered] == ["Feed", "Walk", "Brush"]


def test_scheduler_handles_pet_with_no_tasks():
    owner = Owner(name="Jordan", contact_info="jordan@example.com")
    pet = Pet(name="Mochi", breed="Shiba Inu", age=3)
    owner.add_pet(pet)

    scheduler = Scheduler(owner)

    assert scheduler.get_pending_tasks() == []
    assert scheduler.sort_by_time() == []
    assert scheduler.detect_conflicts() == []


def test_scheduler_filters_tasks_by_pet_and_status():
    owner = Owner(name="Jordan", contact_info="jordan@example.com")
    mochi = Pet(name="Mochi", breed="Shiba Inu", age=3)
    biscuit = Pet(name="Biscuit", breed="Golden Retriever", age=5)
    owner.add_pet(mochi)
    owner.add_pet(biscuit)

    mochi.add_task(Task(description="Feed", time="08:00", frequency="daily"))
    mochi.add_task(Task(description="Walk", time="09:00", frequency="daily"))
    biscuit.add_task(Task(description="Groom", time="10:00", frequency="weekly"))

    scheduler = Scheduler(owner)
    pending_mochi_tasks = scheduler.filter_tasks(pet_name="Mochi", is_completed=False)

    assert [task.description for task in pending_mochi_tasks] == ["Feed", "Walk"]


def test_mark_task_complete_creates_next_occurrence_for_recurring_task():
    owner = Owner(name="Jordan", contact_info="jordan@example.com")
    pet = Pet(name="Mochi", breed="Shiba Inu", age=3)
    owner.add_pet(pet)

    task = Task(description="Walk", time="08:00", frequency="daily")
    pet.add_task(task)

    scheduler = Scheduler(owner)
    scheduler.mark_task_complete(task)

    assert task.is_completed is True
    assert len(pet.get_tasks()) == 2
    assert pet.get_tasks()[-1].description == "Walk"
    assert pet.get_tasks()[-1].is_completed is False
    assert pet.get_tasks()[-1].next_due == date.today() + timedelta(days=1)


def test_scheduler_detects_conflicts_at_same_time():
    owner = Owner(name="Jordan", contact_info="jordan@example.com")
    mochi = Pet(name="Mochi", breed="Shiba Inu", age=3)
    biscuit = Pet(name="Biscuit", breed="Golden Retriever", age=5)
    owner.add_pet(mochi)
    owner.add_pet(biscuit)

    mochi.add_task(Task(description="Feed", time="08:00", frequency="daily"))
    biscuit.add_task(Task(description="Walk", time="08:00", frequency="daily"))

    scheduler = Scheduler(owner)
    warnings = scheduler.detect_conflicts()

    assert len(warnings) == 1
    assert "08:00" in warnings[0]
