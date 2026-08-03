"""
Tests for Career Score Service.
"""

from datetime import date

from app.domain.professional.professional import Professional
from app.domain.common.value_objects.full_name import FullName

from app.domain.services.career_score_service import (
    CareerScoreService,
)

from app.domain.skill.skill import Skill

from app.domain.project.project import Project
from app.domain.project.value_objects.project_name import (
    ProjectName,
)

from app.domain.experience.experience import Experience
from app.domain.experience.value_objects.job_title import (
    JobTitle,
)
from app.domain.experience.value_objects.company_name import (
    CompanyName,
)
from app.domain.experience.value_objects.experience_period import (
    ExperiencePeriod,
)
from app.domain.experience.employment_type import (
    EmploymentType,
)
from app.domain.experience.experience_description import (
    ExperienceDescription,
)

from app.domain.education.education import Education
from app.domain.education.degree_level import DegreeLevel
from app.domain.education.graduation_status import GraduationStatus

from app.domain.certificate.certificate import Certificate
from app.domain.certificate.value_objects.certificate_name import (
    CertificateName,
)
from app.domain.certificate.value_objects.certificate_issuer import (
    Issuer,
)
from app.domain.certificate.value_objects.credential_id import (
    CredentialId,
)

from app.domain.achievement.achievement import Achievement
from app.domain.achievement.value_objects.achievement_title import (
    AchievementTitle,
)
from app.domain.achievement.value_objects.issuer import (
    Issuer as AchievementIssuer,
)
from app.domain.achievement.achievement_type import (
    AchievementType,
)


def create_professional():

    return Professional(
        full_name=FullName(
            "Anil Khanal"
        ),
        primary_goal="Build ANIrex AI",
    )


def test_empty_professional_has_zero_career_score():

    professional = create_professional()

    service = CareerScoreService()

    score = service.calculate(
        professional
    )

    assert score == 0



def test_complete_professional_has_maximum_career_score():

    professional = create_professional()


    # Skills
    professional.add_skill(
        Skill("Python")
    )

    professional.add_skill(
        Skill("Java")
    )

    professional.add_skill(
        Skill("AI")
    )


    # Projects
    professional.add_project(
        Project(
            name=ProjectName(
                "ANIrex AI"
            )
        )
    )

    professional.add_project(
        Project(
            name=ProjectName(
                "SCA Core"
            )
        )
    )


    # Experience
    professional.add_experience(
        Experience(
            job_title=JobTitle(
                "Software Engineer"
            ),
            company_name=CompanyName(
                "ANIrex"
            ),
            employment_type=EmploymentType.FULL_TIME,
            experience_period=ExperiencePeriod(
                date(2024, 1, 1),
                date(2025, 1, 1),
            ),
            description=ExperienceDescription(
                "Backend development"
            ),
        )
    )
    professional.add_experience(
        Experience(
            job_title=JobTitle(
                "AI Engineer"
            ),
            company_name=CompanyName(
                "ANIrex AI"
            ),
            employment_type=EmploymentType.FULL_TIME,
            experience_period=ExperiencePeriod(
                date(2025, 1, 1),
                date(2026, 1, 1),
            ),
            description=ExperienceDescription(
                "Building AI agent systems"
            ),
        )
    )


    # Education
    professional.add_education(
        Education(
            institution="University of West London",
            degree_level=DegreeLevel.BACHELOR,
            field_of_study="Computer Science",
            graduation_status=GraduationStatus.COMPLETED,
        )
    )


    # Certificate
    professional.add_certificate(
        Certificate(
            name=CertificateName(
                "Python Certificate"
            ),
            issuer=Issuer(
                "Coursera"
            ),
            credential_id=CredentialId(
                "CERT-001"
            ),
            issued_date=date(
                2025,
                1,
                1
            ),
        )
    )


    # Achievement
    professional.add_achievement(
        Achievement(
            title=AchievementTitle(
                "Built SCA Architecture"
            ),
            issuer=AchievementIssuer(
                "ANIrex"
            ),
            achievement_type=AchievementType.OPEN_SOURCE,
        )
    )


    service = CareerScoreService()

    score = service.calculate(
        professional
    )


    assert score == 100