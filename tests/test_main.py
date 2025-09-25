"""
Tests for the command-line interface.
"""

import pytest
from unittest.mock import patch
import sys
from io import StringIO

from hello_world.main import main


class TestMain:
    """Test cases for the main CLI function."""
    
    def test_main_default_greeting(self):
        """Test main with default arguments."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main([])
            assert result == 0
            assert mock_stdout.getvalue().strip() == "Hello, World!"
    
    def test_main_with_name(self):
        """Test main with custom name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main(["Python"])
            assert result == 0
            assert mock_stdout.getvalue().strip() == "Hello, Python!"
    
    def test_main_farewell_default(self):
        """Test main with farewell flag."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main(["--farewell"])
            assert result == 0
            assert mock_stdout.getvalue().strip() == "Goodbye, World!"
    
    def test_main_farewell_with_name(self):
        """Test main with farewell flag and custom name."""
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            result = main(["--farewell", "Python"])
            assert result == 0
            assert mock_stdout.getvalue().strip() == "Goodbye, Python!"
    
    def test_main_help(self):
        """Test main with help flag."""
        with pytest.raises(SystemExit) as excinfo:
            main(["--help"])
        assert excinfo.value.code == 0
    
    def test_main_version(self):
        """Test main with version flag."""
        with pytest.raises(SystemExit) as excinfo:
            main(["--version"])
        assert excinfo.value.code == 0
    
    def test_main_invalid_arguments(self):
        """Test main with invalid arguments."""
        with pytest.raises(SystemExit) as excinfo:
            main(["--invalid-flag"])
        assert excinfo.value.code != 0
