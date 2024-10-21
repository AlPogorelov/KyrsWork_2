class Vacancy:
    __slots__ = ("name", 'salary_from', 'salary_to', "url", "requirement", "responsibility")

    def __init__(self, name, salary_from, salary_to, url, requirement, responsibility):
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility

    @classmethod
    def cast_to_object_list(cls, json_vacancies):
        '''Метод получает json данный и по этим данным создаетс писок эезмеплячров класса Vacancy'''

        vacancies_list = []
        for vacancy in json_vacancies:
            name = vacancy.get("name")
            url = vacancy.get("alternate_url")
            requirement = vacancy.get("snippet").get("requirement")
            responsibility = vacancy.get("snippet").get("responsibility")
            salary_from, salary_to = cls.validation_salary(vacancy)

            vac = {
                "name": name,
                "url": url,
                "requirement": requirement,
                "responsibility": responsibility,
                "salary_from": salary_from,
                'salary_to': salary_to
            }

            vacancies_list.append(Vacancy(**vac))

        return vacancies_list

    @staticmethod
    def validation_salary(vacancy):
        if vacancy.get("salary"):
            if vacancy.get("salary").get("from"):
                salary_from = vacancy['salary']['from']
            else:
                salary_from = 0
            if vacancy.get("salary").get("to"):
                salary_to = vacancy['salary']['to']
            else:
                salary_to = 0
        else:
            salary_from = 0
            salary_to = 0
        return salary_from, salary_to

    def to_dict(self):
        '''Метод подгатавливает экземпляк вокансии в словарь для работы'''
        return {
            "name": self.name,
            "url": self.url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "responsibility": self.responsibility,
            "requirement": self.requirement
        }

    def __str__(self):
        return (f'{self.name}, Зарплата: {self.salary_from} - {self.salary_to},'
                f' Требования: {self.responsibility}, Требования: {self.requirement}')

    def __eq__(self, other) -> bool:
        """Метод сравнения вакансий (=)"""
        return self.salary_from == other.salary_from

    def __lt__(self, other) -> bool:
        """Метод сравнения вакансий (<)"""
        return self.salary_from < other.salary_from

    def __le__(self, other) -> bool:
        """Метод сравнения вакансий (<=)"""
        return self.salary_from <= other.salary_from


