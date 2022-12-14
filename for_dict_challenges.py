# Задание 1
# Дан список учеников, нужно посчитать количество повторений каждого имени ученика
# Пример вывода:
# Вася: 1
# Маша: 2
# Петя: 2

students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Петя'},
]
from collections import Counter
flattened_values = [list_dict['first_name'] for list_dict in students]
counter = Counter(flattened_values)
for key, value in counter.items():
    print(key, value)


# Задание 2
# Дан список учеников, нужно вывести самое часто повторящееся имя
# Пример вывода:
# Самое частое имя среди учеников: Маша
students = [
    {'first_name': 'Вася'},
    {'first_name': 'Петя'},
    {'first_name': 'Маша'},
    {'first_name': 'Маша'},
    {'first_name': 'Оля'},
]
from collections import Counter
flattened_values = [list_dict['first_name'] for list_dict in students]
counter = Counter(flattened_values)
max_often_name = max(counter, key=counter.get)
print(f'Самое популярное имя: {max_often_name}')


# Задание 3
# Есть список учеников в нескольких классах, нужно вывести самое частое имя в каждом классе.
# Пример вывода:
# Самое частое имя в классе 1: Вася
# Самое частое имя в классе 2: Маша

school_students = [
    [  # это – первый класс
        {'first_name': 'Вася'},
        {'first_name': 'Вася'},
    ],
    [  # это – второй класс
        {'first_name': 'Маша'},
        {'first_name': 'Маша'},
        {'first_name': 'Оля'},
    ],[  # это – третий класс
        {'first_name': 'Женя'},
        {'first_name': 'Петя'},
        {'first_name': 'Женя'},
        {'first_name': 'Саша'},
    ],
]
for school_class in school_students:
    flattened_values = [list_dict['first_name'] for list_dict in school_class]
    counter = Counter(flattened_values)
    max_often_name = max(counter, key=counter.get)
    print('Самое частое имя в классе {} : {}'.format(str(school_students.index(school_class) + 1 ), max_often_name))


# Задание 4
# Для каждого класса нужно вывести количество девочек и мальчиков в нём.
# Пример вывода:
# Класс 2a: девочки 2, мальчики 0 
# Класс 2б: девочки 0, мальчики 2

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2с', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}
from collections import Counter

def check_name_gender(name):
    gender = 'male' if is_male[name] == True else 'female'
    return gender

def count_genders(school):
    for school_class in school:
        flattened_values = [check_name_gender(list_dict['first_name']) for list_dict in school_class['students']]
        counter = Counter(flattened_values)
        print('В классе {}: девочек {}, мальчиков {}'.format(school_class['class'],counter['female'],counter['male']))

count_genders(school)


# Задание 5
# По информации о учениках разных классов нужно найти класс, в котором больше всего девочек и больше всего мальчиков
# Пример вывода:
# Больше всего мальчиков в классе 3c
# Больше всего девочек в классе 2a

school = [
    {'class': '2a', 'students': [{'first_name': 'Маша'}, {'first_name': 'Оля'}]},
    {'class': '2б', 'students': [{'first_name': 'Олег'}, {'first_name': 'Миша'}]},
    {'class': '2с', 'students': [{'first_name': 'Даша'}, {'first_name': 'Олег'}, {'first_name': 'Маша'}]},
]
is_male = {
    'Олег': True,
    'Маша': False,
    'Оля': False,
    'Миша': True,
    'Даша': False,
}

from collections import Counter
from operator import itemgetter

def check_name_gender(name):
    gender = 'male' if is_male[name] == True else 'female'
    return gender

def count_genders(school):
    ls_dict = []
    for school_class in school:
        flattened_values = [check_name_gender(list_dict['first_name']) for list_dict in school_class['students']]
        counter = Counter(flattened_values)
        ds = {'class':school_class['class'], 'f':counter['female'], 'm':counter['male']}
        ls_dict.append(ds)

    newlist = sorted(ls_dict, key=itemgetter('f'), reverse=True)
    print('Больше всего девочек в классе: ',newlist[0]['class'])
    newlist = sorted(ls_dict, key=itemgetter('m'), reverse=True)
    print('Больше всего мальчиков в классе: ',newlist[0]['class'])

count_genders(school)

