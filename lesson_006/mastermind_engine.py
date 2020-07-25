# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint
random_number = ''


def guess_number():
    global random_number
    while False:
        random_number = randint(1000, 9999)
        if len(set(random_number)) == 4:
            print(random_number)  # Todo почему-то ничего не выводится, не могу понять логику работы, о которой вы пишете
            return True
        else:
            return False


guess_number()


def check_number():
    return {'bulls': '', 'cows': ''}
