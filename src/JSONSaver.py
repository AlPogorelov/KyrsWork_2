import os
from abc import ABC, abstractmethod
import json
from json import JSONDecodeError


class Abstractclass(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass


    @abstractmethod
    def del_vacancy(self, vacancy):
        pass


class JSONSaver(Abstractclass):

    def clear_json_file(self):
        data = []
        with open('./data/vacancies_json.json', 'w', encoding='utf-8') as f:
            pass



    def __init__(self, file_name='./data/vacancies_json.json'):
        """Инициализатор класса JSONSaver"""
        full_file_name = os.path.abspath(file_name)
        self.file_path = full_file_name


    @staticmethod
    def save_to_file(vacancies=[]):

        with open('./data/vacancies_json.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    @staticmethod
    def save_to_reserve_file(vacancies):

        with open('./data/reserve_vacancies_json.json', 'w', encoding='utf-8') as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def read_file_json(self):
        try:
            with open(self.file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if data is None:
                    data = []
        except FileNotFoundError:
            data = []

        except JSONDecodeError:
            data = []

        return data

    def add_vacancy(self, vacancy):

        data = self.read_file_json()

        self.save_to_reserve_file(data)

        if vacancy.url not in [dat.get('url') for dat in data]:

            data.append(vacancy.to_dict())

            self.save_to_file(data)

    def del_vacancy(self, vacancy):
        data = self.read_file_json()

        self.save_to_reserve_file(data)

        for index, vac in enumerate(data):
            if vac["url"] == vacancy.url:
                data.pop(index)

                self.save_to_file(data)

    def add_vacancies(self, vacancies: [list[dict]]):
        data = self.read_file_json()

        self.save_to_reserve_file(data)

        for i in vacancies:
            self.add_vacancy(i)
        #
        # self.save_to_file(data)

