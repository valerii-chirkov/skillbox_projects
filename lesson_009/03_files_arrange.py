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
        if not os.path.exists(self.out_file):
            os.mkdir(self.out_file)

        with open(self.file_name, 'a') as ff:
            for file in archive.namelist():
                modification_time = archive.getinfo(file).date_time
                year, month, day = modification_time[0], modification_time[1], modification_time[2]
                print(year, month)

                archive.extract(file)  # TODO  создаю промежуточную папку
                full_file_path = os.path.join(file)  # TODO не могу догадаться как брать файл из зипа и сразу его кидать
                # TODO в icons_by_year без создание промежут. папки

                path_year = os.path.join(self.out_file, str(year))
                path_month = os.path.join(path_year, str(month))
                try:  # TODO Жалуется на папку, говорит что проблема в 70 строке (прод. строка 76)
                    if os.path.exists(path_year):
                        if os.path.exists(path_month):
                            shutil.copy2(full_file_path, path_month)
                        else:
                            os.makedirs(path_month, exist_ok=True)
                            shutil.copy2(full_file_path, path_month)
                    else:
                        os.makedirs(path_month)
                        shutil.copy2(full_file_path, path_month)  # TODO Но выходит из цикла на первом проходе здесь (67)
                except Exception:
                    pass
            shutil.rmtree(self.file_name[:-4])  # TODO удаляю папку
            print(self.out_file, str(file[6:]))


order = OrderFiles(file_name=FILE, out_file=FILE_OUT)
order.run()


# Усложненное задание (делать по желанию)
# Нужно обрабатывать zip-файл, содержащий фотографии, без предварительного извлечения файлов в папку.
# Это относится только к чтению файлов в архиве. В случае паттерна "Шаблонный метод" изменяется способ
# получения данных (читаем os.walk() или zip.namelist и т.д.)
# Документация по zipfile: API https://docs.python.org/3/library/zipfile.html

# зачет!
