from abc import ABC

import requests


class AbstractAPIConnector(ABC):

    def __init__(self):
        pass


class HeadHunterAPI(AbstractAPIConnector):

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 20}
        self.__vacancies = []

    def __connect_API(self):
        response = requests.get(
            self.__url, headers=self.__headers, params=self.__params
        )
        if response.status_code == 200:
            return response
        else:
            print("Ошибка получения запроса API")
        pass

    def load_return_API(self, keyword):
        self.__params["text"] = keyword
        while self.__params.get("page") != 20:
            response = self.__connect_API()
            if response:
                vacancies = response.json()["items"]
                self.__vacancies.extend(vacancies)
                self.__params["page"] += 1
            else:
                break

        return self.__vacancies

    def vacancies_list(self):

        vacancies_list = []

        for vacancies in self.__vacancies:

            if vacancies["salary"] is None:
                salary = "Зарплата не указана"

            elif vacancies["salary"]["from"] is None:
                salary = "Зарплата не определена"

            elif vacancies["salary"]["to"] is None:
                salary = (
                    f'{vacancies["salary"]["from"]} .{vacancies["salary"]["currency"]}'
                )

            else:
                salary = (
                    f'{vacancies["salary"]["from"]} -'
                    f' {vacancies["salary"]["to"]} .{vacancies["salary"]["currency"]}'
                )

            vacancies_data = {
                "name": vacancies["name"],
                "salary": salary,
                "url": vacancies["alternate_url"],
                "responsibility": vacancies["snippet"]["responsibility"],
            }

            vacancies_list.append(vacancies_data)

        return vacancies_list

    def __str__(self):
        for i in self.vacancies_list():
            print(i)
            return
