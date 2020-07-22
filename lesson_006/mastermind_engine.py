# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.

import random
from termcolor import colored
_game_number = ''
user_number = ''
level_of_game = int(input('Сколько чисел угадываем?: '))
# def level():
#     level_of_game = int(input('Сколько чисел угадываем?: '))
#     if level_of_game == 0:
#         print('Слишком просто, давайте больше!')
#         level()
#     if level_of_game > 10:
#         print('Слишком долго, давайте меньше! ')
#         level()
# TODO не знаю как сделать так, чтобы level_of_game работал в других функциях, через level() не работает,
# TODO если в глобальную область пишу сначала level_of_game = 0, а потом определяю в функции, то он так и остается ноль

# TODO проверку на правильность ввода (string, float, char и тд) пока не делал, сделаю после вашего одобрения алгоритма


def random_number():
    get_ten_digits = list(range(0, 10))
    random.shuffle(get_ten_digits)
    global _game_number

    for i in range(level_of_game):
        _game_number += str(get_ten_digits[i])
    # print(_game_number)
    # для отладки раскоментировать


def guess_number():
    global user_number
    user_number = input(colored("Введите число: ", color='yellow'))

    # Тут мы делаем проверку на длину, и на повтор чисел
    if (len(set(user_number)) == level_of_game) & (len(user_number) == level_of_game):
        return user_number
    else:
        print(colored('Вы ввели неверное число', 'red'))
        guess_number()


def check_number():
    set_game_number = set(_game_number)
    set_user_number = set(user_number)

    list_game_number = list(_game_number)
    list_user_number = list(user_number)

    bulls_quantity = 0
    cows_quantity = 0
    bull_numbers = []

    # Узнаем потенциальных коров
    for i in range(1, level_of_game + 1):
        if len(set_game_number.intersection(set_user_number)) == i:
            cows_quantity += i

    # Узнаем количество быков
    for i in range(level_of_game):
        if list_game_number[i] == list_user_number[i]:
            bulls_quantity += 1
            bull_numbers += list_game_number[i]

    # Быки в приоритете, поэтому вычитаем из cows_quantity быков.
    set_intersection = set_game_number.intersection(set_user_number)
    extra_cows = len(set_intersection.intersection(set(bull_numbers)))
    cows_quantity -= extra_cows
    return {'bulls': bulls_quantity, 'cows': cows_quantity}
