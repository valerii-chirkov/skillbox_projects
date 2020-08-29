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

    def unzip(self):  # 1) получение данных (тут может быть подготовка файла - его разахивация, при необходимости),
        zfile = zipfile.ZipFile(self.file_name, 'r')
        self.file_name = ''
        for filename in zfile.namelist():
            zfile.extract(filename)
        self.file_name = filename

    def collect_data(self):  # 1) получение данных (тут может быть подготовка файла - его разахивация, при необходимости),
        if self.file_name.endswith('.zip'):  # todo Эти две строки (то есть весь if) и есть "подготовка файла"
            self.unzip()
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                self.collect_char(line)

    def collect_char(self, line):  # 2) сбор даннных - подсчёт частоты использования букв,
        for char in line:
            if char.isalpha():
                self.stat[char] = self.stat.get(char, 0) + 1

    def sort_chars(self):  # 3) сортировка статистических данных,
        self.sorted_stat = sorted(self.stat.items(), key=operator.itemgetter(1), reverse=True)
        #  забыли указать self. перед именем атрибута stat
        #  если так делаю, то подсвечивается .items() и выдает ошибку Unresolved attribute reference 'items' for class 'list'
        # todo Вы правы, просмотрел, что stat это словарь, а нужен список. Создаём новый атрибут-список для
        #  сортированных данных, сохраняем результат сортировки в него и его используем в печати в консоль
        return self.sorted_stat

    def print_stat(self):  # 4) вывод в консоль таблицы с данными.
        print('+---------+----------+')
        print('|  буква  | частота  |')
        print('+---------+----------+')
        for item in self.sorted_stat:
            #  итерируйте по атрибуту self.stat
            #  выдает ошибку
            #  File "/Users/valeriichirkov/PycharmProjects/python_base/lesson_009/01_char_stat.py", line 70, in print_stat
            #     print(f'|{item[0]:^9}|{item[1]:^10}|')
            # IndexError: string index out of range
            # todo поправил на список, если есть вопросы почему так, то спрашивайте
            print(f'|{item[0]:^9}|{item[1]:^10}|')  # На вот это жалуется, думаю из-за того что в sort_chars() нужно
            # делать self.stat = ... return self.stat, но выдает ошибку, написал в туду.
        print('+---------+----------+')
        values = self.stat.values()
        total_chars = sum(values)
        print(f'|{"ИТОГО": ^9}|{total_chars:^10}|')
        print('+---------+----------+')

    def launch(self):
        # а) подготовка файла (разархивация, при необходимости)
        self.collect_data()  # б) сбор данных из файла  #  по шаблонному методу должно быть так (ниже)
        # self.collect_char(line)  #  как вызвать этот метод, если он уже вызывается в .open()?
        #  значить open назовите "сбор данных" и именно его тут вызывайте
        #  переименовал, но тогда подготовки файла получается нет
        # todo под подготовкой данных пока может быть только разархивация если передан архив, поэтому создаём метод
        #  "подготовка_файла", в него помещаем разархивацию по условую, а тут, в шаблонном методе перед сбором данных,
        #  вызываем "подготовку файла"
        self.sort_chars()  # в) сортировка
        self.print_stat()  # г) вывод в консоль


statmaker = StatMaker(file_name=FILE)
statmaker.launch()

# После зачета первого этапа нужно сделать упорядочивание статистики
#  - по частоте по возрастанию
#  - по алфавиту по возрастанию
#  - по алфавиту по убыванию
