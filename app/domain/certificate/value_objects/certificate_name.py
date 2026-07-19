"""
Certificate Name Value Object.

Represents the official name/title
of a professional certificate.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CertificateName:
    """
    Certificate name.

    Examples:
    - AWS Certified Developer Associate
    - Google Professional Cloud Architect
    """

    value: str

    def __post_init__(self) -> None:
        """
        Validate certificate name.
        """

        if not self.value:
            raise ValueError(
                "Certificate name cannot be empty."
            )

        if not self.value.strip():
            raise ValueError(
                "Certificate name cannot contain only spaces."
            )

    def __str__(self) -> str:
        return self.value