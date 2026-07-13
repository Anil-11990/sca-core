"""
Application Use Case:
Add Skill
"""

from app.domain.professional.professional import Professional
from app.domain.skill.skill import Skill


class AddSkill:
    """
    Application use case for adding a skill
    to a Professional.
    """

    def execute(
        self,
        professional: Professional,
        skill: Skill,
    ) -> None:
        """
        Purpose:
            Adds a skill to the Professional.

        Business Rule:
            Delegates the operation to the
            Professional aggregate.

        Future:
            Repository persistence,
            domain events,
            audit logging.
        """

        professional.add_skill(skill)