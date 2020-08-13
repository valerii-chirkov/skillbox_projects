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
    snowflakes_out = 0  # тут количество упавших снежинок
    for snowflake in snowflakes:  # для i в словаре со снежинками
        # TODO для чего мы вызываем этот метод ? Мы должны его вызывать у экземпляров которые получили при переборе списка
        # TODO Что этот метод у нас возвращает ? и вообще для чего мы его определили в классе ?
        Snowflake().can_fall()  # вызываем метод can.fall() из класса Snowflake()
        if snowflake.parameter_y <= 0:  # Если снежинка ниже нуля, то
            snowflakes_out += 1  # Считает сколько снежинок упало
    return snowflakes_out  # И возвращает количество упавших


# Добавить снежинки
# TODO функция должна работать только со своими параметрами, возможно нужно какой то еще добавить!
def append_flakes(count):
    # TODO эта проверка у нас уже есть в главном цикле!
    if fallen_flakes:  # Если snowflakes_out не пустой, то:
        print(fallen_flakes)
        # TODO скорее нужно сколько снежинок упало count, завести цикл по этому числу и добавить еще в flakes
        for i in range(fallen_flakes):  # Для каждой снежинки в snowflakes_out:
            # TODO функция не знает о таком параметре как snowflakes, что нужно сделать ?
            if i <= len(snowflakes) - 1:  # Если снежинка меньше или равна длине списка - 1 (на самом деле я сам не понимаю почему здесь такое условие, взял из прошлого модуля)
                # TODO убирать снежинку нам не нужно по ка что не нужно! Удалить строку эту
                snowflakes.remove(snowflakes[i])  # Убираем снежинку
                print(len(snowflakes))
                # TODO даже если этот код был бы рабочим то мы в список flakes добавили просто число! count - число,
                #  не снежинка!
                # flakes.append(count)  # И добавляем новую, закоментил, потому что с ней вылетает
            # TODO тут он создает новый список а нам нужно добавить этот flakes
            get_flakes(count)


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


