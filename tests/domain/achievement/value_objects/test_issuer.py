"""
Tests for Issuer.
"""

import pytest

from app.domain.achievement.value_objects.issuer import (
    Issuer,
)


def test_create_issuer():
    issuer = Issuer("Google")

    assert str(issuer) == "Google"


def test_issuer_is_trimmed():
    issuer = Issuer("  Google  ")

    assert str(issuer) == "Google"


def test_empty_issuer_raises_error():
    with pytest.raises(ValueError):
        Issuer("")


def test_whitespace_issuer_raises_error():
    with pytest.raises(ValueError):
        Issuer("    ")