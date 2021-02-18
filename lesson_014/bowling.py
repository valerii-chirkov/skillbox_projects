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

from lesson_014.custom_exceptions import ValidSymbolsError, TenFramesError, SlashFirstError, TenPointsFrameError
from lesson_014.custom_exceptions import OddEvenEqualityError, XAfterNumber
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


def check_equality(game_score):
    # amount_x counts both cyrillic and latin letters "X" (ex in Eng, ha in Rus) as well as capital and small ones.
    amount_x = game_score.count('X') + game_score.count('Х') + game_score.count('x') + game_score.count('х')
    amount_letters = len(game_score)

    # one should be True and one is False, otherwise the game_score is wrong
    even_number = amount_x % 2 == 0 and amount_letters % 2 == 0
    odd_number = amount_x % 2 != 0 and amount_letters % 2 != 0

    # the amount of X's and symbols in a string should be both either odd or even.
    if even_number or odd_number:
        return True


def check_symbols(game_score):
    # if statement is True, we should check for game_score containing valid values
    for char in game_score:
        if char not in POSSIBLE_SYMBOLS:
            raise ValidSymbolsError('There are some not acceptable symbols')
        else:
            return True


def check_length(game_score):
    amount_x = game_score.count('X') + game_score.count('Х') + game_score.count('x') + game_score.count('х')
    # if values are valid we remove "X" numbers, because they are already 20 points each
    game_score_no_x = game_score.translate({ord(i): None for i in 'XХxх'})
    split_by_two = [game_score_no_x[i:i + 2] for i in range(0, len(game_score_no_x), 2)]

    # for the case of more than 10 frames
    frame_length = len(split_by_two) + amount_x
    if frame_length > 10:
        raise TenFramesError('There are only 10 frames possible')
    else:
        return True


def check_slash_first(throw):
    if throw == '/':
        raise SlashFirstError('Slash symbol cannot be first in a frame')


def check_last_throw(index, max_index, throw):
    internal_points = 0
    if index == max_index:
        if throw in 'XxХх':
            internal_points += 10
        elif throw == '-':
            internal_points += 0
        else:
            internal_points += throw
        return internal_points


def check_penultimate_throw(index, max_index, throw, game_score):
    internal_points = 0
    if index == max_index - 1:
        next_throw1 = game_score[index + 1]
        if throw in '123456789':
            if next_throw1 == '/':
                internal_points += 10
            elif next_throw1 == '-':
                internal_points += int(throw)
            elif next_throw1 in '123456789':
                if int(throw) + int(next_throw1) >= 10:
                    raise TenPointsFrameError('There are more than 10 points in a frame')
                else:
                    internal_points += int(throw) + int(next_throw1)
            elif next_throw1 in 'XxХх':
                raise XAfterNumber('There cannot be X after a number in the end of the frames')
            else:
                raise ValidSymbolsError('There could be only / or - or a number')
        elif throw in 'XxХх':
            if next_throw1 in 'XxХх':
                internal_points += 30
            else:
                internal_points += 10 + next_throw1
        elif throw == '-':
            if next_throw1 == '-':
                internal_points += 0
            elif next_throw1 == '/':
                internal_points += 10
            elif next_throw1 in 'XxХх':
                raise XAfterNumber('There cannot be X after slash in the end of the frames')
            else:
                internal_points += int(next_throw1)
        else:
            internal_points += int(throw) + int(next_throw1)
        return internal_points


def check_throw_dash(throw, next_throw1):
    internal_points = 0
    if throw == '-':
        if next_throw1 == '-':
            internal_points += 0
        elif next_throw1 == '/':
            internal_points += 10
        elif next_throw1 in 'XxХх':
            raise XAfterNumber('There cannot be X after slash in the end of the frames')
        else:
            internal_points += int(next_throw1)


def check_xxx(throw, next_throw1, next_throw2):
    internal_points = 0
    if throw in 'XxХх':
        internal_points += 10
        if next_throw1 in 'XxХх':
            internal_points += 10
            if next_throw2 in 'XxХх':
                internal_points += 10
            elif next_throw2 == '-':
                internal_points += 0
            else:
                internal_points += int(next_throw2)
        elif (next_throw1 and next_throw2).count('/'):
            internal_points += 10
        elif next_throw1.count('-') and next_throw2.count('-'):
            internal_points += 0
        else:
            if (next_throw1 or next_throw2).count('-'):
                try:
                    internal_points += int(next_throw1)
                except ValueError:
                    internal_points += int(next_throw2)
            elif int(next_throw1) + int(next_throw2) >= 10:
                raise TenPointsFrameError('There are more than 10 points in a frame')
            else:
                internal_points += int(next_throw1) + int(next_throw2)
        return internal_points


def check_slash(next_throw1, next_throw2):
    internal_points = 0
    if next_throw1.count('/'):
        internal_points += 10
        if next_throw2 in 'XxХх':
            internal_points += 10
        elif next_throw2 == '-':
            internal_points += 0
        else:
            internal_points += int(next_throw2)
    return internal_points


def check_throw_with_next(next_throw1, throw):
    internal_points = 0
    if throw == '-' and next_throw1 == '-':
        internal_points += 0
    elif throw == '-' and next_throw1 in '123456789':
        internal_points += int(next_throw1)
    elif throw and next_throw1 in '123456789':
        internal_points += int(throw) + int(next_throw1)
    elif throw == '-':
        if next_throw1 == '-':
            internal_points += 0
        elif next_throw1 == '/':
            internal_points += 10
        elif next_throw1 in 'XxХх':
            raise XAfterNumber('There cannot be X after slash in the end of the frames')
        else:
            internal_points += int(next_throw1)
    elif next_throw1 == '-':
        internal_points += int(throw)
    elif next_throw1 in 'XxХх':
        raise OddEvenEqualityError('It is not possible to have X after a number')
    return internal_points


def get_score_american(game_score):
    points = 0
    index, max_index = 0, len(game_score) - 1

    # preparing for main loop, if there are any mistakes - the reason is syntax
    if check_equality(game_score) and check_symbols(game_score) and check_length(game_score):
        # the main loop, if there are any mistakes - the reason is representing of the score
        while index <= max_index:
            throw = game_score[index]
            check_slash_first(throw)
            if check_last_throw(index, max_index, throw):
                points += check_last_throw(index, max_index, throw)
                break
            elif check_penultimate_throw(index, max_index, throw, game_score):
                points += check_penultimate_throw(index, max_index, throw, game_score)
                break
            next_throw1 = game_score[index + 1]
            next_throw2 = game_score[index + 2]
            if check_xxx(throw, next_throw1, next_throw2):
                index += 1
                points += check_xxx(throw, next_throw1, next_throw2)
                continue
            if check_slash(next_throw1, next_throw2):
                index += 2
                points += check_slash(next_throw1, next_throw2)
                continue
            if check_throw_with_next(next_throw1, throw):
                index += 2
                points += check_throw_with_next(next_throw1, throw)
                continue

        return points
    else:
        raise OddEvenEqualityError('There are not appropriate quantity of numbers')

# print(get_score_rules(game_score='-9-9-9-9-9-9-7'))
# print(get_score_american(game_score='-9-9-9-9-9-9-7'))
