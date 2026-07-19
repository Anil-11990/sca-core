"""
Credential ID Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CredentialId:
    """
    Unique certificate credential identifier.
    """

    value: str

    def __post_init__(self):
        if not self.value:
            raise ValueError(
                "Credential ID cannot be empty."
            )

        if not self.value.strip():
            raise ValueError(
                "Credential ID cannot contain only spaces."
            )

    def __str__(self):
        return self.value