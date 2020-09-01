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
        self.stat_keys = []
        self.sort_input = ''

    def prepare_file(self):  # 1) получение данных (тут может быть подготовка файла/его разахивация)
        if self.file_name.endswith('.zip'):
            zfile = zipfile.ZipFile(self.file_name, 'r')
            self.file_name = ''
            for filename in zfile.namelist():
                zfile.extract(filename)
            self.file_name = filename
        with open(self.file_name, 'r', encoding='cp1251') as file:
            self.collect_data(file)

    def collect_data(self, file):  # 2) сбор даннных - подсчёт частоты использования букв
        for line in file:
            for char in line:
                if char.isalpha():
                    self.stat[char] = self.stat.get(char, 0) + 1

    # def sort_chars(self):
    #  #  Одна из важных частей изучаемого паттерна - новая функцинальность добавляется не универсализацией
    #  #  одного класса, а переопределением методов в наследниках. В данном случае тут надо оставить одну из сортировок,
    #  #  а все новые методы сортировки расположить в наследниках. То есть, допустим в базовом классе оставляет
    #  #  сортировку по убыванию, а для сортировки по возрастанию делаем наследника и переопределяем метод сортировки.
    #  #  С остальными методам сортировки надо поступить также - каждый поместить в своего наследника базового класса.
    #     while True:
    #         print('1 - по частоте по убыванию')
    #         print('2  - по частоте по возрастанию')
    #         print('3  - по алфавиту по возрастанию')
    #         print('4  - по алфавиту по убыванию')
    #         self.sort_input = input('Введите способ сортировки: ')
    #         if self.sort_input == '1':
    #             self.sort_chars_frequency_decrease()
    #             break
    #         elif self.sort_input == '2':
    #             self.sort_chars_frequency_increase()
    #             break
    #         elif self.sort_input == '3':
    #             self.sort_chars_alphabet_increase()
    #             break
    #         elif self.sort_input == '4':
    #             self.sort_chars_alphabet_decrease()
    #             break
    #         else:
    #             print('Повторите попытку')

    def sort(self):  # 3) сортировка статистических данных (убывание по частоте)
        self.sorted_stat = sorted(self.stat.items(), key=operator.itemgetter(1), reverse=True)
        return self.sorted_stat

    # def sort_chars_frequency_increase(self):  # 3) сортировка статистических данных (возрастание по частоте)
    #     self.sorted_stat = sorted(self.stat.items(), key=operator.itemgetter(1), reverse=False)
    #     return self.sorted_stat

    # def sort_chars_alphabet_increase(self):  # 3) сортировка статистических данных (возрастание по алфавиту)
    #     self.stat_keys = list(self.stat.keys())
    #     self.stat_keys.sort()
    #     for key in self.stat_keys:
    #         self.sorted_stat.append([key, self.stat[key]])
    #     return self.sorted_stat

    # def sort_chars_alphabet_decrease(self):  # 3) сортировка статистических данных (убывание по алфавиту)
    #     self.stat_keys = list(self.stat.keys())
    #     self.stat_keys.sort()
    #     self.stat_keys.reverse()
    #     for key in self.stat_keys:
    #         self.sorted_stat.append([key, self.stat[key]])
    #     return self.sorted_stat

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
        self.sort()  # в) сортировка
        # self.sort_chars()
        self.print_stat()  # г) вывод в консоль


class SortCharsFrequencyIncrease(StatMaker):
    def sort(self):
        self.sorted_stat = sorted(self.stat.items(), key=operator.itemgetter(1), reverse=False)
        return self.sorted_stat


class SortCharsAlphabetIncrease(StatMaker):  # 3) сортировка статистических данных (возрастание по алфавиту)
    def sort(self):
        self.stat_keys = list(self.stat.keys())
        self.stat_keys.sort()
        for key in self.stat_keys:
            self.sorted_stat.append([key, self.stat[key]])
        return self.sorted_stat


class SortCharsAlphabetDecrease(StatMaker):
    def sort(self):  # 3) сортировка статистических данных (убывание по алфавиту)
        self.stat_keys = list(self.stat.keys())
        self.stat_keys.sort()
        self.stat_keys.reverse()
        for key in self.stat_keys:
            self.sorted_stat.append([key, self.stat[key]])
        return self.sorted_stat


statmaker = StatMaker(file_name=FILE)
sort1 = SortCharsFrequencyIncrease(file_name=FILE)
sort2 = SortCharsAlphabetIncrease(file_name=FILE)
sort3 = SortCharsAlphabetDecrease(file_name=FILE)
sort2.launch()
# зачет первой части
# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию

# зачет!
