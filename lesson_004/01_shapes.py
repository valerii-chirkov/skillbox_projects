# -*- coding: utf-8 -*-

import simple_draw as sd

# Часть 1.
# Написать функции рисования равносторонних геометрических фигур:
# - треугольника
# - квадрата
# - пятиугольника
# - шестиугольника
# Все функции должны принимать 3 параметра:
# - точка начала рисования
# - угол наклона
# - длина стороны
#
# Примерный алгоритм внутри функции:
#   # будем рисовать с помощью векторов, каждый следующий - из конечной точки предыдущего
#   текущая_точка = начальная точка
#   для угол_наклона из диапазона от 0 до 360 с шагом XXX
#      # XXX подбирается индивидуально для каждой фигуры
#      составляем вектор из текущая_точка заданной длины с наклоном в угол_наклона
#      рисуем вектор
#      текущая_точка = конечной точке вектора
#
# Использование копи-пасты - обязательно! Даже тем кто уже знает про её пагубность. Для тренировки.
# Как работает копипаста:
#   - одну функцию написали,
#   - копипастим её, меняем название, чуть подправляем код,
#   - копипастим её, меняем название, чуть подправляем код,
#   - и так далее.
# В итоге должен получиться ПОЧТИ одинаковый код в каждой функции

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# sd.line()
# Результат решения см lesson_004/results/exercise_01_shapes.jpg

# start_point_triangle = sd.get_point(100, 100)
# start_point_square = sd.get_point(400, 100)
# start_point_pentagon = sd.get_point(100, 350)
# start_point_hexagon = sd.get_point(400, 350)
# delta = 0
# length = 100
# incline = 20
#
#
# def triangle(start_point, length):
#     for delta in range(incline, incline + 251, 120):
#         shape_triangle = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
#         shape_triangle.draw()
#         start_point = shape_triangle.end_point
#
#
# def square(start_point, length):
#     for delta in range(incline, incline + 351, 90):
#         shape_square = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
#         shape_square.draw()
#         start_point = shape_square.end_point
#
#
# def pentagon(start_point, length):
#     for delta in range(incline, incline + 289, 72):
#         shape_pentagon = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
#         shape_pentagon.draw()
#         start_point = shape_pentagon.end_point
#
#
# def hexagon(start_point, length):
#     for delta in range(incline, incline + 301, 60):
#         shape_hexagon = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
#         shape_hexagon.draw()
#         start_point = shape_hexagon.end_point
#
#
# triangle(start_point=start_point_triangle, length=length)
# square(start_point=start_point_square, length=length)
# pentagon(start_point=start_point_pentagon, length=length)
# hexagon(start_point=start_point_hexagon, length=length)

# первая часть зачет!

# Часть 1-бис.
# Попробуйте прикинуть обьем работы, если нужно будет внести изменения в этот код.
# Скажем, связывать точки не линиями, а дугами. Или двойными линиями. Или рисовать круги в угловых точках. Или...
# А если таких функций не 4, а 44? Код писать не нужно, просто представь объем работы... и запомни это.

# Часть 2 (делается после зачета первой части)
#
# Надо сформировать функцию, параметризированную в местах где была "небольшая правка".
# Это называется "Выделить общую часть алгоритма в отдельную функцию"
# Потом надо изменить функции рисования конкретных фигур - вызывать общую функцию вместо "почти" одинакового кода.
#
# В итоге должно получиться:
#   - одна общая функция со множеством параметров,
#   - все функции отрисовки треугольника/квадрата/етс берут 3 параметра и внутри себя ВЫЗЫВАЮТ общую функцию.
#
# Не забудте в этой общей функции придумать, как устранить разрыв в начальной/конечной точках рисуемой фигуры
# (если он есть. подсказка - на последней итерации можно использовать линию от первой точки)

# Часть 2-бис.
# А теперь - сколько надо работы что бы внести изменения в код? Выгода на лицо :)
# Поэтому среди программистов есть принцип D.R.Y. https://clck.ru/GEsA9
# Будьте ленивыми, не используйте копи-пасту!


delta = 0
incline = 20


def triangle():
    incline_last = incline + 251
    step = 120
    start_point = sd.get_point(100, 100)
    shapes(start_point=start_point, incline_last=incline_last, step=step)


def square():
    incline_last = incline + 351
    step = 90
    start_point = sd.get_point(400, 100)
    shapes(start_point=start_point, incline_last=incline_last, step=step)


def pentagon():
    incline_last = incline + 289
    step = 72
    start_point = sd.get_point(100, 350)
    shapes(start_point=start_point, incline_last=incline_last, step=step)


def hexagon():
    incline_last = incline + 301
    step = 60
    start_point = sd.get_point(400, 350)
    shapes(start_point=start_point, incline_last=incline_last, step=step)


def shapes(start_point, incline_last, step):
    for delta in range(incline, incline_last, step):
        function = sd.get_vector(start_point=start_point, angle=delta, length=100, width=2)
        function.draw()
        start_point = function.end_point


def call():
    triangle()
    square()
    pentagon()
    hexagon()
    sd.pause()


call()
