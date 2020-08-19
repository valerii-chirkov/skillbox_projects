# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)


class Snowflake:
    def __init__(self):
        self.parameter_x = sd.random_number(100, 1100)  # todo Тут прекрасно подходит "сокращённое" имя - x
        self.parameter_y = 600  # todo а тут - y
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
    snowflakes = []
    for _ in range(count):
        snowflakes.append(Snowflake())  # Создает список экземпляров снежинки
    return snowflakes  # И возвращает его


# Получить упавшие снежинки
def get_fallen_flakes(flakes):
    snowflakes_out = 0  # тут количество упавших снежинок
    for snowflake in flakes:  # для i в словаре со снежинками
        if not snowflake.can_fall():  # Если снежинка ниже нуля, то
            snowflakes_out += 1  # Считает сколько снежинок упало
    return snowflakes_out  # И возвращает количество упавших


def append_flakes(count):  # todo Передавайте список снежинок flakes через параметр
    for flake in range(count):  # 3
        flakes.remove(flakes[flake])  # TODO Удаляете наугад, поэтому некоторые снежинки зависают.
                                      #  Тем более что функция "добавить_снежинок" не должен удалять, а только добавлять
                                      #  Для того, чтобы удалить упавшие снежинки нужно сделать:
                                      #  1) чтобы функция get_fallen_flakes возвращала список индексов упавших
                                      #  2) новую функцию "удалить_снежинки" принимающую список упавших и список flakes
        flakes.append(Snowflake())


flakes = get_flakes(count=10)  # создали список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(flakes)  # подсчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()


