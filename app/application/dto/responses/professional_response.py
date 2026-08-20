"""
Response DTO for Professional.
"""

from dataclasses import dataclass
from datetime import datetime

from app.application.dto.responses.skill_response import SkillResponse
from app.application.dto.responses.goal_response import GoalResponse
from app.application.dto.responses.project_response import ProjectResponse
from app.application.dto.responses.education_response import EducationResponse
from app.application.dto.responses.experience_response import ExperienceResponse
from app.application.dto.responses.certificate_response import CertificateResponse
from app.application.dto.responses.achievement_response import AchievementResponse
from app.application.dto.responses.timeline_event_response import (
    TimelineEventResponse,
)


@dataclass(slots=True, frozen=True)
class ProfessionalResponse:
    """
    Complete response DTO representing
    the Professional aggregate.
    """

    id: str

    full_name: str

    primary_goal: str

    current_title: str

    location: str

    skills: list[SkillResponse]

    goals: list[GoalResponse]

    achievements: list[AchievementResponse]

    certificates: list[CertificateResponse]

    education: list[EducationResponse]

    experiences: list[ExperienceResponse]

    projects: list[ProjectResponse]

    timeline: list[TimelineEventResponse]

    created_at: datetime