# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg


def triangle(start_point=sd.get_point(250, 250), delta=0, length=100):
    for _ in range(3):
        shape_triangle = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_triangle.draw(color=sd.COLOR_RED)
        delta += 120
        start_point = shape_triangle.end_point


def square(start_point=sd.get_point(250, 250), delta=0, length=100):
    for _ in range(4):
        shape_square = sd.get_vector(start_point=start_point, angle=delta, length=length-10, width=2)
        shape_square.draw(color=sd.COLOR_RED)
        delta += 90
        start_point = shape_square.end_point


def pentagon(start_point=sd.get_point(270, 270), delta=0, length=100):
    for _ in range(5):
        shape_pentagon = sd.get_vector(start_point=start_point, angle=delta, length=length-40, width=2)
        shape_pentagon.draw(color=sd.COLOR_RED)
        delta += 72
        start_point = shape_pentagon.end_point


def hexagon(start_point=sd.get_point(270, 270), delta=0, length=100):
    for _ in range(6):
        shape_hexagon = sd.get_vector(start_point=start_point, angle=delta, length=length-45, width=2)
        shape_hexagon.draw(color=sd.COLOR_RED)
        delta += 60
        start_point = shape_hexagon.end_point


input_shape = input('''Введите номер желаемой фигуры:
                    1. Треугольник
                    2. Квадрат
                    3. Пятиугольник
                    4. Шестиугольник

                    ''')

funcs = {'1': triangle, '2': square, '3': pentagon, '4': hexagon}

if input_shape in funcs:
    funcs[input_shape]()
else:
    print('Вы ввели неправильное число')
    sd.pause()

sd.pause()

