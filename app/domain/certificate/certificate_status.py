"""
Certificate Status.

Represents the lifecycle state
of a professional certificate.
"""

from enum import Enum


class CertificateStatus(str, Enum):
    """
    Certificate lifecycle states.
    """

    ACTIVE = "Active"

    EXPIRED = "Expired"

    REVOKED = "Revoked"