#!/usr/bin/env python3
"""
testing module
"""
import unittest
from typing import Dict
from unittest.mock import Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo: Dict, key: str, expected: bool):
        """Testing method (has_license)"""
        client = GithubOrgClient('google')
        self.assertEqual(client.has_license(repo, key), expected)


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test"""
    @classmethod
    def setUpClass(cls):
        """Setup method"""
        routes = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in routes:
                get_mock = Mock()
                get_mock.json.return_value = routes[url]
                return get_mock

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self):
        """test public_repos method"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self):
        """test public_repos method with a license."""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls):
        """Deconstructor method"""
        cls.get_patcher.stop()
        pass
