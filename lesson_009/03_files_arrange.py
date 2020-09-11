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

    def run(self):
        zfile = zipfile.ZipFile(self.file_name, 'r')
        self.file_name = ''
        for filename in zfile.namelist():
            for dirpath, dirnames, filenames in os.walk(zfile.extract(filename)):
                for file in filenames:
                    full_file_path = os.path.join(dirpath, file)
                    modification_time = os.path.getmtime(full_file_path)
                    actual_time = time.gmtime(modification_time)

                    year = actual_time.tm_year
                    month = actual_time.tm_mon
                    path = self.out_file
                    pathos = os.path.join(path, str(year))
                    path_month = os.path.join(pathos, str(month))

                    if os.path.exists(pathos):
                        if os.path.exists(path_month):
                            shutil.copy2(full_file_path, path_month)
                        else:
                            os.makedirs(path_month)
                            shutil.copy2(full_file_path, path_month)
                    else:
                        os.makedirs(path_month)
                        shutil.copy2(full_file_path, path_month)

    def launch(self):
        self.run()


order = OrderFiles(file_name=FILE, out_file=FILE_OUT)
order.launch()




# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html

# зачет!
