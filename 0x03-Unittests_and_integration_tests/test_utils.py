#!/usr/bin/env python3
""" Unit tests for utils.access_nested_map """
import unittest
from parameterized import parameterized
from unittest.mock import patch, Mock
from utils import access_nested_map, get_json
from utils import memoize


class TestAccessNestedMap(unittest.TestCase):
    """ Test class for access_nested_map function """

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """ Test access_nested_map returns expected output """
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), "a"),
        ({"a": 1}, ("a", "b"), "b")
    ])
    def test_access_nested_map_exception(
            self, nested_map, path, expected_exception_message):
        """Test access_nested_map raises KeyError with expected message"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception),
                         f"'{expected_exception_message}'")


class TestGetJson(unittest.TestCase):
    """Unit tests for get_json function in utils module"""

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """Test get_json returns expected result with mocked requests.get"""
        # Configure the mock to return a response with a custom json method
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        mock_get.return_value = mock_response

        # Call get_json and verify the output
        result = get_json(test_url)
        self.assertEqual(result, test_payload)

        # Verify requests.get was called exactly once with test_url
        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """Unit tests for the memoize decorator"""

    def test_memoize(self):
        """Test memoize caches the result of a method"""

        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()

        # Create an instance of TestClass
        test_instance = TestClass()

        # Patch a_method to monitor its calls
        with patch.object(
                test_instance, 'a_method', return_value=42) as mock_method:
            # Access a_property twice
            result1 = test_instance.a_property
            result2 = test_instance.a_property

            # Verify the results are as expected
            self.assertEqual(result1, 42)
            self.assertEqual(result2, 42)

            # Ensure a_method was only called once
            mock_method.assert_called_once()


if __name__ == '__main__':
    unittest.main()
