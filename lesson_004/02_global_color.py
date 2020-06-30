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
# TODO объединим colors с инпут_колорс
# TODO Сделаем общий словарь по номерам цвета, это будет ключ
# TODO в данных будет хранится имя цвета и его цветовая переменная
colors = [(0, sd.COLOR_RED), (1, sd.COLOR_ORANGE), (2, sd.COLOR_YELLOW),
          (3, sd.COLOR_GREEN), (4, sd.COLOR_CYAN), (5, sd.COLOR_BLUE), (6, sd.COLOR_PURPLE)]
start_point_triangle = sd.get_point(10, 10)
start_point_square = sd.get_point(120, 10)
start_point_pentagon = sd.get_point(240, 10)
start_point_hexagon = sd.get_point(360, 10)
delta = 0
length = 100


# TODO Поправить с корректировками от 1 урока
def triangle(start_point, delta, length):
    for _ in range(3):
        shape_triangle = sd.get_vector(start_point=start_point, angle=delta, length=length, width=2)
        shape_triangle.draw(color=color)
        delta += 120
        start_point = shape_triangle.end_point


def square(start_point, delta, length):
    for _ in range(4):
        shape_square = sd.get_vector(start_point=start_point, angle=delta, length=length-10, width=2)
        shape_square.draw(color=color)
        delta += 90
        start_point = shape_square.end_point


def pentagon(start_point, delta, length):
    for _ in range(5):
        shape_pentagon = sd.get_vector(start_point=start_point, angle=delta, length=length-40, width=2)
        shape_pentagon.draw(color=color)
        delta += 72
        start_point = shape_pentagon.end_point


def hexagon(start_point, delta, length):
    for _ in range(6):
        shape_hexagon = sd.get_vector(start_point=start_point, angle=delta, length=length-45, width=2)
        shape_hexagon.draw(color=color)
        delta += 60
        start_point = shape_hexagon.end_point

# TODO Тут мы импутом просто просим ввести число
# TODO предварительно фором выведем все возможные варианты, это делается для того чтобы если нам нужно будет добавит
# TODO цвет, мы его добавит только в одном месте
input_color = int(input('''Введите номер желаемого цвета:
                    0. Красный 
                    1. Оранжевый
                    2. Желтый
                    3. Зеленый
                    4. Циан
                    5. Синий
                    6. Фиолетовый

                    '''))
# TODO Делаем проверку на вхождение ключа в словаре
# TODO Тем самым пофиксим баг когда пользователь вводит не цифры
if input_color in range(len(colors)):
    print('Вы ввели ', input_color)
    color = colors[input_color][1]
else:
    print('Вы ввели неверное число')
    sd.pause()

# TODO Данные вызовы нужно поместить в иф условие чтобы они не выполнялись если ложно
triangle(start_point=start_point_triangle, delta=delta, length=length)
square(start_point=start_point_square, delta=delta, length=length)
pentagon(start_point=start_point_pentagon, delta=delta, length=length)
hexagon(start_point=start_point_hexagon, delta=delta, length=length)

sd.pause()

