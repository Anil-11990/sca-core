from app.application.use_cases.complete_goal import CompleteGoal
from app.domain.common.value_objects.full_name import FullName
from app.domain.goal.goal import Goal
from app.domain.goal.status import GoalStatus
from app.domain.goal.value_objects.goal_title import GoalTitle
from app.domain.professional.professional import Professional


def test_complete_goal_use_case():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI"
    )

    goal = Goal(
        title=GoalTitle("Launch MVP")
    )

    professional.add_goal(goal)

    use_case = CompleteGoal()

    use_case.execute(goal)

    assert goal.progress == 100
    assert goal.status == GoalStatus.COMPLETED