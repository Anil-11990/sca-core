from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.infrastructure.repositories.memory_professional_repository import (
    MemoryProfessionalRepository,
)


def test_save_and_get_professional():
    repo = MemoryProfessionalRepository()

    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    repo.save(professional)

    loaded = repo.get_by_id(professional.id)

    assert loaded == professional