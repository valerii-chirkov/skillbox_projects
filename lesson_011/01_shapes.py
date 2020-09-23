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
        for delta in range(0, 360 + round(360/n), round(360/n)):  # TODO не знаю, подойдет такой вариант или нет
            # vec = sd.vector(start=point, angle=delta + angle, length=length)  # TODO долго пытался вызвать им, но
            # он рисовал 'звездочку', тк end_point почему-то не возвращал
            v = sd.Vector(start_point=point, direction=delta+angle, length=length)
            v.draw()
            point = v.end_point
    return draw_shape


draw_triangle = get_polygon(n=5)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
