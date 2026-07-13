from app.domain.professional.professional import Professional
from app.domain.skill.skill import Skill
from app.domain.common.value_objects.full_name import FullName


def test_add_skill():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI"
    )

    python = Skill("Python")

    professional.add_skill(python)

    assert python in professional.skills


def test_duplicate_skill_is_not_added():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI"
    )

    python = Skill("Python")

    professional.add_skill(python)
    professional.add_skill(python)

    assert len(professional.skills) == 1


def test_skills_are_read_only():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI"
    )

    assert isinstance(professional.skills, tuple)