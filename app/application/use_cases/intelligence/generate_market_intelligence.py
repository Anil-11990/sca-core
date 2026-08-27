"""
Application Use Case:
Generate Market Intelligence
"""

from uuid import UUID

from app.domain.services.market_intelligence_service import (
    MarketIntelligenceService,
)
from app.exceptions.professional_not_found import (
    ProfessionalNotFoundException,
)


class GenerateMarketIntelligence:
    """
    Generates market intelligence for a Professional.

    The use case coordinates:

        Professional repository
        Market signals
        MarketIntelligenceService

    Business rules remain inside the domain service.
    """

    def __init__(
        self,
        repository,
        market_intelligence_service: MarketIntelligenceService,
        market_signals,
    ) -> None:

        self._repository = repository
        self._market_intelligence_service = (
            market_intelligence_service
        )
        self._market_signals = market_signals

    def execute(
        self,
        professional_id: UUID,
    ) -> dict:

        professional = (
            self._repository.get_by_id(
                professional_id
            )
        )

        if professional is None:
            raise ProfessionalNotFoundException()

        return self._market_intelligence_service.analyse(
            professional=professional,
            market_signals=self._market_signals,
        )