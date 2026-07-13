from app.application.use_cases.create_professional import CreateProfessional
from app.domain.professional.professional import Professional
from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_create_professional():
    """
    Creating a Professional should also save it
    using the configured repository.
    """

    repository = MemoryProfessionalRepository()

    use_case = CreateProfessional(repository)

    professional = use_case.execute(
        full_name="Anil Khanal",
        primary_goal="Build ANIrex AI",
    )

    assert isinstance(professional, Professional)

    loaded = repository.get_by_id(professional.id)

    assert loaded == professional