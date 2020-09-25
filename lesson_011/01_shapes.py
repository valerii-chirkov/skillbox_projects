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
        step = round(360 / n)
        start_point = point  # TODO можно обойтись без этого и вызвать дефолтное значение?
        for delta in range(0, 360 - step, step):
            vector = sd.vector(start=point, angle=delta+angle, length=length)
            point = vector
        sd.line(start_point, point)  # sd.line(sd.get_point(200, 200), point)  # TODO так ведь не расширяемо?

    return draw_shape


draw_triangle = get_polygon(n=5)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
