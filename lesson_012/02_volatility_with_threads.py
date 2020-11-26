# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПОТОЧНОМ стиле
#
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
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/01_volatility.py !!!
import csv
import os
from itertools import groupby
from threading import Thread

DIRECTORY = 'trades'
min_volatility, max_volatility, zero_volatility, volatility_stat = [], [], [], []


class Volatility(Thread):

    def __init__(self, file_name):
        self.file_name = file_name
        self.stat = {}
        self.volatility = 0.0
        self.max_price, self.min_price, self.half_sum, self.ticker, self.prices = 0, 0, 0, '', []

    def run(self):
        path = os.path.join(DIRECTORY, self.file_name)
        with open(path, 'r') as ff:
            reader = csv.reader(ff)

            for row in reader:
                self.ticker = row[0]
                if not row.count('PRICE'):
                    self.prices.append(float(row[2]))

            self.max_price, self.min_price = float(max(self.prices)), float(min(self.prices))
            half_sum = ((self.max_price + self.min_price) / 2)
            self.volatility = round((((self.max_price - self.min_price) / half_sum) * 100), 2)


def get_tickers():
    files_list = []
    for file_csv in os.listdir(DIRECTORY):
        files_list.append(Volatility(file_csv))
    return files_list


def get_values():
    for ticker in get_tickers():
        ticker.run()
        volatility_stat.append([ticker.ticker, ticker.volatility])
        ticker.max_price, ticker.min_price, ticker.half_sum = 0, 0, 0
        ticker.ticker, ticker.prices = '', []


def define_zero(ticker):
    if ticker[1] == 0.0:
        zero_volatility.append(ticker[0])
        min_volatility.remove(ticker)


def sort():
    global min_volatility, max_volatility, zero_volatility
    min_volatility = sorted(volatility_stat, key=lambda price: price[1])
    min_volatility = [el for el, _ in groupby(min_volatility)]
    max_volatility = sorted(volatility_stat, key=lambda price: price[1], reverse=True)
    for ticker in volatility_stat:
        define_zero(ticker)
    zero_volatility = sorted(zero_volatility)


def print_stat(max, min, zero):
    print('Max volatility: ')
    for value in max[:3]:
        print('   ' + str(value[0]) + ' - ' + str(value[1]))

    print('Min volatility: ')
    for value in min[:3]:
        print('   ' + str(value[0]) + ' - ' + str(value[1]))

    print('Zero volatility: ')
    print('  ', ', '.join(zero))


get_values()
sort()
print_stat(max=max_volatility,
           min=min_volatility,
           zero=zero_volatility)


# TODO тут ваш код в многопоточном стиле
