# -*- coding: utf-8 -*-

import os
import time
import shutil
import zipfile
import platform
from pprint import pprint
FILE = 'icons.zip'
FILE_OUT = 'icons_by_year'

# Нужно написать скрипт для упорядочивания фотографий (вообще любых файлов)
# Скрипт должен разложить файлы из одной папки по годам и месяцам в другую.
# Например, так:
#   исходная папка
#       icons/cat.jpg
#       icons/man.jpg
#       icons/new_year_01.jpg
#   результирующая папка
#       icons_by_year/2018/05/cat.jpg
#       icons_by_year/2018/05/man.jpg
#       icons_by_year/2017/12/new_year_01.jpg
#
# Входные параметры основной функции: папка для сканирования, целевая папка.
# Имена файлов в процессе работы скрипта не менять, год и месяц взять из времени последней модификации файла
# (время создания файла берется по разному в разых ОС - см https://clck.ru/PBCAX - поэтому берем время модификации).
#
# Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
# Имя целевой папки - icons_by_year (тогда она не попадет в коммит, см .gitignore в папке ДЗ)
#
# Пригодятся функции:
#   os.walk
#   os.path.dirname
#   os.path.join
#   os.path.normpath
#   os.path.getmtime
#   time.gmtime
#   os.makedirs
#   shutil.copy2
#
# Чтение документации/гугла по функциям - приветствуется. Как и поиск альтернативных вариантов :)
#
# Требования к коду: он должен быть готовым к расширению функциональности - делать сразу на классах.
# Для этого пригодится шаблон проектирование "Шаблонный метод"
#   см https://refactoring.guru/ru/design-patterns/template-method
#   и https://gitlab.skillbox.ru/vadim_shandrinov/python_base_snippets/snippets/4


class OrderFiles:
    def __init__(self, file_name, out_file):
        self.file_name = file_name
        self.out_file = out_file
        self.icons = {}
        self.icons_local_time = {}

    def prepare_file(self):  # todo Этого делать не надо, в задании указано, цитата:
        # Файлы для работы взять из архива icons.zip - раззиповать проводником ОС в папку icons перед написанием кода.
        # todo В усложнённом варианте, надо итрериовать по zfile.infolist(), получать данные о времени из архива,
        #  открывать файл в архиве средсвами zipfile и копировать этот файл в нужное место. Но это надо делать после
        #  того как выполните основную задачу.

        if self.file_name.endswith('.zip'):
            zfile = zipfile.ZipFile(self.file_name, 'r')

            for filename in zfile.namelist():
                zfile.extract(filename)
            self.file_name = self.file_name[:-4]

    def run(self):
        count = 0
        for dirpath, dirnames, filenames in os.walk(self.file_name):
            print('*' * 27)
            count += len(filenames)
            for file in filenames:
                full_file_path = os.path.join(dirpath, file)
                modification_time = os.path.getmtime(full_file_path)
                local_time = time.ctime(modification_time)
                # todo используйте time.gmtime() чтобы преобразовать секунды из local_time в список с годом, месяцем и
                #  т.д. Из этого списка получите индексацией нужные данные и сконструируйте "путь" для копирования файла
                # self.icons[local_time] = self.icons.get(local_time, full_file_path)   Почему-то не работает

                # self.icons[modification_time] = self.icons.get(modification_time, full_file_path)
                # self.icons[local_time] = self.icons[modification_time]   так тоже, оставляет один файл
                # del self.icons[modification_time]

                self.icons[modification_time] = self.icons.get(modification_time, full_file_path)
                # self.icons_local_time[local_time] = self.icons.get(local_time, full_file_path)
                # todo Не вполне ясно, зачем перекладывать информацию из одного ключа в другой. Нужно получить год и
                #  месяц модификации файла, "сконструировать" пусть куда файл надо скопировать и выполнить копирование -
                #  собирать данные в словари не надо - а только по очереди копировать файлы.
        # pprint(self.icons)
        # pprint(self.icons_local_time)

    def convert_to_local(self):
        pass

    def icons_by_year(self):
        pass

    def launch(self):
        self.prepare_file()
        self.run()
        self.convert_to_local()


order = OrderFiles(file_name=FILE, out_file=FILE_OUT)
order.launch()




# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html
