# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint
from termcolor import cprint
random_number = ''
# TODO Бесконечные циклы убрал


def check_user_number_api(user_number):
    check_conditions = [
        user_number.isdigit(),
        len(user_number) == 4,
        user_number[0] != 0,
        len(set(user_number)) == 4,
    ]

    if all(check_conditions):
        comparison(user_number)
        return True
    else:
        return False


def guess_number():
    global random_number
    random_number = str(randint(1000, 9999))
    if len(set(random_number)) == 4:
        print(random_number)
        return False


def comparison(user_number):
    stats = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if user_number[i] == random_number[i]:
            stats['bulls'] += 1
        else:
            if random_number.count(user_number[i]):
                stats['cows'] += 1
    return stats
