import pytest

from app.domain.experience.experience import Experience
from app.domain.experience.value_objects.job_title import RoleTitle
from app.domain.experience.value_objects.company_name import CompanyName


def test_description_cannot_be_empty():
    with pytest.raises(ValueError):
        Experience(
            role=RoleTitle("Software Engineer"),
            company=CompanyName("ANIrex"),
            description="",
        )