from collections import defaultdict
import csv
from copy import deepcopy

menu = '''
1. Вывести все отделы
2. Вывести сводный отчёт по отделам
3. Сохранить сводный отчёт в виде csv
0. Выход
'''


def my_menu():
    '''
    Вывод консольного меню
    '''
    is_logged = False
    reader = open_file('C:/Julia/AAA/HWsample.csv')
    while True:
        print(menu)
        inp = input()
        if inp == '1':
            dep = all_departments(reader)
            print(*dep)
        elif inp == '2':
            statistics = report(reader)
            data = from_dict_to_list(statistics)
            print(*data[0].keys(), sep=' | ')
            for line in data:
                print(*line.values(), sep='         ')
                is_logged = True
        elif inp == '3':
            if is_logged:
                statistics = report(reader)
                data = from_dict_to_list(statistics)
                record(data)
                print('Отчёт записан!')
            else:
                print('Сформируйте сначала отчёт')
        elif inp == '0':
            print('Bye')
            break
        else:
            print('Значение введено неверно!')


def all_departments(reader: list) -> set:
    """
    Считывание уникальных отделов из файла
    reader: список со всеми значениями файла csv
    """
    set_depart = set()
    for line in reader[1:]:
        departments = line[2].split('->')
        set_depart.add(departments[0])
    return set_depart


def report(reader: list) -> dict:
    """
    Составление статистики по отделам
    reader: список со всеми значениями файла csv
    """
    dictionary = defaultdict(lambda: [])
    for line in reader[1:]:
        departments = line[2].split('->')
        dictionary[departments[0]].append(int(line[4]))
    statistics = defaultdict(lambda: {})
    for key in dictionary:
        statistics[key] = {'Quantity': len(dictionary[key]),
                           'Max salary': max(dictionary[key]),
                           'Min salary': min(dictionary[key]),
                           'Average salary':
                               int(sum(dictionary[key])/len(dictionary[key]))}
    return statistics


def open_file(path: str) -> list:
    """
    Открытие файла и сохрание данных списком
    path: директория, в котором находится файл csv
    """
    with open(path) as f:
        reader = list(csv.reader
                      (f, delimiter=';', lineterminator='\n'))[:-1]
    return reader


def from_dict_to_list(stat_dict: dict) -> list:
    """
    Распаковка вложенного словаря, добавление отдела в словарь,
    преобразование словаря в список
    stat_dict: словарь с вложенным словарём со статистикой по отделам
    """
    listing = []
    for key, value in stat_dict.items():
        new_dict = deepcopy(value)
        new_dict['Department'] = key
        listing.append(new_dict)
    return listing


def record(data: list) -> None:
    """
    Запись сводного отчёта в файл
    data: список сформированной статистики по отделам
    """
    with open('C:/Julia/AAA/Result.csv', 'w',
              encoding='utf-8', newline='') as file:
        writer = csv.DictWriter(
            file, fieldnames=['Department', 'Quantity',
                              'Max salary', 'Min salary',
                              'Average salary'],
            quoting=csv.QUOTE_NONNUMERIC)
        writer.writeheader()
        for d in data:
            writer.writerow(d)


if __name__ == '__main__':
    my_menu()
