#!/usr/bin/env python3
import unittest
from unittest.mock import patch, MagicMock
from parameterized import parameterized, parameterized_class
from client import GithubOrgClient
import fixtures


@parameterized_class([
    {
        "org_payload": fixtures.org_payload,
        "repos_payload": fixtures.repos_payload,
        "expected_repos": fixtures.expected_repos,
        "apache2_repos": fixtures.apache2_repos}
])
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

    @patch.object(GithubOrgClient, 'org', new_callable=property)
    def test_public_repos_url(self, mock_org):
        """Test GithubOrgClient._public_repos_url"""

        # Set up the mock return value for org to include a known repos_url
        mock_org.return_value = {
            "repos_url": "https://api.github.com/orgs/test_org/repos"}

        # Initialize the client
        client = GithubOrgClient("test_org")

        # Test the _public_repos_url property
        self.assertEqual(
            client._public_repos_url,
            "https://api.github.com/orgs/test_org/repos")

        # Check if the org property was accessed once
        mock_org.assert_called_once()

    @patch('client.get_json')
    @patch.object(GithubOrgClient, '_public_repos_url', new_callable=property)
    def test_public_repos(self, mock_repos_url, mock_get_json):
        """Test GithubOrgClient.public_repos method"""

        # Mock URL and payload for testing
        mock_repos_url.return_value =\
            "https://api.github.com/orgs/test_org/repos"
        mock_get_json.return_value = [
            {"name": "repo1"},
            {"name": "repo2"},
            {"name": "repo3"},
        ]

        # Initialize the client
        client = GithubOrgClient("test_org")

        # Expected list of repository names
        expected_repos = ["repo1", "repo2", "repo3"]

        # Call public_repos and verify the result
        self.assertEqual(client.public_repos(), expected_repos)

        # Check if _public_repos_url and get_json were each called once
        mock_repos_url.assert_called_once()
        mock_get_json.assert_called_once_with(mock_repos_url.return_value)

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),  # Additional test: no license field
    ])
    def test_has_license(self, repo, license_key, expected_result):
        """Test GithubOrgClient.has_license method with different licenses"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected_result)

    @classmethod
    def setUpClass(cls):
        """Set up class method for integration tests"""
        # Patch requests.get
        cls.get_patcher = patch(
            'requests.get', side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class method"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """Mocked requests.get to return
        different JSON payloads based on the URL"""
        mock_response = MagicMock()
        if url == GithubOrgClient.ORG_URL.format(org="test_org"):
            mock_response.json.return_value = fixtures.org_payload
        elif url == fixtures.org_payload["repos_url"]:
            mock_response.json.return_value = fixtures.repos_payload
        return mock_response

    def test_public_repos(self):
        """Test public_repos method with mocked data"""
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method filtering by license with mocked data"""
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos"""

    @classmethod
    def setUpClass(cls):
        """Set up class method for integration tests"""
        # Patch requests.get
        cls.get_patcher = patch(
            'requests.get', side_effect=cls.mocked_requests_get)
        cls.mock_get = cls.get_patcher.start()

    @classmethod
    def tearDownClass(cls):
        """Tear down class method"""
        cls.get_patcher.stop()

    @staticmethod
    def mocked_requests_get(url):
        """Mocked requests.get to return
        different JSON payloads based on the URL"""
        mock_response = MagicMock()
        if url == GithubOrgClient.ORG_URL.format(org="test_org"):
            mock_response.json.return_value = fixtures.org_payload
        elif url == fixtures.org_payload["repos_url"]:
            mock_response.json.return_value = fixtures.repos_payload
        return mock_response

    def test_public_repos(self):
        """Test public_repos method with mocked data"""
        client = GithubOrgClient("test_org")
        repos = client.public_repos()
        self.assertEqual(repos, self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method filtering by license with mocked data"""
        client = GithubOrgClient("test_org")
        repos = client.public_repos(license="apache-2.0")
        self.assertEqual(repos, self.apache2_repos)


if __name__ == '__main__':
    unittest.main()
