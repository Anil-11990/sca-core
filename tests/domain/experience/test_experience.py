from app.domain.experience.experience import Experience
from app.domain.experience.value_objects.job_title import RoleTitle
from app.domain.experience.value_objects.company_name import CompanyName


def test_create_experience():
    experience = Experience(
        role=RoleTitle("Software Engineer"),
        company=CompanyName("ANIrex"),
        description="Building AI systems and backend services.",
    )

    assert experience.role == RoleTitle("Software Engineer")
    assert experience.company == CompanyName("ANIrex")
    assert experience.description == (
        "Building AI systems and backend services."
    )