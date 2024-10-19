def sorted_to_keyword(vacancies_list, key_word):
    """Соритровать словарь с вакансиями по ключевым словам в требовании вакансии"""

    def keyword_score(obj):
        score = 0
        for keyword in key_word:
            if keyword.lower() in obj.requirement.lower():
                score += 1
        return score

    return sorted(vacancies_list, key=keyword_score, reverse=True)


def print_top_n(sorted_list, top_n):
    for vac in sorted_list[:top_n]:
        vac.print_vac()
