from abc import ABC, abstractmethod

import requests


class AbstractHeadHunter(ABC):

    @abstractmethod
    def get_vacancies(self, *args):
        pass


class HeadHunterAPI(AbstractHeadHunter):

    def __init__(self):
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.vacancies = []

    def __connect_API(self):
        '''Модель подключения к API и обработка ошибок запроса'''
        try:
            response = requests.get(
                self.__url, headers=self.__headers, params=self.__params
            )
            if response.status_code != 200:

                print(f"Ошибка запроса API: {response.status_code}")

            return response

        except requests.exceptions.RequestException as e:
            # Обработка ошибок запроса
            print(f"Ошибка при выполнении запроса: {e}")
            return None

    def get_vacancies(self, keyword):
        '''В параметры API запроса добавляет клбчевое слово, и получает JSON ответ по ключевым параметрам запроса'''
        self.__params["text"] = keyword
        response = self.__connect_API()
        vacancie = response.json()["items"]
        return vacancie
