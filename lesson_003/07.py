# -*- coding: utf-8 -*-

# (цикл for)
import simple_draw as sd

COLOR_BEIGE = (249, 228, 183)
sd.background_color = COLOR_BEIGE
BRICK_COLOR = (139, 79, 57)
sd.resolution = (1110, 600)
# Нарисовать стену из кирпичей. Размер кирпича - 100х50
# Использовать вложенные циклы for


def bricks():
    left_bottom_y = 0
    right_top_y = 50
    for i in range(12):
        left_bottom_x = 0
        right_top_x = 100
        if i % 2 != 0:
            left_bottom_x -= 55
            right_top_x -= 55
        for _ in range(11):
            left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
            right_top = sd.get_point(right_top_x, right_top_y)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=BRICK_COLOR, width=0)
            left_bottom_x += 110
            right_top_x += 110
        left_bottom_y += 60
        right_top_y += 60


bricks()

sd.pause()

# зачет!
