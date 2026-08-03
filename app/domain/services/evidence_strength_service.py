"""
Domain Service:
Evidence Strength

Evaluates the strength of career evidence.
"""

from app.domain.evidence.entity import Evidence


class EvidenceStrengthService:
    """
    Calculates evidence quality score.

    Maximum score = 100
    """

    def calculate(
        self,
        evidence: Evidence,
    ) -> int:

        score = 0

        # Evidence title exists
        if evidence.title:
            score += 30

        # Description gives context
        if evidence.description:
            score += 25

        # Evidence category
        if evidence.evidence_type:
            score += 20

        # External verification
        if evidence.reference_url:
            score += 25

        return score