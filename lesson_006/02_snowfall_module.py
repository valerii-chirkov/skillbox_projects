# -*- coding: utf-8 -*-

import simple_draw as sd
from lesson_006.snowfall import *
# На основе кода из lesson_004/05_snowfall.py
# сделать модуль snowfall.py в котором реализовать следующие функции
#  создать_снежинки(N) - создает N снежинок
#  нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
#  сдвинуть_снежинки() - сдвигает снежинки на один шаг
#  номера_достигших_низа_экрана() - выдает список номеров снежинок, которые вышли за границу экрана
#  удалить_снежинки(номера) - удаляет снежинки с номерами из списка
# снежинки хранить в глобальных переменных модуля snowfall
#
# В текущем модуле реализовать главный цикл падения снежинок,
# обращаясь ТОЛЬКО к функциям модуля snowfall

# создать_снежинки(N)
snowflakes_create()
while True:
    sd.start_drawing()
    snowflakes_draw(color=sd.background_color)
    snowflakes_shift()  # сдвинуть_снежинки()
    snowflakes_draw(color=sd.COLOR_WHITE)
    if snowflakes_numbers_out():  # если есть номера_достигших_низа_экрана() то
        snowflakes_delete()  # удалить_снежинки(номера)
        snowflakes_create()  # создать_снежинки(count)
    sd.sleep(0.1)
    sd.finish_drawing()
    if sd.user_want_exit():
        break

sd.pause()
