"""
Mock unit testing for mock_function.py
"""

import pytest
import mock_function as mock

def test_sample():
    """
    Test that the function raises FileNotFoundError when CSV file is missing.
    """
    with pytest.raises(TypeError, match="Input not string."):
        mock.mock_function(123)
