import json
from abc import ABC

import requests




class AbstractHeadHunter(ABC):
    def connect_API(self):
        pass


class HeadHunterAPI(AbstractHeadHunter):

    def __init__(self):
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {'User-Agent': 'HH-User-Agent'}
        self.__params = {'text': '', 'page': 0, 'per_page': 20}
        self.vacancies = []

    def connect_API(self):
        response = requests.get(self.__url, headers=self.__headers, params=self.__params)
        if response == 200:
            print('Ошибка запроса API')

        return response

    def get_vacancies(self, keyword):
        self.__params['text'] = keyword
        response = self.connect_API()
        vacancie = response.json()['items']
        return vacancie

