from app.domain.experience.employment_type import EmploymentType


def test_employment_type_values():
    assert EmploymentType.FULL_TIME.value == "Full-time"
    assert EmploymentType.PART_TIME.value == "Part-time"
    assert EmploymentType.CONTRACT.value == "Contract"
    assert EmploymentType.INTERNSHIP.value == "Internship"
    assert EmploymentType.FREELANCE.value == "Freelance"