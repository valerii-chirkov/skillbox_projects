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
import time
import datetime
# TODO думал что получится решить через библиотеки со временем и датой, но не разобрался как ими пользоваться
FILE = 'events.txt'
OUT_FILE = 'events_out.txt'


class NOKParser:
    def __init__(self, file_name, out_file):
        self.file_name = file_name
        self.out_file = out_file
        self.prev_line = ''
        self.counter = 1

    def prepare_file(self):  # 1) получение данных (тут может быть подготовка файла/его разахивация)
        if self.file_name.endswith('.zip'):
            zfile = zipfile.ZipFile(self.file_name, 'r')
            self.file_name = ''
            for filename in zfile.namelist():
                zfile.extract(filename)
            self.file_name = filename

    def save_noks(self, out_file):
        file_out = open(out_file, 'w', encoding='utf8')
        with open(self.file_name, 'r', encoding='cp1251') as file:
            for line in file:  # Запись первой строки
                self.get_first_nok(line)
                self.counter = 0
                break
            for line in file:
                self.count_noks(file_out, line)

    def get_first_nok(self, line):
        if 'NOK' in line:
            self.prev_line = line

    def count_noks(self, file_out, line):
        if 'NOK' in line:  # if line.count('NOK') TODO Есть разница?
            if self.prev_line[0:18] in line[0: 18]:  # Если содержание пред. строки(до секунд)совпадает с линией
                self.counter += 1  # то накидываем в каунтер
            else:
                self.counter = str(self.counter)  # Переводим счетчик в строку
                appendix = f']{self.counter}'  # Добавляем к нему скобку
                file_out.write(self.prev_line[0:17] + appendix + '\n')  # И записываем с переносом строки
                self.counter = 1  # возвращаем счетчик
            self.prev_line = line  # И все по новой, теперь у нас эта строка стала предыдущей, по ней будем проверять

    def launch(self):
        self.save_noks(out_file=OUT_FILE)
        # TODO знаю что по шаблонному методу тут должны быть другие методы, но не понимаю принцип:
        # TODO если мы передаем в метод параметры и вызываем его в другом методе, то его в launch уже не нужно добавлять

        # TODO По сути у меня один метод разбит на маленькие другие,
        # TODO получается структура должна была быть такой:
        # 1. Распаковка файла
        # 2. Сохраняем в файл ноки
        # 3. Откидываем лишнее (секунды и млсекунды)
        # 4. Потом считаем сколько у нас повторялось и откидываем повторные
        # 5. Запускаем все попорядку
        # TODO но у меня возникала проблема, что на каждый метод мне нужно было или перезаписывать предыдущий events_out
        # TODO или создавать временный, передавать его в следующий метод, там его удалять и создавать опять новый временный
        # TODO я не решил какой метод будет лучше, потому что и так, и так не работало :) поэтому пошел по такому пути.


nokparser = NOKParser(file_name=FILE, out_file=OUT_FILE)
nokparser.launch()

# После зачета первого этапа нужно сделать группировку событий
#  - по часам
#  - по месяцу
#  - по году
