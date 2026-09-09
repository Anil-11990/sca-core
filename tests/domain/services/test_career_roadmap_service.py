from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName
from app.domain.skill.skill import Skill

from app.domain.services.career_roadmap_service import (
    CareerRoadmapService,
)


def test_ai_career_roadmap_generation():

    professional = Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Become AI Engineer",
    )

    professional.add_skill(
        Skill("Python")
    )

    service = CareerRoadmapService()

    roadmap = service.generate(
        professional,
        [
            "Python",
            "FastAPI",
            "React",
        ],
    )

    assert len(roadmap) == 2

    assert roadmap[0]["skill"] == "FastAPI"
    assert roadmap[1]["skill"] == "React"

    assert roadmap[0]["stage"] == "Learning"
