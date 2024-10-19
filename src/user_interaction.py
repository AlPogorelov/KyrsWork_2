from src.JSONSaver import JSONSaver
from src.hh_api import HeadHunterAPI
from src.utils_def import sorted_to_keyword, print_top_n
from src.vacancies import Vacancy


def user_interaction():

    hh_api = HeadHunterAPI()

    json_saver = JSONSaver()

    json_saver.clear_json_file()

    platforms = ["HeadHunter"]

    search_query = input("Введите поисковый запрос: ")

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    filter_words = input("Введите ключевые слова для фильтрации вакансий по требованиям: ").split()

    hh_vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    sorted_vac = sorted_to_keyword(vacancies_list, filter_words)

    print_top_n(sorted_vac, top_n)

    saver = str(input('Сохранить результат в JSON?'))

    if saver.lower() in ['lf', 'да', 'yes']:
        json_saver.add_vacancies(sorted_vac[:top_n])









