# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)
snowflakes = []  # тут у нас снежинки
snowflakes_out = 0  # тут количество упавших снежинок


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
    global snowflakes_out
    snowflakes_out = 0
    for _ in range(count):
        snowflakes.append(Snowflake())  # Создает список экземпляров снежинки
    return snowflakes  # И возвращает его


# Получить упавшие снежинки
def get_fallen_flakes(snowflakes):
    global snowflakes_out
    for snowflake in snowflakes:
        Snowflake().can_fall()
        if snowflake.parameter_y <= 0:  # Если снежинка ниже нуля, то
            snowflakes_out += 1  # Считает сколько снежинок упало
    return snowflakes_out  # И возвращает количество упавших


# Добавить снежинки
def append_flakes(count):
    global snowflakes, snowflakes_out
    if snowflakes_out:
        print(snowflakes_out)
        for i in range(snowflakes_out):
            if i <= len(snowflakes) - 1:
                snowflakes.remove(snowflakes[i])
            get_flakes(count)


flakes = get_flakes(count=10)  # создали список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(snowflakes)  # подсчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()


