from app.domain.education.value_objects.degree_name import (
    DegreeName,
)


def test_create_degree_name():
    degree = DegreeName(
        "BSc Computer Science"
    )

    assert str(degree) == "BSc Computer Science"


def test_degree_name_cannot_be_empty():
    try:
        DegreeName("")

        assert False

    except ValueError:
        assert True
