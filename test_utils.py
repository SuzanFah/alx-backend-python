#!/usr/bin/env python3
"""Test module for utils.get_json function"""
import unittest
from unittest.mock import patch, Mock
from utils import get_json
from parameterized import parameterized


class TestGetJson(unittest.TestCase):
    """Test class for get_json function"""
    
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Test that utils.get_json returns expected result"""
        # Create mock response with json method returning test_payload
        mock_response = Mock()
        mock_response.json.return_value = test_payload
        
        # Patch requests.get to return our mock response
        with patch('requests.get') as mock_get:
            mock_get.return_value = mock_response
            
            # Call the function with test_url
            result = get_json(test_url)
            
            # Assert requests.get was called once with test_url
            mock_get.assert_called_once_with(test_url)
            
            # Assert the result equals test_payload
            self.assertEqual(result, test_payload)
