# -*- coding: utf-8 -*-


# Задача: вычислить 3 тикера с максимальной и 3 тикера с минимальной волатильностью в МНОГОПРОЦЕССНОМ стиле
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
# TODO Внимание! это задание можно выполнять только после зачета lesson_012/02_volatility_with_threads.py !!!

# TODO тут ваш код в многопроцессном стиле
import csv
import os
from collections import OrderedDict
from multiprocessing import Process, Queue
from queue import Empty


class TickerVolatility(Process):

    def __init__(self, file_path, tickers_queue):
        super().__init__()
        if os.path.exists(file_path):
            self.file_path = file_path
        else:
            raise FileExistsError('Каталог с файлами отсутствует')
        self.tickers_queue = tickers_queue

    def get_tickers_info_from_file(self):
        prices = []
        ticker = None
        with open(file=self.file_path, mode='r', encoding='utf8') as csv_file:
            csv_dict = csv.DictReader(csv_file, delimiter=',')
            for line in csv_dict:
                ticker = line['SECID']
                prices.append(float(line['PRICE']))
        return ticker, prices

    def run(self):
        try:
            self.calculate_volatility()
        except Exception as exc:
            print(f'Error - {self.name} - {exc}')

    def calculate_volatility(self):
        ticker, prices = self.get_tickers_info_from_file()
        max_price, min_price = max(prices), min(prices)
        average_price = (max_price + min_price) / 2
        volatility = ((max_price - min_price) / average_price) * 100
        self.tickers_queue.put((ticker, volatility))


def get_next_file(file_path):
    for dirpath, dirnames, filenames in os.walk(file_path):
        for filename in filenames:
            file_name = os.path.join(dirpath, filename)
            yield file_name


def print_report(tickers_dict):
    zero_tickers = {}
    tickers = {}
    for ticker, volatility in tickers_dict.items():
        if volatility == 0:
            zero_tickers[ticker] = volatility
        else:
            tickers[ticker] = volatility
    ordered_tickers = OrderedDict(sorted(tickers.items(), key=lambda x: x[1], reverse=True))
    tickers_list = list(ordered_tickers.keys())
    print('Максимальная волатильность:')
    for secid in tickers_list[:3]:
        print(f'\t{secid} - {ordered_tickers[secid]:2.2f} %')
    print('Минимальная волатильность:')
    for secid in tickers_list[-3:]:
        print(f'\t{secid} - {ordered_tickers[secid]:2.2f} %')
    print('Нулевая волатильность:')
    print('\t', ', '.join(sorted(zero_tickers.keys())), sep='')


def main(tickers_path):
    tickers = {}
    collector = Queue(maxsize=2)
    processes = [TickerVolatility(file_path=fname, tickers_queue=collector) for fname in get_next_file(tickers_path)]
    [process.start() for process in processes]
    while True:
        try:
            ticker, volatility = collector.get(timeout=1)
            tickers[ticker] = volatility
        except Empty:
            if not any(process.is_alive() for process in processes):
                break
    [process.join() for process in processes]
    print_report(tickers)


if __name__ == '__main__':
    TRADE_FILES = './trades'
    main(tickers_path=TRADE_FILES)
