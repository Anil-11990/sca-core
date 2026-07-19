from app.domain.education.value_objects.institution_name import (
    InstitutionName,
)


def test_create_institution_name():
    institution = InstitutionName(
        "University of West London"
    )

    assert (
        str(institution)
        == "University of West London"
    )


def test_institution_name_cannot_be_empty():
    try:
        InstitutionName("")

        assert False

    except ValueError:
        assert True