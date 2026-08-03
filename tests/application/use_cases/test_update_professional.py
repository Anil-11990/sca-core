from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)

from app.application.use_cases.update_professional import (
    UpdateProfessional,
)


def test_update_professional():

    # -----------------------------
    # Arrange
    # -----------------------------

    repository = MemoryProfessionalRepository()


    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


    repository.save(
        professional
    )


    # -----------------------------
    # Execute
    # -----------------------------

    use_case = UpdateProfessional(
        repository
    )


    updated = use_case.execute(
        professional.id,
        "Anil Kumar Khanal",
        "Launch SCA MVP",
    )


    # -----------------------------
    # Assert
    # -----------------------------

    assert updated.full_name == FullName(
        "Anil Kumar Khanal"
    )

    assert updated.primary_goal == (
        "Launch SCA MVP"
    )


    # verify repository persistence

    stored = repository.get_by_id(
        professional.id
    )

    assert stored.full_name == FullName(
        "Anil Kumar Khanal"
    )

    assert stored.primary_goal == (
        "Launch SCA MVP"
    )