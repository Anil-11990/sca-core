from app.application.use_cases.intelligence.analyze_career import (
    AnalyzeCareer,
)

from app.domain.intelligence.career_analyzer import (
    CareerAnalyzer,
)

from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)


class FakeProfessionalRepository:

    def __init__(self, professional):
        self.professional = professional


    def get_by_id(self, entity_id):
        return self.professional


    def save(self, professional):
        pass



def test_analyze_career_returns_intelligence():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


    repository = FakeProfessionalRepository(
        professional
    )


    use_case = AnalyzeCareer(
        repository,
        CareerAnalyzer(),
    )


    result = use_case.execute(
        professional.id,
        [
            "Python",
            "AI",
        ],
    )

    assert result.career_score >= 0
    assert result.profile_completion >= 0
    assert isinstance(result.skill_gaps, list)
    assert result.career_readiness >= 0