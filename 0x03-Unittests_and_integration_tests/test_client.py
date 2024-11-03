#!/usr/bin/env python3
"""
testing module
"""
import unittest
from typing import Dict
from unittest.mock import Mock, patch
from parameterized import parameterized
from client import GithubOrgClient


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
