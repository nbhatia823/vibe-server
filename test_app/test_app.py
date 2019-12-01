import json
import unittest
from flask import Flask

from app import app

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
    
class TestUsers(unittest.TestCase):
    """
    Tests the users endpoints.
    """
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def testPutUser(self):
        self.test_user_data = {
            "user_id": "1",
            "user_name": "test",
            "profile_pic_url": "none",
            "auth_token": "none"
        }
        response = self.client.put(path="/api/users", data=self.test_user_data)
        self.assertEqual(response.status_code, 204)

class TestTrack(unittest.TestCase):
    """
    Tests the track API endpoints.
    """
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def testGetTrack(self):
        response = self.client.get("/api/track/1LeItUMezKA1HdCHxYICed")
        self.assertEqual(response.status_code, 200)

# class TestSpotifyAPI(unittest.TestCase):
#     """
#     This class runs unit tests for the Spotify API calls
#     """
#     def setUp(self):
#         pass
    
#     def test_configured(self):
#         pass

if __name__ == "__main__":
    print("Starting unit tests")
    unittest.main()
    print("Finished unit tests")