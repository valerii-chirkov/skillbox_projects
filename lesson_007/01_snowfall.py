# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)
snowflakes = []  # тут у нас снежинки
snowflakes_out = 0  # тут количество упавших снежинок
N = 10  # задаем количество снежинок


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


# Получить снежинки в количестве count
def get_flakes(count):
    for _ in range(count):
        snowflakes.append(flake)  # Создает список экземпляров снежинки
    return snowflakes  # И возвращает его


# Получить упавшие снежинки
def get_fallen_flakes():
    global snowflakes_out
    for snowflake in snowflakes:
        if snowflake.parameter_y <= 0:  # Если снежинка ниже нуля, то
            snowflakes_out += 1  # Считает сколько снежинок упало
    return snowflakes_out  # И возвращает количество упавших


# Добавить снежинки
def append_flakes(count):
    flakes.append(count)


flake = Snowflake()  # создали экземпляр класса
flakes = get_flakes(count=N)  # создали список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes()  # подсчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()


