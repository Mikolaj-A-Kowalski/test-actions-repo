"""
Tests for the core functionality.
"""

import pytest
from hello_world.core import greet, farewell


class TestGreet:
    """Test cases for the greet function."""
    
    def test_greet_default(self):
        """Test greeting with default name."""
        result = greet()
        assert result == "Hello, World!"
    
    def test_greet_with_name(self):
        """Test greeting with custom name."""
        result = greet("Python")
        assert result == "Hello, Python!"
    
    def test_greet_with_empty_string(self):
        """Test greeting with empty string."""
        result = greet("")
        assert result == "Hello, !"
    
    def test_greet_with_special_characters(self):
        """Test greeting with special characters."""
        result = greet("José")
        assert result == "Hello, José!"


class TestFarewell:
    """Test cases for the farewell function."""
    
    def test_farewell_default(self):
        """Test farewell with default name."""
        result = farewell()
        assert result == "Goodbye, World!"
    
    def test_farewell_with_name(self):
        """Test farewell with custom name."""
        result = farewell("Python")
        assert result == "Goodbye, Python!"
    
    def test_farewell_with_empty_string(self):
        """Test farewell with empty string."""
        result = farewell("")
        assert result == "Goodbye, !"


class TestParameterTypes:
    """Test parameter type handling."""
    
    def test_greet_with_non_string_raises_error(self):
        """Test that non-string input raises appropriate error."""
        with pytest.raises(TypeError):
            greet(123)  # type: ignore
    
    def test_farewell_with_non_string_raises_error(self):
        """Test that non-string input raises appropriate error."""
        with pytest.raises(TypeError):
            farewell(123)  # type: ignore
