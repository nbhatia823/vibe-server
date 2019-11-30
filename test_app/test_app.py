import json
import unittest
from flask import Flask

import sys
import os

sys.path.append(os.getcwd() + '/..')
#hacky way to allow app import for unit testing
from app import app

class TestApp(unittest.TestCase):
    """
    This class contains all the unit tests for this Flask app.
    The tests generally consist of running sample requests against our
    endpoints and validating the response payloads and status codes.

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
        from config import Config

        self.config = Config()


    def test_configured(self):
        self.assertIsNotNone(self.config.HOST)
        self.assertIsNotNone(self.config.DATABASE)
        self.assertIsNotNone(self.config.PASSWORD)
        self.assertIsNotNone(self.config.PORT)
        self.assertIsNotNone(self.config.SECRET_KEY)
        self.assertIsNotNone(self.config.SPOTIFY_CLIENT_ID)
        self.assertIsNotNone(self.config.SPOTIFY_CLIENT_SECRET)

        self.assertIsNotNone(self.config.SPOTIFY_AUTH_TOKEN)
        self.assertIsNotNone(self.config.SPOTIFY_REQ_HEADERS)
        self.assertIsNotNone(self.config.SPOTIFY_ACCOUNT_URL)
        self.assertIsNotNone(self.config.SPOTIFY_API_URL)
        


if __name__ == "__main__":
    unittest.main()
