"""
Education Entity

Represents an academic qualification
inside a professional profile.
"""

from uuid import UUID, uuid4

from app.domain.education.degree_level import DegreeLevel
from app.domain.education.graduation_status import GraduationStatus
from app.domain.education.value_objects.institution_name import InstitutionName


class Education:
    """
    Education entity.

    Represents:
    - institution
    - qualification level
    - field of study
    - completion status
    """

    def __init__(
            self,
            institution: str | InstitutionName,
            degree_level: DegreeLevel,
            field_of_study: str,
            graduation_status: GraduationStatus,
            id: UUID | None = None,
    ):

        if isinstance(institution, str):
            institution = InstitutionName(institution)


        if not field_of_study or not field_of_study.strip():
            raise ValueError(
                "Field of study cannot be empty"
            )


        if not degree_level:
            raise ValueError(
                "Degree level is required"
            )


        if not graduation_status:
            raise ValueError(
                "Graduation status is required"
            )


        self.id = id or uuid4()

        self.institution = institution

        self.degree_level = degree_level

        self.field_of_study = field_of_study.strip()

        self.graduation_status = graduation_status


    def __eq__(self, other):

        if not isinstance(other, Education):
            return False

        return self.id == other.id


    def __repr__(self):

        return (
            f"Education("
            f"institution={self.institution}, "
            f"degree={self.degree_level.value}, "
            f"field={self.field_of_study}, "
            f"status={self.graduation_status.value}"
            f")"
        )