import json
import unittest
from app import app # TODO: this doesn't import for some reason?

class TestApp(unittest.TestCase):
    """
    This class contains all the unit tests for this Flask app.
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


if __name__ == "__main__":
    unittest.main()