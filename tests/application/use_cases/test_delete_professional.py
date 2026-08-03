from pytest import raises

from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)

from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)

from app.application.use_cases.delete_professional import (
    DeleteProfessional,
)

from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


def test_delete_professional():

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

    use_case = DeleteProfessional(
        repository
    )


    use_case.execute(
        professional.id
    )


    # -----------------------------
    # Assert
    # -----------------------------

    with raises(
        ProfessionalNotFoundException
    ):

        repository.get_by_id(
            professional.id
        )