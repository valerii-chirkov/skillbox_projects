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
    # TODO если код запустить он у вас даше в цикл не заходит потому что цикл не может быть FALSE
    while False:
        random_number = randint(1000, 9999)
        # TODO И даже если мы зайдем, то random_number:int и мы не можем применить к нему set
        if len(set(random_number)) == 4:
            print(random_number)
            # TODO а тут должен быть break
            return True
        else:
            return False
    # TODO эта функция должна возвращать число в виде строки


# TODO Мне кажется у вас нормально было написано, и только нужно было его доработать, код!

guess_number()


def check_number():
    return {'bulls': '', 'cows': ''}
