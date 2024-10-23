import json
import os.path
import unittest
from unittest.mock import patch, mock_open
from src.json_saver import JSONSaver
from src.vacancies import Vacancy





def test_save_to_file(file_name='./tests/test_vacancies.json'):
    full_file_name = os.path.abspath(file_name)
    saver = JSONSaver(full_file_name)
    saver.save_to_file(['test'])

    with open(full_file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)

    assert data == ['test']



def test_read_file_json(file_name='./tests/test_vac.json'):

    full_file_name = os.path.abspath(file_name)
    with open(full_file_name, 'r', encoding='utf-8') as f:
        data = json.load(f)

    assert data == ['test']


class TestJSONSaver(unittest.TestCase):

    @patch.object(JSONSaver, 'read_file_json')
    @patch.object(JSONSaver, 'save_to_file')
    def test_add_new_vacancy(self, mock_save_to_file, mock_read_file_json):

        mock_read_file_json.return_value = []

        saver = JSONSaver()

        vacancy = Vacancy('develop', 1000, 1500,'1', '2', '3')

        saver.add_vacancy(vacancy)

        expected_data = [vacancy.to_dict()]
        mock_save_to_file.assert_called_once_with(expected_data)

    @patch.object(JSONSaver, 'read_file_json')
    @patch.object(JSONSaver, 'save_to_file')
    def test_del_existing_vacancy(self, mock_save_to_file, mock_read_file_json):

        mock_read_file_json.return_value = [{"name": "develop", "salary_from": "1000", "salary_to": "1500", "url": "1",
        "requirement": "2", "responsebility": "3"}]

        saver = JSONSaver()

        vacancy = Vacancy('develop', 1000, 1500, '1', '2', '3')

        saver.del_vacancy(vacancy)

        mock_save_to_file.assert_called_once_with([])

    @patch.object(JSONSaver, 'add_vacancy')
    def test_add_multiple_vacancies(self, mock_add_vacancy):
        # Создаем экземпляр JSONSaver
        saver = JSONSaver()

        # Пример списка вакансий
        vacancies = [{"name": "develop", "salary_from": "1000", "salary_to": "1500", "url": "1",
        "requirement": "1", "responsebility": "1"}, {"name": "develop", "salary_from": "2000", "salary_to": "2500", "url": "2",
        "requirement": "2", "responsebility": "3"}]

        # Вызываем метод add_vacancies
        saver.add_vacancies(vacancies)

        # Проверяем, что метод add_vacancy был вызван столько раз, сколько вакансий в списке
        self.assertEqual(mock_add_vacancy.call_count, len(vacancies))

        # Проверяем, что add_vacancy был вызван с каждой вакансией
        for vacancy in vacancies:
            mock_add_vacancy.assert_any_call(vacancy)
