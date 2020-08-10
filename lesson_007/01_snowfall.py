# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self):
        self.parameter_x = 600
        self.parameter_y = 600
        self.length = sd.random_number(5, 10)

    def clear_previous_picture(self):
        point = sd.get_point(self.parameter_x, self.parameter_y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def move(self):
        self.parameter_x += sd.random_number(-10, 10)
        self.parameter_y -= sd.random_number(10, 30)

    def draw(self):
        point = sd.get_point(self.parameter_x, self.parameter_y)
        sd.snowflake(center=point, length=self.length, color=sd.COLOR_WHITE)

    def can_fall(self):
        # TODO смотрите у нас self.parameter_y >= 50 получается булево значение, можно просто оставить это выражение
        # TODO в ретурне и если парметр будет больше то будет True а если меньше то False
        return True if (self.parameter_y >= 50) else False

        # TODO тут в моменте срабатывал всегда True ведь при старте 0 < self.parameter_x < 600 давало True.
        # TODO Срабатывало всегда на первом TRUE, or это же ИЛИ
        # if (0 < self.parameter_x < 600) or (self.parameter_y > 0):
        #     return True
        # else:
        #     return False


flake = Snowflake()

while True:
    flake.clear_previous_picture()
    flake.move()
    flake.draw()
    if not flake.can_fall():
        break
    sd.sleep(0.1)
    if sd.user_want_exit():
        break


# TODO Можно делать второй щаг

# TODO Вам нужно будет написать три функции get_flakes, get_fallen_flakes, append_flakes


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
# flakes = get_flakes(count=N)  # создать список снежинок
# while True:
#     for flake in flakes:
#         flake.clear_previous_picture()
#         flake.move()
#         flake.draw()
#     fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
#     if fallen_flakes:
#         append_flakes(count=fallen_flakes)  # добавить еще сверху
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break

sd.pause()


