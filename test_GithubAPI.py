import unittest
import requests
from GithubAPI import app  # Import the Flask app instance

class TestGitHubAPI(unittest.TestCase):
    def test_api_response(self):
        # Define the API endpoint and the expected status code
        endpoint = 'http://127.0.0.1:5000'  # Replace with your API endpoint
        expected_status_code = 200

        # Send a GET request to the API endpoint
        response = requests.get(endpoint)

        # Assert the response status code matches the expected code
        self.assertEqual(response.status_code, expected_status_code)

if __name__ == '__main__':
    unittest.main()
