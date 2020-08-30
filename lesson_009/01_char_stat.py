# -*- coding: utf-8 -*-
import zipfile
# Подсчитать статистику по буквам в романе Война и Мир.
# Входные параметры: файл для сканирования
# Статистику считать только для букв алфавита (см функцию .isalpha() для строк)
#
# Вывести на консоль упорядоченную статистику в виде
# +---------+----------+
# |  буква  | частота  |
# +---------+----------+  alt + T = †
# |    А    |   77777  |
# |    Б    |   55555  |
# |   ...   |   .....  |
# |    a    |   33333  |
# |    б    |   11111  |
# |   ...   |   .....  |
# +---------+----------+
# |  итого  | 9999999  |
# +---------+----------+
#
# Упорядочивание по частоте - по убыванию. Ширину таблицы подберите по своему вкусу
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import zipfile
import operator
from pprint import pprint
FILE = 'voyna-i-mir.txt.zip'


class StatMaker:
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.sorted_stat = []
        self.file = ''

    def prepare_file(self):  # 1) получение данных (тут может быть подготовка файла/его разахивация)
        if self.file_name.endswith('.zip'):
            zfile = zipfile.ZipFile(self.file_name, 'r')
            self.file_name = ''
            for filename in zfile.namelist():
                zfile.extract(filename)
            self.file_name = filename
        with open(self.file_name, 'r', encoding='cp1251') as file:  # перенес сюда, чтобы избежать большой
            # вложенности в collect_data()
            self.collect_data(file)

    def collect_data(self, file):  # 2) сбор даннных - подсчёт частоты использования букв
        for line in file:
            for char in line:
                if char.isalpha():
                    self.stat[char] = self.stat.get(char, 0) + 1

    def sort_chars(self):  # 3) сортировка статистических данных,
        self.sorted_stat = sorted(self.stat.items(), key=operator.itemgetter(1), reverse=True)
        return self.sorted_stat

    def print_stat(self):  # 4) вывод в консоль таблицы с данными.
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for item in self.sorted_stat:
            print(f'|{item[0]:^9}|{item[1]:^10}|')
        print('+---------+----------+')
        values = self.stat.values()
        total_chars = sum(values)
        print(f'|{"ИТОГО": ^9}|{total_chars:^10}|')
        print('+---------+----------+')

    def launch(self):
        self.prepare_file()  # а) подготовка файла (разархивация, при необходимости)
        self.collect_data(file=self.file)  # б) сбор данных из файла
        self.sort_chars()  # в) сортировка
        self.print_stat()  # г) вывод в консоль


statmaker = StatMaker(file_name=FILE)
statmaker.launch()

# зачет первой части
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
