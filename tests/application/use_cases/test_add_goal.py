from app.application.use_cases.add_goal import AddGoal
from app.domain.common.value_objects.full_name import FullName
from app.domain.goal.goal import Goal
from app.domain.goal.value_objects.goal_title import GoalTitle
from app.domain.professional.professional import Professional


def test_add_goal_use_case():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI"
    )

    goal = Goal(
        title=GoalTitle("Launch SCA MVP")
    )

    use_case = AddGoal()

    use_case.execute(
        professional=professional,
        goal=goal
    )

    assert goal in professional.goals