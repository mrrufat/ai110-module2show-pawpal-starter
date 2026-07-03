# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Paste a sample of your app's CLI or Streamlit output here so a reader can see what a generated plan looks like:

```
# e.g.:
# Daily plan for Biscuit (Golden Retriever):
#   08:00 — Morning walk (30 min) [priority: high]
#   09:00 — Feeding (10 min) [priority: high]
#   ...
```

Actual output from running `python3 main.py`:

```
Today's Schedule:
  08:00 — Morning walk (Mochi) [daily]
  08:30 — Feeding (Mochi) [daily]
  14:00 — Vet checkup (Biscuit) [monthly]
```

## 🧪 Testing PawPal+

Run the full automated test suite with:

```bash
python -m pytest
```

These tests cover the core PawPal+ scheduler behaviors, including sorting tasks by time, filtering tasks by pet/completion status, creating the next recurring instance for daily and weekly tasks, detecting time-slot conflicts, and handling edge cases such as a pet with no tasks.

Sample test output from a successful run:

```text
============================= test session starts ==============================
platform darwin -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: /Users/rufatmusayev/Desktop/CodePath/ai110-module1show-gameglitchinvestigator-starter/ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 7 items

tests/test_pawpal.py .......                                             [100%]

============================== 7 passed in 0.02s ===============================
```

Confidence Level: ★★★★★ (7/7 tests passing)

## 📐 Smarter Scheduling

The scheduler now supports a few lightweight but practical scheduling features that make the CLI demo more useful.

| Feature | Method | Notes |
|---------|--------|-------|
| Sorting by time | `Scheduler.sort_by_time()` | Orders tasks from earliest to latest using their `HH:MM` time values. |
| Filtering by pet or completion status | `Scheduler.filter_tasks()` | Lets the app focus on a specific pet or show only pending/completed tasks. |
| Conflict detection | `Scheduler.detect_conflicts()` | Emits a warning when two pending tasks share the same time slot. |
| Recurring tasks | `Scheduler.mark_task_complete()` | When a daily or weekly task is completed, a new task is created for the next occurrence. |

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step -->
2. <!-- Describe this step -->
3. <!-- Describe this step -->
4. <!-- Describe this step -->
5. <!-- Add more steps as needed -->

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
