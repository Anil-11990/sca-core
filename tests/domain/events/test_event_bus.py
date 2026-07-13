from app.domain.events.event_bus import EventBus
from app.domain.events.goal_completed import GoalCompleted
from app.domain.goal.goal import Goal
from app.domain.goal.value_objects.goal_title import GoalTitle


def test_event_bus_can_publish_events():
    bus = EventBus()

    goal = Goal(
        title=GoalTitle("Launch MVP")
    )

    event = GoalCompleted(goal=goal)

    bus.publish(event)

    assert len(bus.events) == 1
    assert bus.events[0] == event