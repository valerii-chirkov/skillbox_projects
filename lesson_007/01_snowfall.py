# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)
# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


# class Snowflake:
#     def __init__(self):
#         self.parameter_x = 600
#         self.parameter_y = 600
#         self.length = sd.random_number(5, 10)
#
#     def clear_previous_picture(self):
#         point = sd.get_point(self.parameter_x, self.parameter_y)
#         sd.snowflake(center=point, length=self.length, color=sd.background_color)
#
#     def move(self):
#         self.parameter_x += sd.random_number(-10, 10)
#         self.parameter_y -= sd.random_number(10, 30)
#
#     def draw(self):
#         point = sd.get_point(self.parameter_x, self.parameter_y)
#         sd.snowflake(center=point, length=self.length, color=sd.COLOR_WHITE)
#
#     def can_fall(self):
#         return self.parameter_y >= 50
#
#
# flake = Snowflake()
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# TODO Вам нужно будет написать три функции get_flakes, get_fallen_flakes, append_flakes

# TODO Класс снежинки нужно разкоментировать и его использовать

# TODO Не совсем верно исполнили у вас должно быть именно функции не методы. Пример кода основного цикла,
# TODO написан как подсказка по нему видно что это не методы класса!

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

# TODO функция get_flakes(count):
# TODO создает список экземпляров снежинки и возвращает его

# TODO функция get_fallen_flakes(снежинки)
# TODO считает сколько снежинок упало и возвращает их количество упавших

# TODO функция append_flakes(количество)
# TODO добавляет еще снежинки в список flakes который был объявлен ранее цикла.


# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
class Snowflakes:
    def __init__(self):
        self.snowflakes = []
        self.snowflakes_out_numbers = []
        self.parameter_x = 0
        self.parameter_y = 0
        self.length = 0

    def get_flakes(self, count):
        for _ in range(count):
            self.snowflakes.append([sd.random_number(50, 1150), sd.random_number(5, 10), 600])

    def clear_previous_picture(self):
        point = sd.get_point(self.parameter_x, self.parameter_y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def move(self):
        for i in range(len(self.snowflakes)):
            parameter_x = sd.random_number(-10, 10)
            parameter_y = sd.random_number(10, 30)
            self.snowflakes[i][0] += parameter_x
            self.snowflakes[i][2] -= parameter_y

    def draw(self):
        for snowflake in range(len(self.snowflakes)):
            parameter_x = self.snowflakes[snowflake][0]  # для индекс, координата_х из списка координат снежинок
            parameter_y = self.snowflakes[snowflake][2]  # получить координата_у по индексу

            point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
            sd.snowflake(center=point, length=self.snowflakes[snowflake][1], color=sd.COLOR_WHITE)

    def get_fallen_flakes(self):
        for index, snowflake in enumerate(self.snowflakes):
            parameter_y = snowflake[2]
            if (parameter_y <= 0) and (index not in self.snowflakes_out_numbers):
                self.snowflakes_out_numbers.append(index)

        if self.snowflakes_out_numbers:
            # сортируем
            self.snowflakes_out_numbers.sort()
            # сортируем переворачиваем по возрастанию
            self.snowflakes_out_numbers.reverse()
            print(self.snowflakes_out_numbers)
            return self.snowflakes_out_numbers

    def append_flakes(self):
        pass


flakes1 = Snowflakes()
flakes = flakes1.get_flakes(count=10)  # создать список снежинок
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


