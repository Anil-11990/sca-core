import pytest

from app.domain.skill.skill import Skill


def test_skill_has_name():
    skill = Skill(name="Python")

    assert skill.name == "Python"


def test_skill_name_is_trimmed():
    skill = Skill(name="   Python   ")

    assert skill.name == "Python"


def test_skill_requires_name():
    with pytest.raises(ValueError):
        Skill(name="")


def test_skill_requires_non_blank_name():
    with pytest.raises(ValueError):
        Skill(name="     ")