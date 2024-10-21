from src.vacancies import Vacancy


def test_vacancies_init(first_vacancies):
    assert first_vacancies.name == 'python'
    assert first_vacancies.salary_from == 1000
    assert first_vacancies.salary_to == 1500
    assert first_vacancies.url == 'url'
    assert first_vacancies.requirement == 'requirement'
    assert first_vacancies.responsibility == 'responsibility'


def test_cast_to_object_list(json_vacancies):
    result = Vacancy.cast_to_object_list(json_vacancies)
    assert len(result) == 1
    assert result[0].name == '1'
    assert result[0].salary_from == 1
    assert result[0].salary_to == 1
    assert result[0].url == '1'
    assert result[0].requirement == '1'
    assert result[0].responsibility == '1'


def test_to_dict(first_vacancies):
    to_dict = first_vacancies.to_dict()
    assert type(to_dict) is dict
    assert to_dict['name'] == 'python'
    assert to_dict['salary_from'] == 1000
    assert to_dict['salary_to'] == 1500
    assert to_dict['url'] == 'url'
    assert to_dict['requirement'] == 'requirement'
    assert to_dict['responsibility'] == 'responsibility'


def test_comparison_vacancies(first_vacancies, second_vacancies, clone_first_vacancies,):
    assert first_vacancies <= second_vacancies
    assert first_vacancies == clone_first_vacancies
    assert second_vacancies != clone_first_vacancies
    assert second_vacancies >= clone_first_vacancies

