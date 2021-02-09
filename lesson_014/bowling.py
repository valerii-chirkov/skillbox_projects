# -*- coding: utf-8 -*-

# Вас взяли на работу в молодой стартап. Идея стартапа - предоставлять сервис расчета результатов игр.
# Начать решили с боулинга, упрощенной версии.
#
# Правила такие.
#
# Всего 10 кеглей. Игра состоит из 10 фреймов. В одном фрейме до 2х бросков, цель - сбить все кегли.
# Результаты фрейма записываются символами:
#   «Х» – «strike», все 10 кеглей сбиты первым броском
#   «<число>/», например «4/» - «spare», в первый бросок сбиты 4 кегли, во второй – остальные
#   «<число><число>», например, «34» – в первый бросок сбито 3, во второй – 4 кегли.
#   вместо <число> может стоять прочерк «-», например «-4» - ни одной кегли не было сбито за первый бросок
# Результат игры – строка с записью результатов фреймов. Символов-разделителей между фреймами нет.
# Например, для игры из 4 фреймов запись результатов может выглядеть так:
#   «Х4/34-4»
# Предлагается упрощенный способ подсчета количества очков:
#   «Х» – strike всегда 20 очков
#   «4/» - spare всегда 15 очков
#   «34» – сумма 3+4=7
#   «-4» - сумма 0+4=4
# То есть для игры «Х4/34-4» сумма очков равна 20+15+7+4=46
#
# Надо написать python-модуль (назвать bowling), предоставляющий API расчета количества очков:
# функцию get_score, принимающую параметр game_result. Функция должна выбрасывать исключения,
# когда game_result содержит некорректные данные. Использовать стандартные исключения по максимуму,
# если не хватает - создать свои.

import logging

possible_symbols = '123456789-/XХ'
points = 0


def check_input(game_score):
    # amount_x counts both cyrillic and latin letters "X" (ex in Eng, ha in Rus)
    amount_x = game_score.count('X') + game_score.count('Х')
    amount_letters = len(game_score)

    # the amount of X's and symbols in a string should be both either odd or even.
    try:
        if (amount_x % 2 == 0 and amount_letters % 2 == 0) or (amount_x % 2 != 0 and amount_letters % 2 != 0):
            # if statement is True, we should check for game_score containing valid values
            for char in game_score:
                if char not in possible_symbols:
                    raise TypeError('There are some not acceptable symbols')

            game_score = game_score.translate({ord(i): None for i in 'XХ'})
            split_by_two = [game_score[i:i + 2] for i in range(0, len(game_score), 2)]
            check_frames(split_by_two, amount_x)

        else:
            raise ValueError('There is not acceptable value of points in flames')
    except (ValueError, TypeError):
        return False


def check_frames(split_by_two, amount_x):
    global points
    points += 20 * amount_x

    for frame in split_by_two:
        if frame.count('/'):
            if frame.count('0'):
                raise ValueError('For type \"0\" use \"-\"')
            points += 15
        elif frame.count('-'):
            if frame.count('0'):
                raise ValueError('For type \"0\" use \"-\"')
            frame = frame.translate({ord(i): None for i in '-'})
            points += int(frame)
        elif frame.count('0'):
            raise ValueError('For type \"0\" use \"-\"')
        elif frame[0] == '/':
            raise ValueError('Slash symbol cannot be first')
        else:
            two_numbers = int(frame[0]) + int(frame[1])
            if two_numbers >= 10:
                raise ValueError
            points += int(frame[0]) + int(frame[1])
    return points


def get_score(game_score):
    if check_input(game_score) is False:
        raise Exception
    else:
        return points
