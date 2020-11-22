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

DIRECTORY = 'trades'


class Volatility:

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.list_files = os.listdir(file_name)
        self.volatility_stat = []
        self.min_volatility, self.max_volatility, self.zero_volatility = [], [], []
        self.volatility = 0.0
        self.max_price, self.min_price, self.half_sum, self.ticker, self.prices = 0, 0, 0, '', []

    def run(self):
        path = volatility_calculator.file_name + '/' + file_csv
        with open(path, 'r') as ff:
            reader = csv.reader(ff)

            for row in reader:
                self.ticker = row[0]
                if not row.count('PRICE'):
                    self.prices.append(float(row[2]))

            self.max_price, self.min_price = float(max(self.prices)), float(min(self.prices))
            half_sum = ((self.max_price + self.min_price) / 2)
            self.volatility = round((((self.max_price - self.min_price) / half_sum) * 100), 2)


def print_stat(max, min, zero):
    print('Max volatility: ')
    for value in max[:3]:
        print('   ' + str(value[0]) + ' - ' + str(value[1]))

    print('Min volatility: ')
    for value in min[:3]:
        print('   ' + str(value[0]) + ' - ' + str(value[1]))

    print('Zero volatility: ')
    print('  ', ', '.join(zero))


volatility_calculator = Volatility(file_name=DIRECTORY)

for file_csv in volatility_calculator.list_files:
    volatility_calculator.run()
    volatility_calculator.volatility_stat.append([volatility_calculator.ticker, volatility_calculator.volatility])
    volatility_calculator.max_price, volatility_calculator.min_price, volatility_calculator.half_sum = 0, 0, 0
    volatility_calculator.ticker, volatility_calculator.prices = '', []

for ticker in volatility_calculator.volatility_stat:
    if ticker[1] == 0.0:
        volatility_calculator.zero_volatility.append(ticker[0])
        # volatility_calculator.min_volatility.remove(ticker)
        # print(ticker) # TODO почему-то не удаляется элемент из списка

volatility_calculator.zero_volatility = sorted(volatility_calculator.zero_volatility)

volatility_calculator.min_volatility = sorted(volatility_calculator.volatility_stat, key=lambda price: price[1])
volatility_calculator.min_volatility = [el for el, _ in groupby(volatility_calculator.min_volatility)]

volatility_calculator.max_volatility = sorted(volatility_calculator.volatility_stat, key=lambda price: price[1],
                                              reverse=True)

print_stat(max=volatility_calculator.max_volatility,
           min=volatility_calculator.min_volatility,
           zero=volatility_calculator.zero_volatility)

# TODO написать код в однопоточном/однопроцессорном стиле
