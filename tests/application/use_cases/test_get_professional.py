from app.application.use_cases.get_professional import GetProfessional
from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName
from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_get_professional():
    """
    A saved professional can be retrieved by ID.
    """

    repository = MemoryProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    repository.save(professional)

    use_case = GetProfessional(repository)

    result = use_case.execute(professional.id)

    assert result == professional