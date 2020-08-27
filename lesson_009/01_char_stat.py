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

# TODO убирайте такой мертвый код, он только захламляет модуль
# zip_file_name = 'voyna-i-mir.txt.zip'
# zfile = zipfile.ZipFile(zip_file_name, 'r')
# for filename in zfile.namelist():
#     zfile.extract(filename)
class StatMaker:  # TODO РЕР8: до и после определения класса должно быть по 2 пустых строки
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
        # todo Постарайтесь упростить до плоского словаря: ключ это символ, а значение его кол-во в тексте. Тогда весь
        #  код метода можно будет записать в одну строку: self.stat[char] = self.stat.get(char, 0) + 1

    def sort_stat_max_to_min(self):
        sorted_stat = sorted(self.stat[self.prev_char].items(), key=operator.itemgetter(1), reverse=True)
        return sorted_stat

    def print_stat(self):
        print(f'+---------+----------+')  # todo А тут и не обязательны f-строки, это же статический текст
        print(f'|  буква  | частота  |')
        print(f'+---------+----------+')
        # pprint(self.sort_stat_max_to_min())
        for item in self.sort_stat_max_to_min():  # todo C точки зрения реализации паттерна, удобнее тут выводить уже
            # готовые отсортированные данные, так как все основные шаги-методы должны вызываться в "шаблонном" методе,
            # то есть в методе печати вызывать сортировку это не правильно.

            # print(*item)  # Как заставить работать с f-методом? Выводит все без лишних символов
            # item[0] = item[0].translate(None, '()'',')  # Подсмотрел такой вариант, но не работает с тьюплами
            print(f'|{item[0]:^5}|{item[1]:^7}|')
            # todo выводите сами данные, а также границы таблицы, для его используйте возможности
            #  форматирования с указанием ширины места для числа c заполнением остального места пробелами.
            #  Добавьте также строку с итоговыми данными


    # TODO Для реализации паттерна необходимо разбить всю выполняемую задачу на отдельные шаги:
    #  1) получение данных (тут может быть подготовка файла - его разахивация, при необходимости),
    #  2) сбор даннных - подсчёт частоты использования букв,
    #  3) сортировка статистических данных,
    #  4) вывод в консоль таблицы с данными.
    #  Также потребуется сам "шаблонный метод", где последовательно вызываются все методы по порядку.
    #    а) подготовка файла (разархивация, при необходимости)
    #    б) сбор данных из файла
    #    в) сортировка
    #    г) вывод в консоль
    #  Имя шаблонного метода должно быть кратким, например: "запустить", "выполнить"

statmaker = StatMaker(file_name='voyna-i-mir.txt.zip')
# TODO Имена файлов надо присваивать константам и использовать в основном коде только их.

statmaker.open()
statmaker.print_stat()
# TODO Тут надо вызвать только один метод - шаблонный.


# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
