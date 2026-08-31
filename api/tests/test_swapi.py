import requests
from django.test import TestCase
from unittest.mock import patch

from api.clients.swapi_client import fetch_swapi_planets


class SwapiClientTest(TestCase):

    @patch('api.clients.swapi_client.requests.get')
    def test_fetch_planets_returns_data_on_success(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"name": "Tatooine"}]

        result = fetch_swapi_planets()

        self.assertEqual(result, [{"name": "Tatooine"}])


    @patch('api.clients.swapi_client.requests.get')
    def test_fetch_planets_returns_none_on_failure(self, mock_get):
        mock_get.side_effect = requests.exceptions.RequestException

        result = fetch_swapi_planets()

        self.assertIsNone(result)
