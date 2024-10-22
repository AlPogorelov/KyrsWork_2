
def filter_to_keyword(vacancies_list, key_word):
    filter_to = []
    for key in key_word:
        for vac in vacancies_list:
            if vac.requirement is not None:
                if key in vac.requirement.lower():
                    filter_to.append(vac)

    return filter_to


def sorted_salary(vacancies_list):
    '''Сортировка зарплаты по убыванию'''
    return sorted(vacancies_list, reverse=True)


def print_top_n(sorted_list, top_n):

    for vac in sorted_list[:top_n]:
        print(vac)
