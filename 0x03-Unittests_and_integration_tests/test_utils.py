#!/usr/bin/env python3
"""
testing module
"""
import unittest
from unittest.mock import Mock, patch
from parameterized import parameterized
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    """Test class"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test the nested mapp access"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",), 'a'),
        ({"a": 1}, ("a", "b"), 'b')
    ])
    def test_access_nested_map_exception(self, nested_map, path, key):
        """Test exception raising"""
        with self.assertRaises(KeyError) as exception:
            access_nested_map(nested_map, path)
            self.assertEqual(exception.msg, key)


class TestGetJson(unittest.TestCase):
    """Testing class"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, url, payload):
        """test the call"""
        with patch('requests.get') as mock_get:
            mock_json = Mock()
            mock_json.json.return_value = payload
            mock_get.return_value = mock_json
            res = get_json(url)
            self.assertEqual(res, payload)


class TestMemoize(unittest.TestCase):
    """Test caching"""
    def test_memoize(self):
        """Test function"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with patch.object(
            TestClass,
            'a_method',
        ) as mock_a_method:
            mock_a_method.return_value = lambda: 42
            test_class = TestClass()
            self.assertEqual(test_class.a_property(), 42)
            self.assertEqual(test_class.a_property(), 42)
            mock_a_method.assert_called_once()
