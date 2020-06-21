# -*- coding: utf-8 -*-

# (цикл for)

import simple_draw as sd
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)

# Нарисовать радугу: 7 линий разного цвета толщиной 4 с шагом 5 из точки (50, 50) в точку (350, 450)
start_x = 50
start_y = 50
end_x = 350
end_y = 350


def line(point_start_x, point_start_y, point_end_x, point_end_y, step):
    for i in range(7):
        start = sd.get_point(point_start_x, point_start_y)
        end = sd.get_point(point_end_x, point_end_y)

        point_start_x += step
        point_end_x += step
        color = rainbow_colors[i]

        sd.line(start, end, color=color, width=4)


line(point_start_x=start_x, point_start_y=start_y, point_end_x=end_x, point_end_y=end_y, step=5)

# Усложненное задание, делать по желанию.
# Нарисовать радугу дугами от окружности (cсм sd.circle) за нижним краем экрана,
# поэкспериментировать с параметрами, что бы было красиво


# sd.set_screen_size(width=350, height=600)
# point = sd.get_point(460, -200)
# sd.background_color = (15, 116, 235)
#
#
# def rainbow(point, step):
#     radius = 500
#     for i in range(7):
#         color = rainbow_colors[i]
#         radius += step
#         sd.circle(center_position=point, radius=radius, color=color, width=30)
#
#
# rainbow(point=point, step=30)


sd.pause()
