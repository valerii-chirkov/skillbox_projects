# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)

# TODO Используйте комментирование через #, поправил

point = sd.get_point(50, 50)
# TODO Это переменную будем получать в цикле ее можно не объявлять
color = None
# TODO Данная переменная тут не пригодится все на много проще
distance = ((50 - 350) ** 2 + (50 - 450) ** 2) ** 0.5


# TODO код не работает
def bubble(point, step):
    radius = distance
    # TODO Цикл нужно заводить сразу по тьюплу rainbow_colors и брать от туда color
    for i in range(7):
        color = rainbow_colors[i]
        radius += step
        # TODO По заданию нужно нарисовать 7 линий
        sd.circle(center_position=point, radius=radius, color=color, width=5)


bubble(point=point, step=5)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво
# sd.set_screen_size(width=350, height=600)
# point = sd.get_point(460, -200)
# color = sd.COLOR_BLACK
# distance = ((50 - 350) ** 2 + (50 - 450) ** 2) ** 0.5
#
# TODO код не работает
# TODO все комментарии аналогичные
# def bubble(point, step):
#     radius = distance
#     for i in range(7):
#         color = rainbow_colors[i]
#         radius += step
          # TODO тут все верно нужно использовать circle
#         sd.circle(center_position=point, radius=radius, color=color, width=30)
#
#
# bubble(point=point, step=30)

sd.pause()
