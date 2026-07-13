from app.domain.professional.professional import Professional
from app.domain.goal.goal import Goal
from app.domain.goal.value_objects.goal_title import GoalTitle
from app.domain.common.value_objects.full_name import FullName


def test_add_goal():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI"
    )

    goal = Goal(
        title=GoalTitle("Launch SCA MVP")
    )

    professional.add_goal(goal)

    assert goal in professional.goals


def test_duplicate_goal_is_not_added():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI"
    )

    goal = Goal(
        title=GoalTitle("Launch SCA MVP")
    )

    professional.add_goal(goal)
    professional.add_goal(goal)

    assert len(professional.goals) == 1


def test_goals_are_read_only():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI"
    )

    assert isinstance(professional.goals, tuple)