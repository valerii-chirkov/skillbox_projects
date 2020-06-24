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

start_point_triangle = sd.get_point(10, 10)
start_point_square = sd.get_point(120, 10)
start_point_pentagon = sd.get_point(240, 10)
start_point_hexagon = sd.get_point(360, 10)
delta = 0
length = 100


def triangle(start_point, delta, length):
    shape_triangle_1 = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
    shape_triangle_1.draw()
    shape_triangle_2 = sd.get_vector(start_point=shape_triangle_1.end_point, angle=delta+120, length=length, width=2)
    shape_triangle_2.draw()
    shape_triangle_3 = sd.get_vector(start_point=shape_triangle_2.end_point, angle=delta+240, length=length, width=2)
    shape_triangle_3.draw()


def square(start_point, delta, length):
    shape_square_1 = sd.get_vector(start_point=start_point, angle=delta, length=length-10, width=2)
    shape_square_1.draw()
    shape_square_2 = sd.get_vector(start_point=shape_square_1.end_point, angle=delta+90, length=length-10, width=2)
    shape_square_2.draw()
    shape_square_3 = sd.get_vector(start_point=shape_square_2.end_point, angle=delta+180, length=length-10, width=2)
    shape_square_3.draw()
    shape_square_4 = sd.get_vector(start_point=shape_square_3.end_point, angle=delta+270, length=length-10, width=2)
    shape_square_4.draw()


def pentagon(start_point, delta, length):
    shape_pentagon_1 = sd.get_vector(start_point=start_point, angle=delta, length=length-40, width=2)
    shape_pentagon_1.draw()
    shape_pentagon_2 = sd.get_vector(start_point=shape_pentagon_1.end_point, angle=delta+72, length=length-40, width=2)
    shape_pentagon_2.draw()
    shape_pentagon_3 = sd.get_vector(start_point=shape_pentagon_2.end_point, angle=delta+144, length=length-40, width=2)
    shape_pentagon_3.draw()
    shape_pentagon_4 = sd.get_vector(start_point=shape_pentagon_3.end_point, angle=delta+216, length=length-40, width=2)
    shape_pentagon_4.draw()
    shape_pentagon_5 = sd.get_vector(start_point=shape_pentagon_4.end_point, angle=delta+288, length=length-40, width=2)
    shape_pentagon_5.draw()


def hexagon(start_point, delta, length):
    shape_hexagon_1 = sd.get_vector(start_point=start_point, angle=delta, length=length-45, width=2)
    shape_hexagon_1.draw()
    shape_hexagon_2 = sd.get_vector(start_point=shape_hexagon_1.end_point, angle=delta+60, length=length-45, width=2)
    shape_hexagon_2.draw()
    shape_hexagon_3 = sd.get_vector(start_point=shape_hexagon_2.end_point, angle=delta+120, length=length-45, width=2)
    shape_hexagon_3.draw()
    shape_hexagon_4 = sd.get_vector(start_point=shape_hexagon_3.end_point, angle=delta+180, length=length-45, width=2)
    shape_hexagon_4.draw()
    shape_hexagon_5 = sd.get_vector(start_point=shape_hexagon_4.end_point, angle=delta+240, length=length-45, width=2)
    shape_hexagon_5.draw()
    shape_hexagon_6 = sd.get_vector(start_point=shape_hexagon_5.end_point, angle=delta+300, length=length-45, width=2)
    shape_hexagon_6.draw()


triangle(start_point=start_point_triangle, delta=delta, length=length)
square(start_point=start_point_square, delta=delta, length=length)
pentagon(start_point=start_point_pentagon, delta=delta, length=length)
hexagon(start_point=start_point_hexagon, delta=delta, length=length)
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


sd.pause()
