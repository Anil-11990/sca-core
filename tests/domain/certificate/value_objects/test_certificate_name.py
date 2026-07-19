from app.domain.certificate.value_objects.certificate_name import (
    CertificateName,
)


def test_create_certificate_name():
    name = CertificateName(
        "AWS Certified Developer Associate"
    )

    assert str(name) == (
        "AWS Certified Developer Associate"
    )


def test_certificate_name_cannot_be_empty():

    try:
        CertificateName("")

        assert False

    except ValueError:
        assert True


def test_certificate_name_cannot_be_spaces():

    try:
        CertificateName("   ")

        assert False

    except ValueError:
        assert True