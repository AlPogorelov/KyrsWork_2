import pytest

from src.vacancies import Vacancy


@pytest.fixture
def first_vacancies():
    return Vacancy(
        name='python',
        salary_from=1000,
        salary_to=1500,
        url='url',
        requirement='requirement',
        responsibility='responsibility'
    )

@pytest.fixture
def clone_first_vacancies():
    return Vacancy(
        name='python',
        salary_from=1000,
        salary_to=1500,
        url='url',
        requirement='requirement',
        responsibility='responsibility'
    )


@pytest.fixture
def second_vacancies():
    return Vacancy(
        name='python',
        salary_from=2000,
        salary_to=2500,
        url='url',
        requirement='requirement1',
        responsibility='responsibility1'
    )


@pytest.fixture
def json_vacancies():
    return [{'name': '1',
            'salary': {'from': 1, 'to': 1, 'currency': 'RUR', 'gross': False},
             'url': 'https://api.hh.ru/vacancies/108620069?host=hh.ru', 'alternate_url': '1',
             'snippet': {'requirement': '1', 'responsibility': '1'}}
            ]