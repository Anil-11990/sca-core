from app.domain.events.goal_completed import GoalCompleted
from app.domain.goal.goal import Goal
from app.domain.goal.value_objects.goal_title import GoalTitle


def test_goal_completed_event():
    goal = Goal(
        title=GoalTitle("Launch MVP")
    )

    event = GoalCompleted(goal=goal)

    assert event.goal == goal