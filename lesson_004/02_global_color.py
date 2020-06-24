# -*- coding: utf-8 -*-
import simple_draw as sd

# Добавить цвет в функции рисования геом. фигур. из упр lesson_004/01_shapes.py
# (код функций скопировать сюда и изменить)
# Запросить у пользователя цвет фигуры посредством выбора из существующих:
#   вывести список всех цветов с номерами и ждать ввода номера желаемого цвета.
# Потом нарисовать все фигуры этим цветом

# Пригодятся функции
# sd.get_point()
# sd.line()
# sd.get_vector()
# и константы COLOR_RED, COLOR_ORANGE, COLOR_YELLOW, COLOR_GREEN, COLOR_CYAN, COLOR_BLUE, COLOR_PURPLE
# Результат решения см lesson_004/results/exercise_02_global_color.jpg
colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
start_point_triangle = sd.get_point(10, 10)
start_point_square = sd.get_point(120, 10)
start_point_pentagon = sd.get_point(240, 10)
start_point_hexagon = sd.get_point(360, 10)
delta = 0
length = 100
input_color = int(input('''Введите номер желаемого цвета:
                    0. Красный 
                    1. Оранжевый
                    2. Желтый
                    3. Зеленый
                    4. Циан
                    5. Синий
                    6. Фиолетовый
                    
                    '''))
if 0 <= input_color < 7:
    print('Вы ввели ', input_color)
    color = colors[input_color]
else:
    print('Вы ввели неверное число, поэтому мы нарисуем своим цветом')
    random_number = sd.random_number(0, 7)
    color = colors[random_number]


def triangle(start_point, delta, length):
    shape_triangle_1 = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
    shape_triangle_1.draw(color=color)
    shape_triangle_2 = sd.get_vector(start_point=shape_triangle_1.end_point, angle=delta+120, length=length, width=2)
    shape_triangle_2.draw(color=color)
    shape_triangle_3 = sd.get_vector(start_point=shape_triangle_2.end_point, angle=delta+240, length=length, width=2)
    shape_triangle_3.draw(color=color)


def square(start_point, delta, length):
    shape_square_1 = sd.get_vector(start_point=start_point, angle=delta, length=length-10, width=2)
    shape_square_1.draw(color=color)
    shape_square_2 = sd.get_vector(start_point=shape_square_1.end_point, angle=delta+90, length=length-10, width=2)
    shape_square_2.draw(color=color)
    shape_square_3 = sd.get_vector(start_point=shape_square_2.end_point, angle=delta+180, length=length-10, width=2)
    shape_square_3.draw(color=color)
    shape_square_4 = sd.get_vector(start_point=shape_square_3.end_point, angle=delta+270, length=length-10, width=2)
    shape_square_4.draw(color=color)


def pentagon(start_point, delta, length):
    shape_pentagon_1 = sd.get_vector(start_point=start_point, angle=delta, length=length-40, width=2)
    shape_pentagon_1.draw(color=color)
    shape_pentagon_2 = sd.get_vector(start_point=shape_pentagon_1.end_point, angle=delta+72, length=length-40, width=2)
    shape_pentagon_2.draw(color=color)
    shape_pentagon_3 = sd.get_vector(start_point=shape_pentagon_2.end_point, angle=delta+144, length=length-40, width=2)
    shape_pentagon_3.draw(color=color)
    shape_pentagon_4 = sd.get_vector(start_point=shape_pentagon_3.end_point, angle=delta+216, length=length-40, width=2)
    shape_pentagon_4.draw(color=color)
    shape_pentagon_5 = sd.get_vector(start_point=shape_pentagon_4.end_point, angle=delta+288, length=length-40, width=2)
    shape_pentagon_5.draw(color=color)


def hexagon(start_point, delta, length):
    shape_hexagon_1 = sd.get_vector(start_point=start_point, angle=delta, length=length-45, width=2)
    shape_hexagon_1.draw(color=color)
    shape_hexagon_2 = sd.get_vector(start_point=shape_hexagon_1.end_point, angle=delta+60, length=length-45, width=2)
    shape_hexagon_2.draw(color=color)
    shape_hexagon_3 = sd.get_vector(start_point=shape_hexagon_2.end_point, angle=delta+120, length=length-45, width=2)
    shape_hexagon_3.draw(color=color)
    shape_hexagon_4 = sd.get_vector(start_point=shape_hexagon_3.end_point, angle=delta+180, length=length-45, width=2)
    shape_hexagon_4.draw(color=color)
    shape_hexagon_5 = sd.get_vector(start_point=shape_hexagon_4.end_point, angle=delta+240, length=length-45, width=2)
    shape_hexagon_5.draw(color=color)
    shape_hexagon_6 = sd.get_vector(start_point=shape_hexagon_5.end_point, angle=delta+300, length=length-45, width=2)
    shape_hexagon_6.draw(color=color)


triangle(start_point=start_point_triangle, delta=delta, length=length)
square(start_point=start_point_square, delta=delta, length=length)
pentagon(start_point=start_point_pentagon, delta=delta, length=length)
hexagon(start_point=start_point_hexagon, delta=delta, length=length)

sd.pause()
