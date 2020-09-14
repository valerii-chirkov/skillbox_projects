# -*- coding: utf-8 -*-

import os
import shutil
import zipfile
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
        archive = zipfile.ZipFile(self.file_name, 'r')
        with open(self.out_file, 'a') as ff:  # todo Вы пытаетесь открыть папку, которой на самом деле может не быть
                                              #  (удалите папки icons и icons_by_year, если они есть.
                                              #  Папка icons_by_year должна создаваться этой программой). Тут надо
                                              #  открывать файл архива, перебирать (итерировать) файлы, смотреть время
                                              #  модификации именно внутри архива, а потом извлекать или копировать файл
                                              #  из архива на диск, в целевую папку
            for file in archive.namelist():
                modification_time = archive.getinfo(file).date_time
                year, month, day = modification_time[0], modification_time[1], modification_time[2]
                print(year, month)

                full_file_path = os.path.join(file)

                pathos = os.path.join(ff.name, str(year))
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


order = OrderFiles(file_name=FILE, out_file=FILE_OUT)
order.run()


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html

# зачет!
