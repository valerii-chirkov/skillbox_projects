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
from random import randint
from pprint import pprint

# zip_file_name = 'voyna-i-mir.txt.zip'
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zfile.namelist():
#     zfile.extract(filename)
class StatMaker:
    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.prev_char = ''

    def unzip(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def open(self):
        if self.file_name.endswith('.zip'):
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.check_alfa(line)

    def check_alfa(self, line):
        for char in line:
            if char.isalpha():
                self.collect_char(char)

    def collect_char(self, char):
        if self.prev_char in self.stat:
            if char in self.stat[self.prev_char]:
                self.stat[self.prev_char][char] += 1
            else:
                self.stat[self.prev_char][char] = 1
        else:
            self.stat[self.prev_char] = {char: 1}

    def sort_stat_max_to_min(self):
        sorted_stat = sorted(self.stat[self.prev_char].items(), key=operator.itemgetter(1), reverse=True)
        return sorted_stat

    def print_stat(self):
        print(f'+---------+----------+')
        print(f'|  буква  | частота  |')
        print(f'+---------+----------+')
        # pprint(self.sort_stat_max_to_min())
        for item in self.sort_stat_max_to_min():
            # print(*item)  # Как заставить работать с f-методом? Выводит все без лишних символов
            # item[0] = item[0].translate(None, '()'',')  # Подсмотрел такой вариант, но не работает с тьюплами
            print(f'{item}')


statmaker = StatMaker(file_name='voyna-i-mir.txt.zip')
statmaker.open()
statmaker.print_stat()




# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
