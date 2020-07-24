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


def random_number():
    global _game_number
    # TODO Можно упростить заводим бесконечный цикл
    # TODO _game_number присваиваем строку в которой randint(1000, 9999)
    # TODO Потом проверяем если set этой строки без дублей, (можно прочекать длину)
    # TODO то выходим из цикла
    # TODO и возвращаем нужный нам результат
    get_ten_digits = list(range(0, 10))
    shuffle(get_ten_digits)
    for i in range(4):
        _game_number += str(get_ten_digits[i])
        if _game_number[0] == '0':
            _game_number = _game_number.replace('0', str(get_ten_digits[5]))
    print(_game_number)
    return _game_number


# TODO если тут поставить счетчик то наглядно видно как рекурсия выдает ошибку на 997 вызове!

# TODO Эта функция у нас только чекает правильность ввода, в главном файле пишем функцию
# TODO которая отвечает за основную логику
def guess_number(user_number):
    if (len(set(user_number)) == 4) & (len(user_number) == 4):
        # TODO тут мы возвращаем не число а True
        return user_number
    else:
        # TODO по аналогии тут возвращается False, никаких принтов и рекурсий тут не пишем
        print(colored('Вы ввели неверное число', 'red'))
        guess_number(user_number)
# TODO Обрабатываем так в главном файле
# TODO if guess_number(user_number):
# TODO     делаем какие то действия
# TODO     break - выход из цикла
# TODO else:
# TODO     print(colored('Вы ввели неверное число', 'red'))
# TODO и все выше мы можем поместить в бесконечный цикл и выходить из него по TRUE


def check_number(user_number):
    stats = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if user_number[i] == _game_number[i]:
            stats['bulls'] += 1
        else:
            # TODO используйте метод .сount
            if _game_number.__contains__(user_number[i]):
                stats['cows'] += 1
    return stats



