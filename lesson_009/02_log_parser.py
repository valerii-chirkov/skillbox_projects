# -*- coding: utf-8 -*-

# Имеется файл events.txt вида:
#
# [2018-05-17 01:55:52.665804] NOK
# [2018-05-17 01:56:23.665804] OK
# [2018-05-17 01:56:55.665804] OK
# [2018-05-17 01:57:16.665804] NOK
# [2018-05-17 01:57:58.665804] OK
# ...
#
# Напишите программу, которая считывает файл
# и выводит число событий NOK за каждую минуту в другой файл в формате
#
# [2018-05-17 01:57] 1234
# [2018-05-17 01:58] 4321
# ...
#
# Входные параметры: файл для анализа, файл результата
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4

import zipfile
FILE = 'events.txt'
OUT_FILE = 'events_out.txt'


class NOKParser:
    def __init__(self, file_name, out_file):
        self.file_name = file_name
        self.out_file = out_file
        self.keys = {}
        self.date = ''
        self.cut = None

    def setup_cut(self):  # todo Вот этот самый метод, который будем переопределять
        self.cut = 17

    def fill_dict(self):
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:
                if 'NOK' in line:
                    self.get_date(line)
                    self.grouping()

    def get_date(self, line):
        self.date = line[0:self.cut] + ']'
        return self.date

    def grouping(self):
        self.keys[self.date] = self.keys.get(self.date, 0) + 1

    def write_out_file(self):
        with open(self.out_file, 'w', encoding='utf8') as file:
            for date in self.keys:
                amount = str(self.keys.get(date))
                line = date + ' ' + amount + '\n'
                file.write(line)

    def launch(self):
        self.setup_cut()
        self.fill_dict()
        self.write_out_file()


class GroupingHours(NOKParser):
    def setup_cut(self):
        self.cut = 14


# class GroupingDays(NOKParser):
#     pass
#
#
# class GroupingMonths(NOKParser):
#     pass
#
#
# class GroupingYears(NOKParser):
#     pass


nokparser = NOKParser(file_name=FILE, out_file=OUT_FILE)
# sort1 = GroupingHours(file_name=FILE, out_file=OUT_FILE, cut=14)
# sort2 = GroupingDays(file_name=FILE, out_file=OUT_FILE, cut=11)
# sort3 = GroupingMonths(file_name=FILE, out_file=OUT_FILE, cut=8)
# sort4 = GroupingYears(file_name=FILE, out_file=OUT_FILE, cut=5)
nokparser.launch()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
