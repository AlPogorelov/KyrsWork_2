import json
import os
from abc import ABC, abstractmethod
from json import JSONDecodeError


class Abstractclass(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy):
        pass

    @abstractmethod
    def del_vacancy(self, vacancy):
        pass

    @abstractmethod
    def add_vacancies(self, vacancy):
        pass

    @abstractmethod
    def clear_json_file(self):
        pass

    @abstractmethod
    def read_file_json(self):
        pass


class JSONSaver(Abstractclass):

    def clear_json_file(self):

        with open(self.file_path, "w", encoding="utf-8"):
            pass

    def __init__(self, file_name="./data/vacancies_json.json"):
        """Инициализатор класса JSONSaver"""
        full_file_name = os.path.abspath(file_name)
        self.file_path = full_file_name

    def save_to_file(self, vacancies=[]):
        '''Метод сохранение данный в JSON файл'''

        with open(self.file_path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def read_file_json(self):
        '''Метод чтение JSON файла'''
        try:
            with open(self.file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                if data is None:
                    data = []
        except FileNotFoundError:
            data = []

        except JSONDecodeError:
            data = []

        return data

    def add_vacancy(self, vacancy):
        '''Добавление единичной вакансии в JSON файл'''

        data = self.read_file_json()

        if vacancy.url not in [dat.get("url") for dat in data]:

            data.append(vacancy.to_dict())

            self.save_to_file(data)

    def del_vacancy(self, vacancy):
        '''Удаление единичной вакансии из JSON файла'''
        data = self.read_file_json()

        for index, vac in enumerate(data):
            if vac["url"] == vacancy.url:
                data.pop(index)

                self.save_to_file(data)

    def add_vacancies(self, vacancies: [list[dict]]):
        '''Добавление списка вакансии в JSON файл'''
        for i in vacancies:
            self.add_vacancy(i)
