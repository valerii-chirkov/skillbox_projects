# Составить отдельный модуль mastermind_engine, реализующий функциональность игры.
# В mastermind_engine нужно реализовать функции:
#   загадать_число()
#   проверить_число(NN) - возвращает словарь {'bulls': N, 'cows': N}
# Загаданное число хранить в глобальной переменной.
# Обратите внимание, что строки - это список символов.
from random import randint
random_number = ''

# TODO Главный принцип функций чтобы они выполняли что то одно, лаконичные действия!
# TODO Заведем еще одну переменную число_пользователя в глобальном скоупе!


# TODO По названию функции у нас она чекает число, а не сравнивает результаты
def check_user_number_api(user_number):
    check_conditions = [
        user_number.isdigit(),
        len(user_number) == 4,
        user_number[0] != 0,
        len(set(user_number)) == 4,
    ]

    if all(check_conditions):
        # TODO тут мы не будем вызывать comparison, а присвоим число_пользователя = user_number
        comparison(user_number)
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


# TODO эта функция не будет получать user_number, а будет работать с глобальной переменной число_пользователя
# TODO которую мы получили ранее в check_user_number_api
def comparison(user_number):
    stats = {'bulls': 0, 'cows': 0}
    for i in range(4):
        if user_number[i] == random_number[i]:
            stats['bulls'] += 1
        else:
            if random_number.count(user_number[i]):
                stats['cows'] += 1
    return stats

# TODO можно сюда дописать метод проверки на выигрыш!
# TODO Проверив число_пользователя == random_number и так же возвращать булево значение!

# TODO после всех этих изменений движок готов! Работаем только с главный файлом.
