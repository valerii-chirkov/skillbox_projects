# -*- coding: utf-8 -*-

import simple_draw as sd
from snowfall import snowflakes_create, snowflakes_delete, snowflakes_shift, snowflakes_draw, snowflakes_numbers_out
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
N = int(input('Введите количество снежинок: '))
snowflakes_create(N)
while True:
    sd.start_drawing()
    snowflakes_draw(color=sd.background_color)
    snowflakes_shift()  # сдвинуть_снежинки()
    snowflakes_draw(color=sd.COLOR_WHITE)
    snowflakes_out = snowflakes_numbers_out()
    if snowflakes_out:
        snowflakes_delete(snowflakes_out)  # удалить_снежинки(номера)
        snowflakes_create(len(snowflakes_out))  # создать_снежинки(count)
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# зачет!
