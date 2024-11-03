#!/usr/bin/env python3
"""
testing module
"""
import unittest
from typing import Dict
from unittest.mock import Mock, PropertyMock, patch
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD


class TestGithubOrgClient(unittest.TestCase):
    """Testing class"""
    @parameterized.expand([
        ('google', {'status': 'alive'}),
        ('abc', {'status': 'alive'})
        ])
    @patch('client.get_json')
    def test_org(self, org: str, resp: Dict, mock_get: Mock):
        """Test org"""
        mock_get.return_value = resp
        client = GithubOrgClient(org)
        self.assertEqual(client.org, resp)

    def test_public_repos_url(self):
        """Test method"""
        resp = {
            "url": "https://api.github.com/orgs/google",
            "repos_url": "https://api.github.com/orgs/google/repos"
            }
        with patch.object(
            GithubOrgClient,
            'org',
            new_callable=PropertyMock
        ) as mock_org:
            client = GithubOrgClient('google')
            mock_org.return_value = resp
            self.assertEqual(client._public_repos_url, resp["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get: Mock):
        """Test method"""
        repos_url, repos_payload, repos_list, _ = TEST_PAYLOAD[0]
        mock_get.return_value = repos_payload
        client = GithubOrgClient('google')
        with patch.object(
            GithubOrgClient,
            '_public_repos_url',
            new_callable=PropertyMock
        ) as mock_public_repos:
            mock_public_repos.return_value = repos_url
            self.assertEqual(client.public_repos(), repos_list)
            mock_get.assert_called_once()
            mock_public_repos.assert_called_once()
