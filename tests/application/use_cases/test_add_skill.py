from app.application.use_cases.add_skill import AddSkill
from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.domain.skill.skill import Skill


def test_add_skill_use_case():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI"
    )

    use_case = AddSkill()

    skill = Skill("Python")

    use_case.execute(
        professional=professional,
        skill=skill
    )

    assert skill in professional.skills