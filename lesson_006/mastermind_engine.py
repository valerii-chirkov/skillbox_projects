# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.

from random import shuffle
# from lesson_006.mastermind import user_number
from termcolor import colored
_game_number = ''
user_number = '1234'


def random_number():
    # TODO не придумал лучшего алгоритма, пока что так
    global _game_number
    get_ten_digits = list(range(0, 10))
    shuffle(get_ten_digits)
    for i in range(4):
        _game_number += str(get_ten_digits[i])
        if _game_number[0] == '0':
            _game_number = _game_number.replace('0', str(get_ten_digits[5]))
    return _game_number


def guess_number():
    if (len(set(user_number)) == 4) & (len(user_number) == 4):
        return user_number
    else:
        print(colored('Вы ввели неверное число', 'red'))
    check_number()


def check_number():
    stats = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if user_number[i] == _game_number[i]:
            stats['bulls'] += 1
        else:
            if _game_number.__contains__(user_number[i]):
                stats['cows'] += 1
    return stats


# TODO Я не совсем понимаю как можно функцию guess_number разделить на две - одну с выводом, а другую с логикой
