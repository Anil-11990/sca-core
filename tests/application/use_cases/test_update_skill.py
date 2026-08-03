from app.application.use_cases.update_skill import UpdateSkill

from app.domain.skill.skill import Skill

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.domain.professional.professional import (
    Professional,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_update_skill():

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
    # Existing skill
    # ---------------------------------

    old_skill = Skill(
        "Python"
    )


    professional.add_skill(
        old_skill
    )


    repo.save(
        professional
    )


    # ---------------------------------
    # Updated skill
    # ---------------------------------

    new_skill = Skill(
        "Artificial Intelligence"
    )


    # Keep same ID because update
    # replaces the existing entity

    new_skill.id = old_skill.id


    # ---------------------------------
    # Execute update use case
    # ---------------------------------

    use_case = UpdateSkill(
        repo
    )


    updated = use_case.execute(
        professional.id,
        new_skill,
    )


    # ---------------------------------
    # Assert
    # ---------------------------------

    assert len(
        updated.skills
    ) == 1


    assert (
        updated.skills[0].name
        == "Artificial Intelligence"
    )