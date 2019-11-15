import json
import unittest
from flask import Flask

from app import app
from config import Config

class TestConfigComplete(unittest.TestCase):
    """
    This class ensures that the config files are populated with a nonempty
    string type to account for misconfiguration issues

    """
    def setUp(self):
        self.config = Config()
    def test_config_pairs(self):
        self.assertTrue(isinstance(self.config.HOST, str))
        self.assertTrue(isinstance(self.config.DATABASE, str))
        self.assertTrue(isinstance(self.config.USERNAME, str))
        self.assertTrue(isinstance(self.config.PASSWORD, str))
        self.assertTrue(isinstance(self.config.PORT, str))


class TestApp(unittest.TestCase):
    """
    This class contains all the unit tests for this Flask app.
    The tests generally consist of running sample requests against our
    endpoints and validating the response payloads and status codes.
    http://www.patricksoftwareblog.com/unit-testing-a-flask-application/
    """

    def setUp(self):
        """Do all the setup required before every test runs
        """
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_main_page(self):
        """A simple smoke test to check that the home page works
        """
        response = self.client.get(path="/")
        self.assertEqual(response.status_code, 200)

class TestSpotifyAPI(unittest.TestCase):
    """
    This class runs unit tests for the Spotify API calls
    """
    def setUp(self):
        self.spotify_helper = None

    def test_configured(self):
        self.assertIsNotNone(self.spotify_helper.client_secret)

if __name__ == "__main__":
    unittest.main()
