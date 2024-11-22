#!/usr/bin/env python3
"""Test module for client"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
import requests


@parameterized_class([
    {
        'org_payload': TEST_PAYLOAD[0][0],
        'repos_payload': TEST_PAYLOAD[0][1],
        'expected_repos': TEST_PAYLOAD[0][2],
        'apache2_repos': TEST_PAYLOAD[0][3],
    }
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up class fixtures"""
        cls.get_patcher = patch('requests.get')
        cls.mock_get = cls.get_patcher.start()

        def side_effect(url):
            """Side effect function for requests.get mock"""
            mock_response = requests.Response()
            
            if url.endswith('/orgs/google'):
                mock_response.json = lambda: cls.org_payload
            elif url.endswith('/orgs/google/repos'):
                mock_response.json = lambda: cls.repos_payload
            
            return mock_response

        cls.mock_get.side_effect = side_effect

    @classmethod
    def tearDownClass(cls):
        """Tear down class fixtures"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test for public_repos method"""
        client = GithubOrgClient('google')
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Integration test for public_repos with license argument"""
        client = GithubOrgClient('google')
        self.assertEqual(
            client.public_repos(license="apache-2.0"),
            self.apache2_repos
        )