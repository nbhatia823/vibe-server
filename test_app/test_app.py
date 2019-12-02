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
    
    def testPositiveUserOperations(self):
        """Test that put, get, then delete works.
        """
        self.test_user_data = {
            "user_id": "1",
            "user_name": "test",
            "profile_pic_url": "none",
            "auth_token": "none"
        }
        response = self.client.put(path="/api/users", content_type='application/json',
        data=json.dumps(self.test_user_data))
        self.assertEqual(response.status_code, 204)

        response = self.client.get(path="/api/users/1")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, self.test_user_data)
        
        response = self.client.delete(path="/api/users/1")
        self.assertEqual(response.status_code, 204)

    def testNegativeGet(self):
        """Tests a failed GET
        """
        response = self.client.get(path="/api/users/2")
        self.assertEqual(response.status_code, 404)
    
    def testNegativePut(self):
        """Tests a failed PUT
        """
        response = self.client.put(path="/api/users")
        self.assertEquals(response.status_code, 400)
    
    def testNegativeDelete(self):
        """Tests a failed delete
        """
        response = self.client.delete(path="/api/users/2")
        self.assertEqual(response.status_code, 400)


class TestTrack(unittest.TestCase):
    """
    Tests the track API endpoints.
    """
    def setUp(self):
        self.app = app
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()
    
    def testGetTrack(self):
        response = self.client.get(path="/api/track/1LeItUMezKA1HdCHxYICed")
        self.assertEqual(response.status_code, 200)

    def testNegativeGetTrack(self):
        response = self.client.get(path="/api/track/xx")
        self.assertEqual(response.status_code, 404)

    def testPostAndGetAndDeleteTrack(self):
        track_data = {
            "track_id": "xy",
            "track_name": "test",
            "artist_name": "test",
            "album_art_url": "test",
            "sentiment_score": 1.0
        }
        response = self.client.post(path="/api/track", data=track_data)
        self.assertEqual(response.status_code, 201)
        response = self.client.get(path="/api/track/xy")
        self.assertEqual(response.status_code, 200)
        response = self.client.delete(path="/api/track/xy")
        self.assertEqual(response.status_code, 204)

    def testNegativePostTrack(self):
        response = self.client.post(path="/api/track/1")
        self.assertEqual(response.status_code, 400)
    
    def testNegativeDeleteTrack(self):
        response = self.client.delete(path="/api/track/xy")
        self.assertEqual(response.status_code, 400)

if __name__ == "__main__":
    print("Starting unit tests")
    unittest.main()
    print("Finished unit tests")