# -*- coding: utf-8 -*-


# Описание предметной области:
#
# При торгах на бирже совершаются сделки - один купил, второй продал.
# Покупают и продают ценные бумаги (акции, облигации, фьючерсы, етс). Ценные бумаги - это по сути долговые расписки.
# Ценные бумаги выпускаются партиями, от десятка до несколько миллионов штук.
# Каждая такая партия (выпуск) имеет свой торговый код на бирже - тикер - https://goo.gl/MJQ5Lq
# Все бумаги из этой партии (выпуска) одинаковы в цене, поэтому говорят о цене одной бумаги.
# У разных выпусков бумаг - разные цены, которые могут отличаться в сотни и тысячи раз.
# Каждая биржевая сделка характеризуется:
#   тикер ценнной бумаги
#   время сделки
#   цена сделки
#   обьем сделки (сколько ценных бумаг было куплено)
#
# В ходе торгов цены сделок могут со временем расти и понижаться. Величина изменения цен называтея волатильностью.
# Например, если бумага №1 торговалась с ценами 11, 11, 12, 11, 12, 11, 11, 11 - то она мало волатильна.
# А если у бумаги №2 цены сделок были: 20, 15, 23, 56, 100, 50, 3, 10 - то такая бумага имеет большую волатильность.
# Волатильность можно считать разными способами, мы будем считать сильно упрощенным способом -
# отклонение в процентах от полусуммы крайних значений цены за торговую сессию:
#   полусумма = (максимальная цена + минимальная цена) / 2
#   волатильность = ((максимальная цена - минимальная цена) / полусумма) * 100%
# Например для бумаги №1:
#   half_sum = (12 + 11) / 2 = 11.5
#   volatility = ((12 - 11) / half_sum) * 100 = 8.7%
# Для бумаги №2:
#   half_sum = (100 + 3) / 2 = 51.5
#   volatility = ((100 - 3) / half_sum) * 100 = 188.34%
#
# В реальности волатильность рассчитывается так: https://goo.gl/VJNmmY
#
# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью.
# Бумаги с нулевой волатильностью вывести отдельно.
# Результаты вывести на консоль в виде:
#   Максимальная волатильность:
#       ТИКЕР1 - ХХХ.ХХ %
#       ТИКЕР2 - ХХХ.ХХ %
#       ТИКЕР3 - ХХХ.ХХ %
#   Минимальная волатильность:
#       ТИКЕР4 - ХХХ.ХХ %
#       ТИКЕР5 - ХХХ.ХХ %
#       ТИКЕР6 - ХХХ.ХХ %
#   Нулевая волатильность:
#       ТИКЕР7, ТИКЕР8, ТИКЕР9, ТИКЕР10, ТИКЕР11, ТИКЕР12
# Волатильности указывать в порядке убывания. Тикеры с нулевой волатильностью упорядочить по имени.
#
# Подготовка исходных данных
# 1. Скачать файл https://drive.google.com/file/d/1l5sia-9c-t91iIPiGyBc1s9mQ8RgTNqb/view?usp=sharing
#       (обратите внимание на значок скачивания в правом верхнем углу,
#       см https://drive.google.com/file/d/1M6mW1jI2RdZhdSCEmlbFi5eoAXOR3u6G/view?usp=sharing)
# 2. Раззиповать средствами операционной системы содержимое архива
#       в папку python_base/lesson_012/trades
# 3. В каждом файле в папке trades содержится данные по сделакам по одному тикеру, разделенные запятыми.
#   Первая строка - название колонок:
#       SECID - тикер
#       TRADETIME - время сделки
#       PRICE - цена сделки
#       QUANTITY - количество бумаг в этой сделке
#   Все последующие строки в файле - данные о сделках
#
# Подсказка: нужно последовательно открывать каждый файл, вычитывать данные, высчитывать волатильность и запоминать.
# Вывод на консоль можно сделать только после обработки всех файлов.
#
# Для плавного перехода к мультипоточности, код оформить в обьектном стиле, используя следующий каркас
#
import csv
import os
from itertools import groupby
import threading
DIRECTORY = 'trades'


class Volatility:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.list_files = os.listdir(file_name)
        self.volatility_stat = []
        self.min_volatility = []
        self.max_volatility = []
        self.zero_volatility = []

    def open(self):
        for file_csv in self.list_files:
            path = self.file_name + '/' + file_csv
            with open(path, 'r') as ff:
                reader = csv.reader(ff)
                self.run(reader)

    def run(self, reader):
        ticker, prices = '', []
        for row in reader:
            ticker = row[0]
            if not row.count('PRICE'):
                prices.append(row[2])

        max_price, min_price = float(max(prices)), float(min(prices))
        half_sum = ((max_price + min_price) / 2)
        volatility = round((((max_price - min_price) / half_sum) * 100), 2)
        #  появляется отрицательная волатильность, проблема в max_price и min_price, некоректно показываются
        self.volatility_stat.append([ticker, volatility])

    def sort(self):
        self.open()
        self.min_volatility = sorted(self.volatility_stat, key=lambda price: price[1])
        self.min_volatility = [el for el, _ in groupby(self.min_volatility)]  #  тут в роли костыля,
        # тк повторялся O2H9 - -2.04, но вообще отрицательной не может быть, поэтому что-то с min и max price'ами
        self.max_volatility = sorted(self.volatility_stat, key=lambda price: price[1], reverse=True)
        for ticker in self.volatility_stat:
            if ticker[1] == 0.0:
                self.zero_volatility.append(ticker[0])
        self.zero_volatility = sorted(self.zero_volatility)
        self.zero_volatility = [el for el, _ in groupby(self.zero_volatility)]  #  чтобы сохранить порядок
        return self.min_volatility, self.max_volatility, self.zero_volatility

    def print(self):
        print('Max volatility: ')
        for value in self.sort()[1][:3]:
            print('   ' + str(value[0]) + ' - ' + str(value[1]))
        print('Min volatility: ')
        for value in self.sort()[0][:3]:
            print('   ' + str(value[0]) + ' - ' + str(value[1]))
        print('Zero volatility: ')
        print('  ', ', '.join(self.zero_volatility))

    def threading(self):
        thread = threading.Thread(target=self.print(), args=(1,))
        thread.start()
# TODO Так как в следующей задаче будет попытка посчитать тоже самое во многопоточном варианте, нам нужно будет
#  запускать обработку каждого файла отдельным объектом класса, для чего код должен быть организован таким образом,
#  чтобы каждый объект "работал" бы только над одним файлом. Вынесите цикл по файлам из класса, это должен быть внешний
#  цикл. Данные можно складывать в глобальные переменные либо создавать список объектов (откуда потом объединять все
#  данные по тикерам в общую переменую) и обрабатывать данные атрибутов объектов тоже внешним кодом (сортировка,
#  вывод результата)


volatility_calculator = Volatility(file_name=DIRECTORY)
volatility_calculator.threading()

# TODO написать код в однопоточном/однопроцессорном стиле
