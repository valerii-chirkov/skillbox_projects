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


start_point_triangle = sd.get_point(100, 100)
start_point_square = sd.get_point(400, 100)
start_point_pentagon = sd.get_point(100, 350)
start_point_hexagon = sd.get_point(400, 350)
delta = 0
length = 100
incline = 20


def triangle(start_point, delta, length):
    for delta in range(incline, incline + 251, 120):
        shape_triangle = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_triangle.draw(color=color)
        delta += 120  # Тогда эта строка нам не понадобистя
        start_point = shape_triangle.end_point


def square(start_point, delta, length):
    for delta in range(incline, incline + 351, 90):
        shape_square = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_square.draw(color=color)
        start_point = shape_square.end_point


def pentagon(start_point, delta, length):
    for delta in range(incline, incline + 289, 72):
        shape_pentagon = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_pentagon.draw(color=color)
        delta += 72
        start_point = shape_pentagon.end_point


def hexagon(start_point, delta, length):
    for delta in range(incline, incline + 301, 60):
        shape_hexagon = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_hexagon.draw(color=color)
        start_point = shape_hexagon.end_point


colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]

colors_dict = {0: '0. Красный', 1: '1. Оранжевый', 2: '2. Желтый', 3: '3. Зеленый', 4: '4. Циан',
               5: '5. Синий', 6: '6. Фиолетовый'}

for i in range(len(colors_dict)):
    print(colors_dict[i])

input_color = input('Введите цифру вашего цвета: ')

try:
    if int(input_color) in colors_dict:
        print('Вы ввели ', input_color)
        color = colors[int(input_color)]
        triangle(start_point=start_point_triangle, delta=delta, length=length)
        square(start_point=start_point_square, delta=delta, length=length)
        pentagon(start_point=start_point_pentagon, delta=delta, length=length)
        hexagon(start_point=start_point_hexagon, delta=delta, length=length)
    else:
        print('Вы ввели неверное число')
        sd.pause()
except (RuntimeError, TypeError, NameError, ValueError):
    print('Вы ввели неверное число')
    sd.pause()

# TODO Я не понял как можно объединить эти условия
# TODO объединим colors с инпут_колорс
# TODO Сделаем общий словарь по номерам цвета, это будет ключ
# TODO в данных будет хранится имя цвета и его цветовая переменная

# TODO Делаем проверку на вхождение ключа в словаре
# TODO Тем самым пофиксим баг когда пользователь вводит не цифры

sd.pause()

