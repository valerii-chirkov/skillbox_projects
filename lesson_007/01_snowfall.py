# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)
snowflakes = []
snowflakes_out = 0
N = 10


class Snowflake:
    def __init__(self):
        self.parameter_x = sd.random_number(100, 1100)
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
        return self.parameter_y >= 0

# TODO Почему вы не удаляете тудушки или хотя бы не делает их комментариями?

# TODO как думает где у вас проблемы что конкретно не получилось ? в каких функция у вас затруднения
# TODO Напишите по подробнее.


# TODO перед каждой функцией напишите что она делает!
def get_flakes(count):  # TODO функция get_flakes(count):
    for _ in range(count):
        snowflakes.append(flake)  # TODO создает список экземпляров снежинки
    return snowflakes  # TODO и возвращает его


def get_fallen_flakes():  # TODO функция get_fallen_flakes(снежинки)
    global snowflakes_out
    for snowflake in snowflakes:
        if snowflake.parameter_y <= 0:
            snowflakes_out += 1  # TODO считает сколько снежинок упало
    return snowflakes_out  # TODO и возвращает их количество упавших


def append_flakes(count):  # TODO функция append_flakes(количество)
    #  TODO добавляет еще снежинки в список flakes который был объявлен ранее цикла.
    flakes.append(count)


flake = Snowflake()
flakes = get_flakes(count=N)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()


