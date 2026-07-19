from app.domain.certificate.value_objects.certificate_issuer import (
    Issuer,
)


def test_create_issuer():

    issuer = Issuer(
        "Amazon Web Services"
    )

    assert str(issuer) == (
        "Amazon Web Services"
    )


def test_issuer_cannot_be_empty():

    try:
        Issuer("")

        assert False

    except ValueError:
        assert True


def test_issuer_cannot_be_spaces():

    try:
        Issuer("   ")

        assert False

    except ValueError:
        assert True