from uuid import uuid4

from app.application.use_cases.intelligence.generate_career_roadmap import (
    GenerateCareerRoadmap,
)

from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.domain.services.career_roadmap_service import (
    CareerRoadmapService,
)


class FakeProfessionalRepository:

    def __init__(self, professional):
        self.professional = professional

    def get_by_id(self, professional_id):

        if professional_id == self.professional.id:
            return self.professional

        return None


def test_generate_career_roadmap():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Become AI Engineer",
    )

    repository = FakeProfessionalRepository(
        professional
    )

    use_case = GenerateCareerRoadmap(
        repository=repository,
        roadmap_service=CareerRoadmapService(),
    )

    roadmap = use_case.execute(
        professional.id
    )

    assert isinstance(
        roadmap,
        list,
    )


def test_generate_career_roadmap_rejects_unknown_professional():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Become AI Engineer",
    )

    repository = FakeProfessionalRepository(
        professional
    )

    use_case = GenerateCareerRoadmap(
        repository=repository,
        roadmap_service=CareerRoadmapService(),
    )

    unknown_id = uuid4()

    try:

        use_case.execute(
            unknown_id
        )

        assert False

    except Exception as exc:

        assert (
            type(exc).__name__
            == "ProfessionalNotFoundException"
        )