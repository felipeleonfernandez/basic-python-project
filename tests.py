import unittest
from unittest.mock import patch
from your_module import greet

class TestGreetFunction(unittest.TestCase):
    @patch('builtins.input', return_value='Alice')
    def test_greet_with_name(self, mock_input):
        expected_output = "Hello, Alice!"
        self.assertEqual(greet('Alice'), expected_output)

    @patch('builtins.input', return_value='')
    def test_greet_without_name(self, mock_input):
        expected_output = "Hello, !"
        self.assertEqual(greet(''), expected_output)

if __name__ == '__main__':
    unittest.main()
