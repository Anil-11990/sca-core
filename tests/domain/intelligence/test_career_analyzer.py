from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName

from app.domain.intelligence.career_analyzer import (
    CareerAnalyzer,
)


def test_career_analyzer_returns_report():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


    analyzer = CareerAnalyzer()


    result = analyzer.analyze(
        professional,
        [
            "Python",
            "Machine Learning",
        ],
    )


    assert result["career_score"] == 0

    assert result["profile_completion"] == 40

    assert result["skill_gaps"] == [
        "Python",
        "Machine Learning",
    ]

    assert result["career_readiness"] == 0