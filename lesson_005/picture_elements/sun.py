import simple_draw as sd

point = sd.get_point(100, 500)
traces_coordinates = [40, 450, 150, 545, 50, 545, 160, 450]
traces_coordinates_long = [15, 500, 165, 500, 100, 565, 100, 415]

# TODO Можно придумать алгоритм с использованием sd.random_number и sd.random_color


def traces():
    # TODO почему бы нам сразу не пройтись по списку traces_coordinates, и получить в цикле нужное нам значение
    for i in range(0, 3, 2):
        v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates[i], traces_coordinates[i + 1]), angle=45,
                           length=10, width=1)
        v1.draw(color=sd.COLOR_YELLOW)
    # TODO Тут тоже можно поступить так же
    for i in range(4, 7, 2):
        v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates[i], traces_coordinates[i + 1]), angle=130,
                           length=10, width=1)
        v1.draw(color=sd.COLOR_YELLOW)


# TODO закрашиваются белым и беграундом практически мгновенно
def traces_animate():
    for i in range(0, 3, 2):
        v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates_long[i], traces_coordinates_long[i + 1]), angle=0,
                           length=20, width=1)
        v1.draw(color=sd.COLOR_YELLOW)
    for i in range(4, 7, 2):
        v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates_long[i], traces_coordinates_long[i + 1]), angle=90,
                           length=20, width=1)
        v1.draw(color=sd.COLOR_YELLOW)

    for i in range(0, 3, 2):
        v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates_long[i], traces_coordinates_long[i + 1]), angle=0,
                           length=20, width=1)
        v1.draw(color=sd.background_color)

    for i in range(4, 7, 2):
        v1 = sd.get_vector(start_point=sd.get_point(traces_coordinates_long[i], traces_coordinates_long[i + 1]), angle=90,
                           length=20, width=1)
        v1.draw(color=sd.background_color)


def sun():
    sd.circle(point, radius=50, color=sd.COLOR_YELLOW, width=50)


def sun_static():
    sun()
    traces()

