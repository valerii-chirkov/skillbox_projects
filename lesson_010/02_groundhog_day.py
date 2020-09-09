# -*- coding: utf-8 -*-

# День сурка
#
# Напишите функцию one_day() которая возвращает количество кармы от 1 до 7
# и может выкидывать исключения:
# - IamGodError
# - DrunkError
# - CarCrashError
# - GluttonyError
# - DepressionError
# - SuicideError
# Одно из этих исключений выбрасывается с вероятностью 1 к 13 каждый день
#
# Функцию оберните в бесконечный цикл, выход из которого возможен только при накоплении
# кармы до уровня ENLIGHTENMENT_CARMA_LEVEL. Исключения обработать и записать в лог.
# При создании собственных исключений максимально использовать функциональность
# базовых встроенных исключений.
from random import randint
ENLIGHTENMENT_CARMA_LEVEL = 777
total_carma = 0


class IamGodError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class SuicideError(Exception):
    pass


def one_day():
    exceptions = [IamGodError('I am god'), DrunkError('I am drunk'), CarCrashError('I am crushed'),
                  GluttonyError('I am glutton'), DepressionError('I am in depression'), SuicideError('I did suicide'), ]
    dice_exc = randint(0, len(exceptions)-1)
    exception = exceptions[dice_exc]
    global total_carma
    dice = randint(1, 13)
    if dice == 13:
        raise exception

    total_carma += randint(1, 7)
    print(total_carma)


while True:
    try:
        one_day()
    except Exception as ex:
        print(ex)
        continue
    if total_carma >= ENLIGHTENMENT_CARMA_LEVEL:
        print(f'Вышел из цикла с кармой {total_carma}')
        break

# зачет!
