from app.domain.goal.status import GoalStatus


def test_goal_status_not_started_exists():
    assert GoalStatus.NOT_STARTED.value == "NOT_STARTED"


def test_goal_status_in_progress_exists():
    assert GoalStatus.IN_PROGRESS.value == "IN_PROGRESS"


def test_goal_status_completed_exists():
    assert GoalStatus.COMPLETED.value == "COMPLETED"


def test_goal_status_has_three_states():
    assert len(GoalStatus) == 3