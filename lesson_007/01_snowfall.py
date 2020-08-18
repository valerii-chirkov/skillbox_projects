# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)


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
    snowflakes = []
    for _ in range(count):
        snowflakes.append(Snowflake())  # Создает список экземпляров снежинки
    return snowflakes  # И возвращает его


# Получить упавшие снежинки
def get_fallen_flakes(snowflakes):
    # TODO нужно сделать подсчет тип int
    snowflakes_out = []  # тут количество упавших снежинок
    for snowflake in snowflakes:  # для i в словаре со снежинками
        # TODO Что этот метод у нас возвращает ? и вообще для чего мы его определили в классе ?
        # TODO Эта строка нам важна, нужно понять для чего мы ее тут вызываем ?
        # TODO Какой результат она нам дает, и что в коде сейчас дублируется ?
        snowflake.can_fall()  # вызываем метод can.fall() из класса Snowflake()
        if snowflake.parameter_y <= 0:  # Если снежинка ниже нуля, то
            # TODO сейчас мы тут не считаем количество а создаем новый список! А куда количество делось?
            snowflakes_out.append(snowflake)  # Считает сколько снежинок упало
    return snowflakes_out  # И возвращает количество упавших


# TODO эта функция должна принимать количество а не список снежинок
def append_flakes(count):
    for flake in count:  # 3
        flakes.remove(flake)
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


