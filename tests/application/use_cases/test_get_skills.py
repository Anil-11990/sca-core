from app.application.use_cases.get_skills import GetSkills
from app.domain.common.value_objects.full_name import FullName
from app.domain.professional.professional import Professional
from app.domain.skill.skill import Skill


def test_get_skills():
    professional = Professional(
        full_name=FullName("Anil Khanal"),
        primary_goal="Build ANIrex AI",
    )

    python = Skill("Python")
    fastapi = Skill("FastAPI")

    professional.add_skill(python)
    professional.add_skill(fastapi)

    use_case = GetSkills()

    skills = use_case.execute(professional)

    assert len(skills) == 2
    assert python in skills
    assert fastapi in skills