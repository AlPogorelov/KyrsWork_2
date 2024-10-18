class Vacancy:
    __slots__ = ('name', 'salary', 'url', 'requirement', 'responsibility')

    def __init__(self, name, salary, url, requirement, responsibility):
        self.name = name
        self.salary = salary
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility


    @classmethod
    def cast_to_object_list(cls, json_vacancies):
        vacancies_list = []
        for vacancy in json_vacancies:
            name = vacancy.get("name")
            url = vacancy.get("alternate_url")
            requirement = vacancy.get("snippet").get("requirement")
            responsibility = vacancy.get("snippet").get("responsibility")
            if vacancy.get("salary"):

                if vacancy.get("salary").get("from"):

                    if vacancy.get("salary").get("to"):

                        salary_get = (f'{vacancy.get("salary").get("from")} -'
                                      f' {vacancy.get("salary").get("to")} .{vacancy.get("salary").get("currency")}')

                    else:
                        salary_get = f'{vacancy.get("salary").get("from")} .{vacancy.get("salary").get("currency")}'
            else:
                salary_get = 0

            salary = salary_get

            vac = {
                "name": name,
                "url": url,
                "requirement": requirement,
                "responsibility": responsibility,
                "salary": salary
            }

            vacancies_list.append(Vacancy(**vac))

        return vacancies_list

    def to_dict(self):
        return {
            'name': self.name,
            'url': self.url,
            'salary': self.salary,
            'responsibility': self.responsibility,
            'requirement': self.requirement
        }

    def print_vac(self):
        print({
            'name': self.name,
            'url': self.url,
            'salary': self.salary,
            'responsibility': self.responsibility,
            'requirement': self.requirement
        })


    def __eq__(self, other) -> bool:
        """Метод сравнения вакансий (=)"""
        return self.salary == other.salary

    def __lt__(self, other) -> bool:
        """Метод сравнения вакансий (<)"""
        return self.salary < other.salary

    def __le__(self, other) -> bool:
        """Метод сравнения вакансий (<=)"""
        return self.salary <= other.salary
