# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint
random_number = ''
user_global = ''


def conditions(user_number):
    global user_global
    check_conditions = [
        user_number.isdigit(),
        len(user_number) == 4,
        # поправил вот тут, так как проверка числа а не строки
        # TODO я убрал int, потому что если ввели строку - то программа падает
        user_number[0] != 0,
        len(set(user_number)) == 4,
    ]
    if all(check_conditions):
        user_global = user_number
        return True
    else:
        return False


# тут бесконечный цикл нужен! для проверки. Функция будет возвращать число!
def guess_number():
    global random_number
    while True:
        random_number = str(randint(1000, 9999))
        if len(set(random_number)) == 4:
            print(f'Число которое загадали - {random_number}')
            break
    return random_number


def comparison():
    # А здесь мы используем глобальную переменную
    global user_global
    stats = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if user_global[i] == random_number[i]:
            stats['bulls'] += 1
        else:
            if random_number.count(user_global[i]):
                stats['cows'] += 1
    return stats


def win():
    global user_global
    # можно упростить сразу вот так:
    return user_global == random_number

