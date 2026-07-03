from pawpal_system import Pet, Task


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
