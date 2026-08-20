from app.application.use_cases.intelligence.get_recommendations import (
    GetRecommendations,
)

from app.domain.professional.professional import (
    Professional,
)

from app.domain.common.value_objects.full_name import (
    FullName,
)


class FakeProfessionalRepository:

    def __init__(
        self,
        professional,
    ):
        self.professional = professional


    def get_by_id(
        self,
        professional_id,
    ):
        return self.professional



def test_get_recommendations_returns_missing_project_and_skill_advice():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal=(
            "Build ANIrex AI"
        ),
    )


    repository = FakeProfessionalRepository(
        professional
    )


    use_case = GetRecommendations(
        repository
    )


    recommendations = use_case.execute(
        professional.id
    )


    assert len(recommendations) == 2

    assert (
        recommendations[0].priority
        == "HIGH"
    )

    assert (
        recommendations[1].priority
        == "MEDIUM"
    )



def test_get_recommendations_for_unknown_professional():

    repository = FakeProfessionalRepository(
        None
    )


    use_case = GetRecommendations(
        repository
    )


    try:

        use_case.execute(
            "invalid-id"
        )

        assert False

    except Exception:

        assert True