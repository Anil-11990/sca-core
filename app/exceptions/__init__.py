"""
Application Exceptions.
"""

from .professional_not_found import ProfessionalNotFoundException
from .duplicate_entity import DuplicateEntityException
from .repository_exception import RepositoryException
from .validation_exception import ValidationException

__all__ = [
    "ProfessionalNotFoundException",
    "DuplicateEntityException",
    "RepositoryException",
    "ValidationException",
]