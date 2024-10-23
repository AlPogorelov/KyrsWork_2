from src.utils_def import filter_to_keyword, sorted_salary
from src.vacancies import Vacancy


def test_filter_to_keyword(vacancies_list):
    result = filter_to_keyword(vacancies_list, ['чай', 'бот'])

    assert len(result) == 2
    assert result[0].name == 'develop3'
    assert result[0].url == 'url3'
    assert result[0].requirement == 'Требования чай'
    assert result[1].name == 'develop1'
    assert result[1].url == 'url1'


def test_sorted_salary(vacancies_list):
    result = sorted_salary(vacancies_list)
    assert result[0].name == 'develop3'
    assert result[0].url == 'url3'
    assert result[0].salary_from == 3000
    assert result[2].name == 'develop1'
    assert result[2].url == 'url1'
    assert result[2].salary_from == 1000
