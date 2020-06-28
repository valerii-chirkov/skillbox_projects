# -*- coding: utf-8 -*-

# (определение функций)
import simple_draw as sd

# Написать функцию отрисовки смайлика в произвольной точке экрана
# Форма рожицы-смайлика на ваше усмотрение
# Параметры функции: кордината X, координата Y, цвет.
# Вывести 10 смайликов в произвольных точках экрана.
COLOR_SKIN = (249, 215, 177)
COLOR_HOOD = (112, 63, 46)
COLOR_ORANGE = (235, 92, 51)
colors = [
        sd.COLOR_WHITE,
        sd.COLOR_RED,
        sd.COLOR_YELLOW,
        sd.COLOR_GREEN,
        sd.COLOR_BLUE,
        sd.COLOR_BLACK,
        COLOR_SKIN,
        COLOR_HOOD,
        COLOR_ORANGE
    ]


amount = int(input('Введите количество смайликов: '))
color = colors[0]


def smile(amount):
    for _ in range(amount):
        start_coordinate_x, start_coordinate_y = sd.random_number(0, 1200), sd.random_number(0, 600)
        draw_smiles(start_coordinate_x=start_coordinate_x, start_coordinate_y=start_coordinate_y, color=color)


def draw_smiles(start_coordinate_x, start_coordinate_y, color):
    sd.resolution = (1200, 600)
    sd.background_color = color

    start_point = sd.get_point(start_coordinate_x, start_coordinate_y)

    start_point_left_eye = sd.get_point(start_coordinate_x - 15, start_coordinate_y)
    start_point_right_eye = sd.get_point(start_coordinate_x + 15, start_coordinate_y)

    start_point_eyes_line = sd.get_point(start_coordinate_x, start_coordinate_y + 3)
    end_point_eyes_line = sd.get_point(start_coordinate_x, start_coordinate_y - 3)

    start_point_left_pupil = sd.get_point(start_coordinate_x - 10, start_coordinate_y - 1)
    start_point_right_pupil = sd.get_point(start_coordinate_x + 10, start_coordinate_y - 1)

    start_point_mouth = sd.get_point(start_coordinate_x + 5, start_coordinate_y - 30)
    end_point_mouth = sd.get_point(start_coordinate_x - 5, start_coordinate_y - 30)

    sd.circle(start_point, radius=50, color=colors[6], width=50)
    sd.circle(start_point, radius=50, color=colors[5], width=1)

    sd.circle(start_point_left_eye, radius=15, color=colors[0], width=15)
    sd.circle(start_point_right_eye, radius=15, color=colors[0], width=15)

    sd.circle(start_point_left_pupil, radius=3, color=colors[5], width=3)
    sd.circle(start_point_right_pupil, radius=3, color=colors[5], width=3)

    sd.line(start_point_eyes_line, end_point_eyes_line, color=colors[5], width=1)
    sd.line(start_point_mouth, end_point_mouth, color=colors[5], width=2)


smile(amount=amount)


sd.pause()

# зачет!
