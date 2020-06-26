# -*- coding: utf-8 -*-

import simple_draw as sd

# Запросить у пользователя желаемую фигуру посредством выбора из существующих
#   вывести список всех фигур с номерами и ждать ввода номера желаемой фигуры.
# и нарисовать эту фигуру в центре экрана

# Код функций из упр lesson_004/02_global_color.py скопировать сюда
# Результат решения см lesson_004/results/exercise_03_shape_select.jpg
# TODO Константы из списка заносим в словарь по нужному ключу
colors = [sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN, sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE]
start_point_triangle = sd.get_point(250, 250)
start_point_square = sd.get_point(250, 250)
start_point_pentagon = sd.get_point(270, 270)
start_point_hexagon = sd.get_point(270, 270)
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
input_shape = int(input('''Введите номер желаемой фигуры:
                    0. Треугольник
                    1. Квадрат
                    2. Пятиугольник
                    3. Шестиугольник
                    
                    '''))

# TODO Тут делаем аналогично с поправками от прошлых уроков, + в словарях можно также хранить и функции.
# TODO В условии, если номер есть в словаре мы сможем сразу вытащить все нужные данные и функцию рисования.
# TODO Если нет то завершаем работу, выводом нужного сообщения
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
    shape_triangle_2 = sd.get_vector(start_point=shape_triangle_1.end_point, angle=delta + 120, length=length, width=2)
    shape_triangle_2.draw(color=color)
    shape_triangle_3 = sd.get_vector(start_point=shape_triangle_2.end_point, angle=delta + 240, length=length, width=2)
    shape_triangle_3.draw(color=color)


def square(start_point, delta, length):
    shape_square_1 = sd.get_vector(start_point=start_point, angle=delta, length=length - 10, width=2)
    shape_square_1.draw(color=color)
    shape_square_2 = sd.get_vector(start_point=shape_square_1.end_point, angle=delta + 90, length=length - 10, width=2)
    shape_square_2.draw(color=color)
    shape_square_3 = sd.get_vector(start_point=shape_square_2.end_point, angle=delta + 180, length=length - 10, width=2)
    shape_square_3.draw(color=color)
    shape_square_4 = sd.get_vector(start_point=shape_square_3.end_point, angle=delta + 270, length=length - 10, width=2)
    shape_square_4.draw(color=color)


def pentagon(start_point, delta, length):
    shape_pentagon_1 = sd.get_vector(start_point=start_point, angle=delta, length=length - 40, width=2)
    shape_pentagon_1.draw(color=color)
    shape_pentagon_2 = sd.get_vector(start_point=shape_pentagon_1.end_point, angle=delta + 72, length=length - 40,
                                     width=2)
    shape_pentagon_2.draw(color=color)
    shape_pentagon_3 = sd.get_vector(start_point=shape_pentagon_2.end_point, angle=delta + 144, length=length - 40,
                                     width=2)
    shape_pentagon_3.draw(color=color)
    shape_pentagon_4 = sd.get_vector(start_point=shape_pentagon_3.end_point, angle=delta + 216, length=length - 40,
                                     width=2)
    shape_pentagon_4.draw(color=color)
    shape_pentagon_5 = sd.get_vector(start_point=shape_pentagon_4.end_point, angle=delta + 288, length=length - 40,
                                     width=2)
    shape_pentagon_5.draw(color=color)


def hexagon(start_point, delta, length):
    shape_hexagon_1 = sd.get_vector(start_point=start_point, angle=delta, length=length - 45, width=2)
    shape_hexagon_1.draw(color=color)
    shape_hexagon_2 = sd.get_vector(start_point=shape_hexagon_1.end_point, angle=delta + 60, length=length - 45,
                                    width=2)
    shape_hexagon_2.draw(color=color)
    shape_hexagon_3 = sd.get_vector(start_point=shape_hexagon_2.end_point, angle=delta + 120, length=length - 45,
                                    width=2)
    shape_hexagon_3.draw(color=color)
    shape_hexagon_4 = sd.get_vector(start_point=shape_hexagon_3.end_point, angle=delta + 180, length=length - 45,
                                    width=2)
    shape_hexagon_4.draw(color=color)
    shape_hexagon_5 = sd.get_vector(start_point=shape_hexagon_4.end_point, angle=delta + 240, length=length - 45,
                                    width=2)
    shape_hexagon_5.draw(color=color)
    shape_hexagon_6 = sd.get_vector(start_point=shape_hexagon_5.end_point, angle=delta + 300, length=length - 45,
                                    width=2)
    shape_hexagon_6.draw(color=color)


# TODO Делаем код всегда более расширяемым!
# TODO В данном случае если мы введем еще одну фигуру нужно будет дописывать еще и тут пару строк!
if input_shape == 0:
    print('Вы ввели ', input_shape)
    triangle(start_point=start_point_triangle, delta=delta, length=length)
elif input_shape == 1:
    print('Вы ввели ', input_shape)
    square(start_point=start_point_square, delta=delta, length=length)
elif input_shape == 2:
    print('Вы ввели ', input_shape)
    pentagon(start_point=start_point_pentagon, delta=delta, length=length)
elif input_shape == 3:
    print('Вы ввели ', input_shape)
    hexagon(start_point=start_point_hexagon, delta=delta, length=length)
else:
    print('Вы ввели неверное число')


sd.pause()
