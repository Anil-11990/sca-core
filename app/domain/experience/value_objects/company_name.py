"""
Company Name Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True)
class CompanyName:
    """
    Represents the name of a company where a
    Professional has worked.
    """

    value: str

    def __post_init__(self):
        """
        Validate the company name.
        """

        if not self.value:
            raise ValueError(
                "Company name cannot be empty."
            )

        if not self.value.strip():
            raise ValueError(
                "Company name cannot contain only spaces."
            )

        if len(self.value.strip()) < 2:
            raise ValueError(
                "Company name is too short."
            )

        if len(self.value.strip()) > 100:
            raise ValueError(
                "Company name cannot exceed 100 characters."
            )

    def __str__(self):
        return self.value