# -*- coding: utf-8 -*-

# На основе своего кода из lesson_009/02_log_parser.py напишите итератор (или генератор)
# котрый читает исходный файл events.txt и выдает число событий NOK за каждую минуту
# <время> <число повторений>
#
# пример использования:
#
# grouped_events = <создание итератора/генератора>  # Итератор или генератор? выбирайте что вам более понятно
# for group_time, event_count in grouped_events:
#     print(f'[{group_time}] {event_count}')
#
# на консоли должно появится что-то вроде
#
# [2018-05-17 01:57] 1234
FILE = 'events.txt'


def get_noks():
    cut = 17
    keys = {}

    with open(FILE, 'r', encoding='cp1251') as file:
        for line in file:
            if 'NOK' in line:
                date = line[0:cut] + ']'
                keys[date] = keys.get(date, 0) + 1

    for date in keys:
        amount = str(keys.get(date))
        line = date + ' ' + amount + '\n'
        yield line


grouped_events = get_noks()
for nok in grouped_events:
    print(nok)


# class NOKParser:
#     def __init__(self, file_name):
#         self.file_name = file_name
#         self.keys = {}
#         self.date = ''
#         self.cut = None
#
#     def setup_cut(self):
#         self.cut = 17
#
#     def fill_dict(self):
#         with open(self.file_name, 'r', encoding='cp1251') as file:
#             for line in file:
#                 if 'NOK' in line:
#                     self.get_date(line)
#                     self.grouping()
#
#     def get_date(self, line):
#         self.date = line[0:self.cut] + ']'
#         return self.date
#
#     def grouping(self):
#         self.keys[self.date] = self.keys.get(self.date, 0) + 1
#
#     def write_out_file(self):
#         for date in self.keys:
#             amount = str(self.keys.get(date))
#             line = date + ' ' + amount + '\n'
#             print(line)
#
#     def launch(self):
#         self.setup_cut()
#         self.fill_dict()
#         self.write_out_file()
#
#
# class GroupingMinutes(NOKParser):
#     def setup_cut(self):
#         self.cut = 17
#
#
# nokparser = NOKParser(file_name=FILE)
# sort1 = GroupingMinutes(file_name=FILE)
# sort1.launch()