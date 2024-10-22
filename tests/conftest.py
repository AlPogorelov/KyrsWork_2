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

@pytest.fixture
def vacancies_list():
    return [Vacancy('develop1', 1000,
                    1500, 'url1','Требования ЧАТБОТ', 'responsibility1'),
            Vacancy('develop2', 2000,
                    2500, 'url2','Требования ЧАТ', 'responsibility2'),
            Vacancy('develop3', 3000,
                    3500, 'url3','Требования чай', 'responsibility3')
    ]

