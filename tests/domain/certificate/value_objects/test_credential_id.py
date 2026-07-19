from app.domain.certificate.value_objects.credential_id import (
    CredentialId,
)


def test_create_credential_id():

    credential = CredentialId(
        "AWS-123456"
    )

    assert str(credential) == (
        "AWS-123456"
    )


def test_credential_id_cannot_be_empty():

    try:
        CredentialId("")

        assert False

    except ValueError:
        assert True


def test_credential_id_cannot_be_spaces():

    try:
        CredentialId("   ")

        assert False

    except ValueError:
        assert True