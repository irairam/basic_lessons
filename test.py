# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2б', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

from collections import Counter
from collections import defaultdict


# print(str(school[0]['students']))

def check_name_gender(name):
    gender = 'male' if is_male[name] == True else 'female'
    return gender

def count_genders(school_class):
    flattened_values = [check_name_gender(list_dict['first_name']) for list_dict in school_class['students']]
    counter = Counter(flattened_values)
    return counter

# group by
def group_by(school):
    res = {}
    for i, v in school:
        res[v] = [i] if v not in res.keys() else res[v] + [i]
    print(res)


# school_groupped_by = group_by(school)
# print(str(school_groupped_by))



# Counter(tok['Value'] for tok in school)