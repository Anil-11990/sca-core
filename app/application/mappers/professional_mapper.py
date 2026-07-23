"""
Professional Mapper.

Converts Professional Aggregate Root
into ProfessionalResponse DTO.
"""

from app.domain.professional.professional import Professional

from app.application.dto.responses.professional_response import (
    ProfessionalResponse,
)

from app.application.mappers.skill_mapper import SkillMapper
from app.application.mappers.goal_mapper import GoalMapper
from app.application.mappers.project_mapper import ProjectMapper
from app.application.mappers.education_mapper import EducationMapper
from app.application.mappers.experience_mapper import ExperienceMapper
from app.application.mappers.certificate_mapper import CertificateMapper
from app.application.mappers.achievement_mapper import AchievementMapper
from app.application.mappers.timeline_event_mapper import (
    TimelineEventMapper,
)


class ProfessionalMapper:
    """
    Maps Professional Aggregate
    to ProfessionalResponse DTO.
    """

    @staticmethod
    def to_response(
        professional: Professional,
    ) -> ProfessionalResponse:
        """
        Convert complete Professional
        aggregate into response DTO.
        """

        return ProfessionalResponse(

            id=str(
                professional.id
            ),

            full_name=str(
                professional.full_name
            ),

            primary_goal=(
                professional.primary_goal
            ),

            current_title=(
                professional.current_title
            ),

            location=(
                professional.location
            ),

            skills=[
                SkillMapper.to_response(skill)
                for skill in professional.skills
            ],

            goals=[
                GoalMapper.to_response(goal)
                for goal in professional.goals
            ],

            achievements=[
                AchievementMapper.to_response(
                    achievement
                )
                for achievement in professional.achievements
            ],

            certificates=[
                CertificateMapper.to_response(
                    certificate
                )
                for certificate in professional.certificates
            ],

            education=[
                EducationMapper.to_response(
                    education
                )
                for education in professional.educations
            ],

            experiences=[
                ExperienceMapper.to_response(
                    experience
                )
                for experience in professional.experiences
            ],

            projects=[
                ProjectMapper.to_response(project)
                for project in professional.projects
            ],

            timeline=[
                TimelineEventMapper.to_response(event)
                for event in professional.timeline
            ],

            created_at=(
                professional.created_at
            ),
        )