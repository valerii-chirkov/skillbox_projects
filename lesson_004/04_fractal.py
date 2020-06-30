# -*- coding: utf-8 -*-

import simple_draw as sd

sd.resolution = (1000, 600)
# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


# point = sd.get_point(300, 10)
# angle = (60, 120)
#
#
# def draw_branches(point, angle, length):
#     v1 = sd.get_vector(start_point=point, angle=angle[0], length=length, width=5)
#     v1.draw(color=sd.COLOR_WHITE)
#     v2 = sd.get_vector(start_point=point, angle=angle[1], length=length, width=5)
#     v2.draw(color=sd.COLOR_WHITE)
#
#
# draw_branches(point=point, angle=angle, length=100)


# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви


# point = sd.get_point(500, 10)
# angle = 90
#
#
# def draw_branches(point, angle, length):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=5)
#     v1.draw(color=sd.COLOR_WHITE)
#
#     next_point = v1.end_point
#     next_angle1 = angle - 30
#     next_angle2 = angle + 30
#     next_length = length * 0.75
#     draw_branches(next_point, next_angle1, next_length)
#     draw_branches(next_point, next_angle2, next_length)
#
#
# draw_branches(point, angle, 150)


# 3) Запустить вашу рекурсивную функцию, используя следующие параметры:
# root_point = sd.get_point(300, 30)
# draw_branches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# root_point = sd.get_point(300, 30)
#
#
# def draw_branches(root_point, angle, length):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=root_point, angle=angle, length=length, width=5)
#     v1.draw(color=sd.COLOR_WHITE)
#
#     next_point = v1.end_point
#     next_angle1 = angle - 30
#     next_angle2 = angle + 30
#     next_length = length * 0.75
#     draw_branches(next_point, next_angle1, next_length)
#     draw_branches(next_point, next_angle2, next_length)
#
#
# draw_branches(root_point, angle=90, length=150)

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# Пока-что думаю над решением

point = sd.get_point(500, 10)
angle = 90


def draw_branches(point, angle, length):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=2)
    v1.draw(color=sd.COLOR_WHITE)

    next_point = v1.end_point
    next_angle1 = angle - (sd.random_number(100, 140) / 100 * 30)
    next_angle2 = angle + (sd.random_number(100, 140) / 100 * 30)
    next_length = length * (sd.random_number(100, 120) / 100 * 0.75)
    draw_branches(next_point, next_angle1, next_length)
    draw_branches(next_point, next_angle2, next_length)


draw_branches(point, angle, 100)

sd.pause()

# зачет!
