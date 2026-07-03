# PawPal+ Project Reflection

## 1. System Design

PawPal+ lets a user perform three core actions:

1. Add and manage pet and task information.
2. Generate a simple daily plan from the tasks that have been entered.
3. Review the resulting schedule, including pending items and any overlap warnings.

### a. Initial design

My initial UML design centered on four core classes:

- Owner — stores the owner's basic details and owns a collection of pets.
- Pet — stores pet details and tracks the tasks assigned to that pet.
- Task — represents a single care activity, including a description, time, and recurrence frequency.
- Scheduler — organizes tasks across pets and provides useful views such as sorting, filtering, and conflict detection.

The initial relationships were straightforward: an Owner owns one or more Pets, a Pet has many Tasks, and the Scheduler works over that owner-pet-task structure.

### b. Design changes

The design changed as the implementation became more concrete. The biggest adjustment was moving from a more abstract scheduling concept to a clearer domain model that matched the actual code:

- I added a back-reference from Task to Pet so each task can be traced to the pet it belongs to.
- I kept Pet responsible for holding its own list of tasks and for returning that list to the scheduler.
- I refined the role of Scheduler so it became the organizing layer of the system rather than a passive container.
- I simplified the task model to focus on recurring care tasks with a time and frequency, which made the recurrence behavior easier to implement and test.

These changes made the architecture cleaner because each class now has a single, obvious responsibility.

---

## 2. Scheduling Logic and Tradeoffs

### a. Constraints and priorities

The scheduler currently considers:

- Task time values, which determine chronological ordering
- Completion status, which determines whether a task is pending or already done
- Recurrence frequency, which controls how a completed task creates the next occurrence
- Exact time matches, which are used to flag conflicts

I prioritized the constraints that were easiest to understand and most useful for a starter version of the app: order, pending status, and duplicate-time conflicts.

### b. Tradeoffs

One important tradeoff is that conflict detection only checks for exact time matches. It does not yet reason about task durations or overlapping windows. That is reasonable for this version because it keeps the logic simple, readable, and testable while still helping a pet owner catch obvious scheduling problems.

---

## 3. AI Collaboration

### a. How I used AI

I used my AI coding assistant throughout the project for three main tasks:

- Brainstorming the class structure and reviewing whether the UML matched the implementation
- Drafting and refining tests for the scheduler behaviors
- Debugging and explaining issues when the test suite or UI behavior did not match expectations

The most effective prompts were specific ones that asked for either test cases, implementation guidance, or a comparison between the current code and the intended design.

### b. Judgment and verification

One AI suggestion I rejected was the idea of keeping scheduling logic inside the UI layer. That would have made the app harder to test and would have duplicated logic between the interface and the backend. I modified that suggestion by keeping the scheduling behavior in Scheduler and letting the Streamlit app simply display the results.

I verified AI-generated suggestions by checking them against the existing class responsibilities and by running the tests after each change.

### c. AI strategy reflection

Using separate chat sessions for different phases helped me stay organized. I could focus one session on designing the classes and another on testing or UI integration without mixing goals. That made the work feel more intentional and reduced confusion.

My main lesson as the lead architect was that AI is most useful when it accelerates exploration and implementation, but the final design still needs a human decision-maker. I had to define the boundaries of each class, choose what mattered most, and make sure the system stayed simple and maintainable.

---

## 4. Testing and Verification

### a. What I tested

I tested the core scheduler behaviors that matter most for this app:

- Sorting tasks into chronological order
- Creating the next recurring task after a daily task is marked complete
- Detecting duplicate-time conflicts
- Handling the edge case of a pet with no tasks

These tests were important because they verify the features that users would notice immediately in the UI.

### b. Confidence

I am highly confident in the current implementation because the automated suite passes and the main behaviors are covered by tests. If I had more time, I would add tests for more complex edge cases such as multiple overlapping conflicts, weekly recurrence after completion, and validation for malformed task times.

---

## 5. Reflection

### a. What went well

I am most satisfied with the way the backend and UI now work together. The scheduler logic is clear, the Streamlit interface makes those behaviors visible, and the test suite gives confidence that the core features are stable.

### b. What I would improve

If I had another iteration, I would expand the scheduler to support more realistic constraints, such as task durations, priorities, or time windows, and I would make the conflict warnings more interactive.

### c. Key takeaway

One important lesson was that good system design matters even more when AI tools are involved. The AI can generate code quickly, but it is still the architect's job to keep the design coherent, purposeful, and easy to verify.
