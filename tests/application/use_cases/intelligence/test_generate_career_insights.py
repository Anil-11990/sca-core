from app.application.use_cases.intelligence.generate_career_insights import (
    GenerateCareerInsights,
)

from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName


class FakeProfessionalRepository:

    def __init__(self, professional):
        self.professional = professional


    def get_by_id(self, professional_id):
        return self.professional



def test_generate_career_insights():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


    repository = FakeProfessionalRepository(
        professional
    )


    use_case = GenerateCareerInsights(
        repository
    )


    insights = use_case.execute(
        professional.id
    )


    assert isinstance(
        insights,
        list
    )