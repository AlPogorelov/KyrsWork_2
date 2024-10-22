import unittest
from unittest.mock import patch, Mock
from src.hh_api import HeadHunterAPI

import src.hh_api
class TestHHApi(unittest.TestCase):

    @patch('requests.get')
    def test_connect_api_code_200(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_get.return_value = mock_response

        con_api = HeadHunterAPI()
        responce = con_api._HeadHunterAPI__connect_API()

        assert responce.status_code == 200

    @patch('requests.get')
    def test_connect_api_code_400(self, mock_get):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_get.return_value = mock_response

        con_api = HeadHunterAPI()
        responce = con_api._HeadHunterAPI__connect_API()

        assert responce.status_code == 400

    @patch('requests.get')
    def test_get_vacancies(self, mock_get):

        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "items": [{"id": 1, "name": "Vacancy 1"}, {"id": 2, "name": "Vacancy 2"}]
        }
        mock_get.return_value = mock_response

        con_api = HeadHunterAPI()
        responce = con_api.get_vacancies('python')

        assert responce == [{"id": 1, "name": "Vacancy 1"}, {"id": 2, "name": "Vacancy 2"}]


