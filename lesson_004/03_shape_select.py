# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg

delta = 0
length = 100


def triangle(start_point=sd.get_point(250, 250), *, delta, length):
    for delta in range(0, 251, 120):
        shape_triangle = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_triangle.draw()
        start_point = shape_triangle.end_point


def square(start_point=sd.get_point(250, 250), *, delta, length):
    for delta in range(0, 351, 90):
        shape_square = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_square.draw()
        start_point = shape_square.end_point


def pentagon(start_point=sd.get_point(250, 250), *, delta, length):
    for delta in range(0, 289, 72):
        shape_pentagon = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_pentagon.draw()
        start_point = shape_pentagon.end_point


def hexagon(start_point=sd.get_point(250, 200), *, delta, length):
    for delta in range(0, 301, 60):
        shape_hexagon = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_hexagon.draw()
        start_point = shape_hexagon.end_point


shapes_dict = {'0': ['0. Треугольник', triangle],
               '1': ['1. Квадрат', square],
               '2': ['2. Пятиугольник', pentagon],
               '3': ['3. Шестиугольник', hexagon]}

for i in range(len(shapes_dict)):
    print(shapes_dict[str(i)][0])

input_shape = input('Введите номер желаемой фигуры: ')

if input_shape in shapes_dict:
    print('Вы ввели ', input_shape)
    shapes_dict[input_shape][1](delta=delta, length=length)
else:
    print('Вы ввели неверное число')
    sd.pause()
sd.pause()

