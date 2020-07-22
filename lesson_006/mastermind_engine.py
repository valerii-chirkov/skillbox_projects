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

# TODO в этом модуле у нас только логика, никаких сообщений и ввода, все общение выносим в главный модуль!

# TODO по заданию Компьютер загадывает четырехзначное число, все цифры которого различны 1000 - 9999

level_of_game = int(input('Сколько чисел угадываем?: '))

# def level():
#     level_of_game = int(input('Сколько чисел угадываем?: '))
#     if level_of_game == 0:
#         print('Слишком просто, давайте больше!')
#         level()
#     if level_of_game > 10:
#         print('Слишком долго, давайте меньше! ')
#         level()
# TODO использование рекурсий не самый лучший вариант level()! Потому что в питоне по дефолту всего можно запустить
#  около 1000 рекурсий потом код упадет!

# TODO global level_of_game в начале, чтобы функция знала что мы используем глобальную переменную

# TODO проверку на правильность ввода (string, float, char и тд) пока не делал: Хорошо используйте .isdigit()


def random_number():
    # TODO пока что будет делать как по заданию, имеем ввиду что у нас 4 цифры
    # TODO первая из которых не может быть 0
    # TODO и не должно быть повторений

    get_ten_digits = list(range(0, 10))
    random.shuffle(get_ten_digits)
    # TODO определяется в начале функции
    global _game_number

    for i in range(level_of_game):
        _game_number += str(get_ten_digits[i])
    # print(_game_number)
    # для отладки раскоментировать


# TODO тут мы пишем логику для проверки числа у пользователя!
# TODO добавим проверку на число, на первый 0, на повторение, и на количество!

# TODO Саму эту функцию вынесем общения вынесем в главный файл
def guess_number():
    global user_number
    user_number = input(colored("Введите число: ", color='yellow'))

    # Тут мы делаем проверку на длину, и на повтор чисел
    if (len(set(user_number)) == level_of_game) & (len(user_number) == level_of_game):
        return user_number
    else:
        print(colored('Вы ввели неверное число', 'red'))
        # TODO использовать рекурсии плохой стиль, в младших модулях мы их проходили для того чтобы познакомиться
        guess_number()


def check_number():
    # TODO как то переусложненно! Можно упростить вот таким алгоритмом
    # TODO создаем словарик с нулевыми показателями как у вас в ретурне к примеру
    # TODO заводим цикл по range(4)
    # TODO     если число_пользователя[индекс] = число_робота[индекс]
    # TODO         в словарь по быкам увеличиваем на +1
    # TODO     иначе
    # TODO         если число_робота.содержит(число_пользователя[индекс])
    # TODO             в словарь по коровам увеличиваем на +1
    # TODO И ретурном возвращаем словарь

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
