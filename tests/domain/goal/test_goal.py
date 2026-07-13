from app.domain.goal.goal import Goal
from app.domain.goal.value_objects.goal_title import GoalTitle
from app.domain.goal.status import GoalStatus


def test_goal_has_title():
    goal = Goal(
        title=GoalTitle("Build ANIrex AI")
    )

    assert goal.title == GoalTitle("Build ANIrex AI")


def test_goal_starts_not_started():
    goal = Goal(
        title=GoalTitle("Build ANIrex AI")
    )

    assert goal.status == GoalStatus.NOT_STARTED


def test_goal_starts_with_zero_progress():
    goal = Goal(
        title=GoalTitle("Build ANIrex AI")
    )

    assert goal.progress == 0


def test_progress_cannot_be_negative():
    goal = Goal(
        title=GoalTitle("Build ANIrex AI")
    )

    try:
        goal.update_progress(-1)
        assert False
    except ValueError:
        assert True


def test_progress_cannot_exceed_100():
    goal = Goal(
        title=GoalTitle("Build ANIrex AI")
    )

    try:
        goal.update_progress(101)
        assert False
    except ValueError:
        assert True


def test_goal_completes_at_100_percent():
    goal = Goal(
        title=GoalTitle("Build ANIrex AI")
    )

    goal.update_progress(100)

    assert goal.progress == 100
    assert goal.status == GoalStatus.COMPLETED