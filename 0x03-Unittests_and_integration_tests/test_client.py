#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
from fixtures import org_payload, repos_payload,\
    expected_repos, apache2_repos


class TestGithubOrgClient(unittest.TestCase):
    """Unit tests for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""

        # Setup: define expected return value for the mock
        expected_result = {"login": org_name, "id": 123}
        mock_get_json.return_value = expected_result

        # Create an instance of GithubOrgClient with the provided org_name
        client = GithubOrgClient(org_name)

        # Call the org property and verify the result
        self.assertEqual(client.org, expected_result)

        # Check that get_json was called exactly once with the correct URL
        mock_get_json.assert_called_once_with(
            f"https://api.github.com/orgs/{org_name}")

    @patch('client.GithubOrgClient.org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test _public_repos_url property"""
        # Define the mocked payload with a known 'repos_url'
        mock_payload = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"
        }
        mock_org.return_value = mock_payload

        # Create a GithubOrgClient instance
        client = GithubOrgClient("test_org")

        # Access _public_repos_url and check that
        # it matches the repos_url in the mock payload
        self.assertEqual(client._public_repos_url, mock_payload["repos_url"])

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test public_repos method"""
        # Define the mocked payload returned by get_json
        mock_repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}},
            {"name": "repo3", "license": {"key": "gpl"}},
        ]
        mock_get_json.return_value = mock_repos_payload

        # Define the mocked URL for _public_repos_url
        mock_repos_url = "https://api.github.com/orgs/test_org/repos"

        with patch.object(
                GithubOrgClient, '_public_repos_url',
                new_callable=property) as mock_public_repos_url:
            mock_public_repos_url.return_value = mock_repos_url

            # Create a GithubOrgClient instance
            client = GithubOrgClient("test_org")

            # Call the public_repos method and
            # check if it matches the expected result
            expected_repos = ["repo1", "repo2", "repo3"]
            self.assertEqual(client.public_repos(), expected_repos)

            # Verify that _public_repos_url
            # and get_json were each called exactly once
            mock_public_repos_url.assert_called_once()
            mock_get_json.assert_called_once_with(mock_repos_url)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Additional test: no license field
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test GithubOrgClient.has_license method with different licenses"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)


@parameterized_class([
    {
        "org_payload": org_payload,
        "repos_payload": repos_payload,
        "expected_repos": expected_repos,
        "apache2_repos": apache2_repos}
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient.public_repos method"""

    @classmethod
    def setUpClass(cls):
        """Set up class-level mocks and fixtures"""
        cls.get_patcher = patch('requests.get')

        # Start the patcher and configure the side_effect
        cls.mock_get = cls.get_patcher.start()
        cls.mock_get.side_effect = cls.mocked_requests_get

    @classmethod
    def tearDownClass(cls):
        """Tear down class-level mocks"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """Side effect function to return
        different fixture data based on URL"""
        if "repos" in url:
            return MockResponse(repos_payload)
        return MockResponse(org_payload)

    def test_public_repos(self):
        """Test public_repos method with different licenses"""
        client = GithubOrgClient("some_org")

        # Test without license filter
        self.assertEqual(client.public_repos(), expected_repos)

        # Test with Apache 2.0 license filter
        self.assertEqual(
            client.public_repos(license="apache-2.0"), apache2_repos)

    def test_public_repos(self):
        """Test public_repos method without a license filter"""
        client = GithubOrgClient("some_org")
        self.assertEqual(client.public_repos(), expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method with license filter 'apache-2.0'"""
        client = GithubOrgClient("some_org")
        self.assertEqual(
            client.public_repos(license="apache-2.0"), apache2_repos)


class MockResponse:
    """Mock response object to simulate .json() for requests.get"""
    def __init__(self, json_data):
        self.json_data = json_data

    def json(self):
        return self.json_data


if __name__ == '__main__':
    unittest.main()
