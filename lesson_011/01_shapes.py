# -*- coding: utf-8 -*-

import simple_draw as sd

# На основе вашего кода из решения lesson_004/01_shapes.py сделать функцию-фабрику,
# которая возвращает функции рисования треугольника, четырехугольника, пятиугольника и т.д.
#
# Функция рисования должна принимать параметры
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Функция-фабрика должна принимать параметр n - количество сторон.


def get_polygon(n):
    def draw_shape(point, angle, length):
        for delta in range(0, 360, 360//n):  # TODO Тут лучше не делить целочисленно, а округлять обычное деление
                                             #  функцией round
            function = sd.get_vector(start_point=point, angle=delta + angle, length=length)
            function.draw()
            # TODO 1) Нэйминг: что такое "функция"? Если уж быть точным, то get_vector возвращает объект класса Vector
            #  2) Если использовать функцию sd.vector то код будет короче, так как она сразу рисует и возвращает
            #  последнюю точку
            point = function.end_point
    return draw_shape
    # TODO Как можно видеть, фигура рисуется с разрывом, раз вы это не поправили в задаче 4, то пора сделать это сейчас


draw_triangle = get_polygon(n=6)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
