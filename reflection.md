# PawPal+ Project Reflection

## 1. System Design

PawPal+ should let a user perform three core actions:

1. **Add/manage pet and task info** — enter owner and pet details, and add or edit care tasks (walks, feeding, meds, enrichment, grooming) with at least a duration and priority.
2. **Generate a daily plan** — request a schedule and have the system build one by weighing task durations, priorities, and available time.
3. **View today's plan with reasoning** — see the resulting schedule for the day along with an explanation of why tasks were included, ordered, or skipped.

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

My initial UML has four independent classes:

- **Owner** — holds the pet owner's basic info (name, contact info) and scheduling preferences (preferred start/end time for the day). Responsible for adding pets and kicking off task management and daily plan generation.
- **Pet** — holds basic info about the animal (name, breed, age, special needs). Responsible for exposing the tasks assigned to it and its resulting daily schedule.
- **Task** — represents a single care activity (name, duration, priority, optional time constraints). Responsible for its own create/edit/delete lifecycle.
- **Schedule** — represents a day's plan: a date, an ordered list of tasks, total duration, and the reasoning behind the plan. Responsible for building itself from a set of tasks, reordering by priority, and displaying the final plan.

The relationships are: an Owner owns one or more Pets, a Pet has many Tasks assigned to it, and a Schedule includes many Tasks for a given day.



**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes. An AI review of `pawpal_system.py` against the UML flagged that the classes had no way to reference each other, even though the diagram implies they should:

- Added a `pet` field on `Task` so each task can point back to the `Pet` it belongs to (the UML only showed `Pet -> Task`, not the reverse, which made it impossible to tell which pet a standalone task belonged to).
- Added a `tasks` field and an `owner` field on `Pet`, so a pet can list its own tasks and be traced back to its owner.
- Added a `pet` field on `Schedule`, so a generated schedule can be tied to the specific pet (and, through it, the owner) it was built for.
- Decided that `Schedule.generate_from_tasks()` should be the single place the scheduling algorithm lives, with `Owner.generate_daily_plan()` simply delegating to it once implemented — this avoids duplicating scheduling logic in two places.

When writing the full implementation, the design changed further:

- Renamed `Schedule` to `Scheduler` and reframed it as the "brain" of the system: instead of just holding one day's ordered task list, `Scheduler` now takes an `Owner` and actively retrieves and organizes tasks across all of that owner's pets (`get_all_tasks`, `get_pending_tasks`, `get_tasks_by_pet`, `organize_by_time`). This matched the real responsibility better — the class does the organizing, it isn't just a data container for the result.
- Changed `Task`'s fields from `name, duration, priority, time_constraints` to `description, time, frequency, is_completed`. This shifted the model from a priority/duration-based scheduling task to a recurring-care-task model (e.g., "feed cat" every "daily" at "08:00"), with an explicit completion flag instead of relying on `Schedule` to track what's been done.
- `Owner` dropped `preferred_start_time`/`preferred_end_time` since time-window constraints are no longer part of the simplified `Task` model, and gained `get_all_tasks()` to aggregate tasks across its pets directly.
- If yes, describe at least one change and why you made it.

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

One tradeoff is that the scheduler only checks for exact time matches when detecting conflicts, rather than trying to reason about overlapping durations or time windows. That is reasonable for this starter version because it keeps the logic simple, readable, and fast while still catching the most obvious scheduling problems such as two tasks assigned to the same time slot.

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
