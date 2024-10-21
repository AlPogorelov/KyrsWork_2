from src.hh_api import HeadHunterAPI
from src.json_saver import JSONSaver
from src.utils_def import print_top_n, filter_to_keyword, sorted_salary
from src.vacancies import Vacancy


def user_interaction():

    hh_api = HeadHunterAPI()

    json_saver = JSONSaver()

    json_saver.clear_json_file()

    platforms = ["HeadHunter"]

    search_query = input("Введите поисковый запрос: ")

    top_n = int(input("Введите количество вакансий для вывода в топ N: "))

    filter_words = input(
        "Введите ключевые слова для сортировки вакансий в требованиях: "
    ).split()

    hh_vacancies = hh_api.get_vacancies(search_query)

    vacancies_list = Vacancy.cast_to_object_list(hh_vacancies)

    if filter_words != []:
        vacancies_list = filter_to_keyword(vacancies_list, filter_words)

    else:
        print('Значит соритровать не будем')

    sort_salary = str(input('Сортировать вакансии по зарплате? '))

    if sort_salary.lower() in ["lf", "да", "yes"]:

        vacancies_list = sorted_salary(vacancies_list)

    print_vac = str(input('Распечатать список вакансий? '))

    if print_vac.lower() in ["lf", "да", "yes"]:
        print_top_n(vacancies_list, top_n)

    saver = str(input("Сохранить результат в JSON?"))

    if saver.lower() in ["lf", "да", "yes"]:
        json_saver.add_vacancies(vacancies_list[:top_n])

        if json_saver.read_file_json() == []:
            print("По данным притериям вакансии не найдены")
