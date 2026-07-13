"""
Application Use Case:
Create Professional
"""

from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional


class CreateProfessional:
    """
    Creates a new Professional aggregate.

    This class represents the application layer use case.
    """

    def execute(
        self,
        full_name: str,
        primary_goal: str,
    ) -> Professional:
        """
        Purpose:
            Creates a Professional.

        Future:
            Repository persistence,
            events,
            auditing,
            validation,
            AI onboarding.
        """

        return Professional(
            full_name=FullName(full_name),
            primary_goal=primary_goal,
        )