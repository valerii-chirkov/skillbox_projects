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

from lesson_014.custom_exceptions import *  # TODO Это не хорошая практика, явно импортируйте только используемые
                                            #  объекты
POSSIBLE_SYMBOLS = '123456789-/XХxх'


def get_score(game_score):
    points = 0
    # amount_x counts both cyrillic and latin letters "X" (ex in Eng, ha in Rus) as well as capital and small ones.
    amount_x = game_score.count('X') + game_score.count('Х') + game_score.count('x') + game_score.count('х')
    amount_letters = len(game_score)

    even_number = amount_x % 2 == 0 and amount_letters % 2 == 0
    odd_number = amount_x % 2 != 0 and amount_letters % 2 != 0

    # the amount of X's and symbols in a string should be both either odd or even.
    if even_number or odd_number:
        # if statement is True, we should check for game_score containing valid values
        for char in game_score:
            if char not in POSSIBLE_SYMBOLS:
                raise ValidSymbolsError('There are some not acceptable symbols')

        # if values are valid we remove "X" numbers, because they are already 20 points each
        game_score = game_score.translate({ord(i): None for i in 'XХxх'})
        split_by_two = [game_score[i:i + 2] for i in range(0, len(game_score), 2)]

        # for the case of more than 10 frames
        frame_length = len(split_by_two) + amount_x
        if frame_length > 10:
            raise TenFramesError('There are only 10 frames possible')

        points += 20 * amount_x

        # then we split our row for pairs and check them for possible TypeErrors
        for frame in split_by_two:
            if frame.count('/'):
                if frame[0] == '/':
                    raise SlashFirstError('Slash symbol cannot be first')
                else:
                    points += 15
            elif frame.count('-'):
                frame = frame.translate({ord(i): None for i in '-'})
                # in the case of '1234XХ-135--'
                if frame == '':
                    pass
                else:
                    points += int(frame)
            else:
                two_numbers = int(frame[0]) + int(frame[1])
                if two_numbers >= 10:
                    raise TenPointsFrameError('There are more than 10 points in a frame')
                points += int(frame[0]) + int(frame[1])
        return points
    else:
        raise OddEvenEqualityError('There are not appropriate quantity of numbers')


# print(get_score('1234XХ-135'))
