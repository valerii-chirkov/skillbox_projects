# -*- coding: utf-8 -*-

import simple_draw as sd

# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,


# point = sd.get_point(300, 10)
# angle = (60, 120)


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


point = sd.get_point(300, 10)
angle = 90


def draw_branches(point, angle, length, delta):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=5)
    v1.draw(color=sd.COLOR_WHITE)
    next_point = v1.end_point
    # TODO тут нужно два раза описать вызов самой функции но с другими параметрами, для отклонения
    next_angle = angle - delta
    next_length = length * .75
    draw_branches(point=next_point, angle=next_angle, length=next_length, delta=delta)


# TODO Вызов функции должен быть один, а рекурсии нужно написать в самой функции,
# TODO отклонение ветвей влево и в право 
for delta in range(0, 51, 10):
    draw_branches(point=point, angle=angle, length=100, delta=delta)

for delta in range(-50, 1, 10):
    draw_branches(point=point, angle=angle, length=100, delta=delta)


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
#  TODO Аналогично делаем и тут
# def draw_branches(point, angle, length, delta):
#     if length < 10:
#         return
#     v1 = sd.get_vector(start_point=point, angle=angle, length=length)
#     v1.draw()
#     next_point = v1.end_point
#     next_angle = angle - delta
#     next_length = length * .75
#     draw_branches(point=next_point, angle=next_angle, length=next_length, delta=delta)
#
#
# for delta in range(0, 51, 10):
#     draw_branches(point=root_point, angle=90, length=100, delta=delta)
#
# for delta in range(-50, 1, 10):
#     draw_branches(point=root_point, angle=90, length=100, delta=delta)



# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

# Пока-что думаю над решением

root_point = sd.get_point(300, 30)


def draw_branches(point, angle, length, delta):
    if length < 10:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length)
    v1.draw()
    next_point = v1.end_point
    # TODO Нужно немного упростить данный алгоритм без дельта
    next_angle = angle - (delta * sd.random_number(100, 140) / 100)
    next_length = length * (.75 * sd.random_number(100, 120) / 100)
    # TODO ТутНужно сделать по аналогии от прошлых комментариев
    draw_branches(point=next_point, angle=next_angle, length=next_length, delta=delta)


# TODO Данные два цикла не требуются нужно сделать только один вызов функции с параметрами
for delta in range(0, 51, 10):
    if delta >= 0:
        draw_branches(point=root_point, angle=90, length=100, delta=delta)

for delta in range(-50, 1, 10):
    draw_branches(point=root_point, angle=90, length=100, delta=delta)

sd.pause()
