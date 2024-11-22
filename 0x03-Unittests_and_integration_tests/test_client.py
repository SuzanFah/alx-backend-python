#!/usr/bin/env python3
"""Test module for client"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient"""

    @parameterized.expand([
        ("google"),
        ("abc")
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns correct value"""
        test_client = GithubOrgClient(org_name)
        test_client.org()
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}"
        )

    def test_public_repos(self):
        """Test GithubOrgClient.public_repos method"""
        test_payload = {
            'repos_url': 'https://api.github.com/orgs/google/repos',
            'repos': [
                {
                    'id': 1,
                    'name': 'repo1'
                },
                {
                    'id': 2,
                    'name': 'repo2'
                }
            ]
        }

        expected_repos = ['repo1', 'repo2']

        with patch('client.GithubOrgClient.org',
                  new_callable=PropertyMock) as mock_org:
            mock_org.return_value = test_payload

            with patch('client.get_json') as mock_json:
                mock_json.return_value = test_payload['repos']

                client = GithubOrgClient('google')
                repos = client.public_repos()

                self.assertEqual(repos, expected_repos)
                mock_org.assert_called_once()
                mock_json.assert_called_once()