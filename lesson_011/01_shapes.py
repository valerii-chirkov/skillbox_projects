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
        for delta in range(0, 360 + step, step):  #  не знаю, подойдет такой вариант или нет - OK, только уберите лишнюю
            # сторону (+ step). А исправить несовпадение первой и последней точек надо другим способом - в цикле
            # рисовать на одну cторону меньше, а после цикла рисовать линию (sd.line) между первой и последней точками
            # vec = sd.vector(start=point, angle=delta + angle, length=length)  #  долго пытался вызвать им, но
            # он рисовал 'звездочку', тк end_point почему-то не возвращал
            # TODO sd.vector возвращает именно крайнюю точку, только её надо брать сразу, а не пытаться искать атрибуты:
            #  point = sd.vector...
            v = sd.Vector(start_point=point, direction=delta+angle, length=length)  # todo смысла менять get_vector на Vector нет
            v.draw()
            point = v.end_point
    return draw_shape


draw_triangle = get_polygon(n=5)
draw_triangle(point=sd.get_point(200, 200), angle=13, length=100)

sd.pause()
