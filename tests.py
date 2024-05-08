import pytest
from unittest.mock import patch
from script import greet

@pytest.mark.parametrize("name, expected_output", [
    ('Alice', 'Hello, Alice!'),
    ('', 'Hello, !')
])
@patch('builtins.input')
def test_greet(mock_input, name, expected_output):
    mock_input.return_value = name
    assert greet(name) == expected_output
