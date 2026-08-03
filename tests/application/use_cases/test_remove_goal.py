"""
Tests for Remove Goal Use Case.
"""

from app.application.use_cases.remove_goal import (
    RemoveGoalUseCase,
)

from app.domain.goal.goal import Goal

from app.domain.goal.value_objects.goal_title import (
    GoalTitle,
)

from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)



def test_remove_goal():

    # ---------------------------------
    # Arrange
    # Create repository
    # ---------------------------------

    repo = MemoryProfessionalRepository()



    # ---------------------------------
    # Create professional
    # ---------------------------------

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )



    # ---------------------------------
    # Add existing goal
    # ---------------------------------

    goal = Goal(
        title=GoalTitle(
            "Launch SCA MVP"
        )
    )


    professional.add_goal(
        goal
    )


    repo.save(
        professional
    )



    # ---------------------------------
    # Execute remove
    # ---------------------------------

    use_case = RemoveGoalUseCase(
        repo
    )


    result = use_case.execute(
        professional.id,
        goal.id,
    )



    # ---------------------------------
    # Assert
    # ---------------------------------

    assert len(
        result.goals
    ) == 0