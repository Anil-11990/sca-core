"""
Certificate Issuer Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class Issuer:
    """
    Certificate issuing organisation.
    """

    value: str

    def __post_init__(self):

        if not self.value:
            raise ValueError(
                "Certificate issuer cannot be empty."
            )

        if not self.value.strip():
            raise ValueError(
                "Certificate issuer cannot contain only spaces."
            )

    def __str__(self):
        return self.value