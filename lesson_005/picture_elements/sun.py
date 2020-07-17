import simple_draw as sd
import random

point = sd.get_point(100, 500)
# TODO неиспользуемые списки удаляем, некоторые можно объединить по смыслу
traces_coordinates = [40, 450, 150, 545, 50, 545, 160, 450]
traces_coordinates_x = [40, 150, 50, 160]
traces_coordinates_y = [450, 545, 545, 450]
traces_coordinates_long = [15, 500, 165, 500, 100, 565, 100, 415]


def sun():
    # TODO Тогда это список не нужен, загляните в функцию random_color посмотрите что она делает!
    colors = [
        sd.COLOR_RED,
        sd.COLOR_ORANGE,
        sd.COLOR_YELLOW,
    ]
    # TODO Вот так можно было
    color = sd.random_color()
    sd.circle(point, radius=50, color=color, width=50)

    angle = 45
    # TODO Если хотим получить индекс делаем вот так, так хоть нет ошибки
    for i, _ in enumerate(traces_coordinates_x):
        # TODO тут можно сделать вот так и сразу понятно почему у нас ошибка
        # TODO i - это не индекс это значение из traces_coordinates_x
        # TODO А ниже мы пытаемся что то получить

        # TODO Можно добавить список углов под каждый луч тогда и их тоже подставлять в нужный вектор
        start_point = sd.get_point(traces_coordinates_x[i], traces_coordinates_y[i])
        v1 = sd.get_vector(start_point=start_point, angle=angle, length=110, width=1)
        v1.draw(color=color)
        # TODO При таком раскладе у на i = 0, 1, 2, 3 (координат всего 4) условие не сработает
        if i >= 4:
            print("сработало")
            angle = 130
    # TODO Оставшийся код нам в принципе не нужен
    # angle = 0
    # for i in range(len(traces_coordinates_long), 2):
    #     v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates_long[i], traces_coordinates_long[i + 1]),
    #                        angle=angle,
    #                        length=20, width=1)
    #     v1.draw(color=color)
    #     if i >= 4:
    #         angle = 90
    # for i in range(len(traces_coordinates_long), 2):
    #     v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates_long[i], traces_coordinates_long[i + 1]),
    #                        angle=angle,
    #                        length=20, width=1)
    #     v1.draw(color=sd.background_color)
    #     if i >= 4:
    #         angle = 90
