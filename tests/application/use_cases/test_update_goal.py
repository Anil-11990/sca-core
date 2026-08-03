"""
Tests for Update Goal Use Case.
"""

from app.application.use_cases.update_goal import (
    UpdateGoalUseCase,
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



def test_update_goal():

    # ---------------------------------
    # Arrange
    # Repository
    # ---------------------------------

    repo = MemoryProfessionalRepository()



    # ---------------------------------
    # Create Professional
    # ---------------------------------

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )



    # ---------------------------------
    # Existing Goal
    # ---------------------------------

    old_goal = Goal(
        title=GoalTitle(
            "Build Portfolio"
        )
    )


    professional.add_goal(
        old_goal
    )


    repo.save(
        professional
    )



    # ---------------------------------
    # Updated Goal
    # ---------------------------------

    updated_goal = Goal(
        title=GoalTitle(
            "Launch SCA MVP"
        )
    )


    # Preserve identity
    # Update replaces same entity
    updated_goal.id = old_goal.id



    # ---------------------------------
    # Execute
    # ---------------------------------

    use_case = UpdateGoalUseCase(
        repo
    )


    result = use_case.execute(
        professional.id,
        updated_goal,
    )



    # ---------------------------------
    # Assert
    # ---------------------------------

    assert len(
        result.goals
    ) == 1


    assert (
        result.goals[0]
        .title.value
        ==
        "Launch SCA MVP"
    )