from app.domain.evidence.entity import Evidence
from app.domain.services.evidence_strength_service import (
    EvidenceStrengthService,
)


def test_complete_evidence_has_maximum_score():

    evidence = Evidence(
        title="SCA Core Architecture",
        description="AI career operating system implementation",
        evidence_type="Project",
        reference_url="github.com/anil/sca",
    )

    service = EvidenceStrengthService()

    score = service.calculate(
        evidence
    )

    assert score == 100


def test_empty_optional_information_scores_lower():

    evidence = Evidence(
        title="Small Project",
    )

    service = EvidenceStrengthService()

    score = service.calculate(
        evidence
    )

    assert score == 30