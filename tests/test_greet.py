"""Tests for the greet module."""

import pytest
from basic_python_project.greet import greet


class TestGreet:
    """Test cases for the greet function."""

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("Alice", "Hello, Mr./Ms. Alice!"),
            ("Bob", "Hello, Mr./Ms. Bob!"),
            ("", "Hello, Anonymous!"),
        ],
    )
    def test_greet_with_different_names(self, name: str, expected: str) -> None:
        """Test greet function with different names."""
        assert greet(name) == expected

    def test_greet_returns_string(self) -> None:
        """Test that greet function returns a string."""
        result = greet("Test")
        assert isinstance(result, str)
