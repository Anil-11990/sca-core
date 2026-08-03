from app.application.use_cases.remove_skill import RemoveSkill
from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.domain.skill.skill import Skill


def test_remove_skill():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    python = Skill("Python")

    professional.add_skill(python)

    RemoveSkill().execute(
        professional,
        python,
    )

    assert len(professional.skills) == 0