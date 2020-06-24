# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw

COLOR_BEIGE = (249, 228, 183)
simple_draw.background_color = (147, 58, 22)
simple_draw.resolution = (1000, 1000)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


# TODO Попробуем упростить данный алгоритм
# TODO Заводим цикл в в цикле, в первом цикле получаем через функцию инумерайт номер строки
# TODO а через функцию рандж в заданном диапазоне координату Y (0, 601, 50)
# TODO Во втором цикле цикле в заданном диапазоне получаем координату X, только перед этим
# TODO проверяем строку на четность и от этого меняем начало диапазона у след.ряда кирпичей
# TODO Создаем начальные и конечные точки рисования для функции прямоугольника
# TODO Рисуем прямоугольник, функцией прямоугольник
def bricks1():
    x1, y1 = 0, 1000
    x2, y2 = 1000, 1000
    for i in range(20):
        start = simple_draw.get_point(x1, y1)
        end = simple_draw.get_point(x2, y2)
        simple_draw.line(start_point=start, end_point=end, color=COLOR_BEIGE, width=5)
        for j in range(10):
            x11 = x1 + (100 * j)
            if i % 2 != 0:
                x11 += 50
            else:
                pass
            y11 = y1
            x22, y22 = x11, y1 - 50
            start1 = simple_draw.get_point(x11, y11)
            end1 = simple_draw.get_point(x22, y22)
            simple_draw.line(start_point=start1, end_point=end1, color=COLOR_BEIGE, width=5)
        y1 -= 50
        y2 -= 50


bricks1()

simple_draw.pause()
