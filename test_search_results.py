import unittest
from flask import Flask, request
from app import search_results

class TestSearchResults(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.client = self.app.test_client()

    def test_search_results_valid_client_id(self):
        # Simulate a POST request with a valid client_id
        client_id = 1
        response = self.client.post('/search', data={'client_id': client_id})
        breakpoint()
        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the client data is present in the response
        self.assertIn(b'Client Data', response.data)
        self.assertIn(b'Matej Petrinovic', response.data)
        self.assertIn(b'mpetrinovic@mail.com', response.data)
        self.assertIn(b'012432134', response.data)

    def test_search_results_invalid_client_id(self):
        # Simulate a POST request with an invalid client_id
        client_id = 999
        response = self.client.post('/search', data={'client_id': client_id})

        # Check if the response status code is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # Check if the "Client not found" message is present in the response
        self.assertIn(b'Client not found', response.data)

if __name__ == '__main__':
    unittest.main()
