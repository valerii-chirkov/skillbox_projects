# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)


class Snowflake:
    def __init__(self):
        self.x = sd.random_number(100, 1100)
        self.y = 600
        self.length = sd.random_number(5, 10)

    def clear_previous_picture(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.background_color)

    def move(self):
        self.x += sd.random_number(-10, 10)
        self.y -= sd.random_number(10, 30)

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length, color=sd.COLOR_WHITE)

    def can_fall(self):
        return self.y >= 0


# Получить снежинки в количестве count
def get_flakes(count):
    snowflakes = []
    for _ in range(count):
        snowflakes.append(Snowflake())  # Создает список экземпляров снежинки
    return snowflakes  # И возвращает его


# Получить упавшие снежинки
def get_fallen_flakes(flakes):
    snowflakes_out = []  # тут количество упавших снежинок
    for index, snowflake in enumerate(flakes):
        if not snowflake.can_fall():
            snowflakes_out.append(index)
    if snowflakes_out:
        snowflakes_out.sort()  # сортируем
        snowflakes_out.reverse()  # переворачиваем по возрастанию
        print(snowflakes_out)
    return snowflakes_out  # И возвращает количество упавших


def append_flakes(count, flakes):
    for _ in count:  # 3
        flakes.append(Snowflake())


def del_flakes(snowflakes_out, flakes):
    for idx in snowflakes_out:
        if idx <= len(flakes)-1:  #  Объясните пожалуйста что это за проверка
                                  # (преподаватель написал в прошлом модуле, но не объяснил)
                                  # -- Перестраховка на случай, чтобы не получить ошибку доступа к несуществующему
                                  #  элементу. Тут достаточно просто del flakes[idx] вместо if
            flakes.remove(flakes[idx])


flakes = get_flakes(count=10)  # создали список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(flakes)  # подсчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes, flakes=flakes)  # добавить еще сверху
        del_flakes(snowflakes_out=fallen_flakes, flakes=flakes)
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()

# зачет!
