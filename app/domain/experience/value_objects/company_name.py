"""
Company Name Value Object.
"""

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class CompanyName:
    """
    Represents a company name.
    """

    value: str

    def __post_init__(self) -> None:
        value = self.value.strip()

        if not value:
            raise ValueError(
                "Company name cannot be empty."
            )

        object.__setattr__(self, "value", value)

    def __str__(self) -> str:
        return self.value