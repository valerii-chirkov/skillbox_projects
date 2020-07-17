import simple_draw as sd
import random

point = sd.get_point(100, 500)
traces_coordinates = [40, 450, 150, 545, 50, 545, 160, 450]
traces_coordinates_x = [40, 150, 50, 160]
traces_coordinates_y = [450, 545, 545, 450]
traces_coordinates_long = [15, 500, 165, 500, 100, 565, 100, 415]
# TODO Можно придумать алгоритм с использованием sd.random_number и sd.random_color


def sun():
    colors = [
        sd.COLOR_RED,
        sd.COLOR_ORANGE,
        sd.COLOR_YELLOW,
    ]
    # TODO Я не понял как использовать sd.random_color со своими цветами, поэтом взял функцию из return'а
    color = random.choice(colors)
    sd.circle(point, radius=50, color=color, width=50)

    angle = 45
    for i in traces_coordinates_x:
        v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates_x[i], traces_coordinates_y[i]), angle=angle,
                           length=10, width=1)
        v1.draw(color=color)
        if i >= 4:
            angle = 130

    angle = 0
    for i in range(len(traces_coordinates_long), 2):
        v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates_long[i], traces_coordinates_long[i + 1]),
                           angle=angle,
                           length=20, width=1)
        v1.draw(color=color)
        if i >= 4:
            angle = 90
    for i in range(len(traces_coordinates_long), 2):
        v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates_long[i], traces_coordinates_long[i + 1]),
                           angle=angle,
                           length=20, width=1)
        v1.draw(color=sd.background_color)
        if i >= 4:
            angle = 90
