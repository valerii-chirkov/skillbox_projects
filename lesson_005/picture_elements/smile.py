import simple_draw as sd
sd.set_screen_size(width=1200, height=600)
COLOR_SKIN = (249, 215, 177)
COLOR_HOOD = (112, 63, 46)
COLOR_ORANGE = (235, 92, 51)
colors = [
        sd.COLOR_WHITE,
        sd.COLOR_RED,
        sd.COLOR_YELLOW,
        sd.COLOR_GREEN,
        sd.COLOR_BLUE,
        sd.COLOR_BLACK,
        COLOR_SKIN,
        COLOR_HOOD,
        COLOR_ORANGE
    ]
color = colors[0]


def smile(amount):
    for _ in range(amount):
        start_coordinate_x, start_coordinate_y = 530, 170
        draw_smiles(start_coordinate_x=start_coordinate_x, start_coordinate_y=start_coordinate_y, color=color)


def draw_smiles(start_coordinate_x, start_coordinate_y, color):
    sd.resolution = (1200, 600)
    sd.background_color = color
    draw_face(start_coordinate_x, start_coordinate_y)
    draw_eyes(start_coordinate_x, start_coordinate_y)
    draw_mouth(start_coordinate_x, start_coordinate_y)


def draw_face(start_coordinate_x, start_coordinate_y):
    start_point = sd.get_point(start_coordinate_x, start_coordinate_y)

    sd.circle(start_point, radius=50, color=colors[6], width=50)
    sd.circle(start_point, radius=50, color=colors[5], width=1)


def draw_eyes(start_coordinate_x, start_coordinate_y):
    start_point_left_eye = sd.get_point(start_coordinate_x - 15, start_coordinate_y)
    start_point_right_eye = sd.get_point(start_coordinate_x + 15, start_coordinate_y)

    start_point_eyes_line = sd.get_point(start_coordinate_x, start_coordinate_y + 3)
    end_point_eyes_line = sd.get_point(start_coordinate_x, start_coordinate_y - 3)

    sd.circle(start_point_left_eye, radius=15, color=colors[0], width=15)
    sd.circle(start_point_right_eye, radius=15, color=colors[0], width=15)
    # TODO Постараться избавиться от этого цикла, он не имеет смысла далее
    for _ in range(1):
        start_point_left_pupil = sd.get_point(start_coordinate_x - 20, start_coordinate_y - 1)
        start_point_right_pupil = sd.get_point(start_coordinate_x + 5, start_coordinate_y - 1)
        sd.circle(start_point_left_pupil, radius=3, color=sd.COLOR_WHITE, width=3)
        sd.circle(start_point_right_pupil, radius=3, color=sd.COLOR_WHITE, width=3)

        sd.circle(start_point_left_pupil, radius=3, color=colors[5], width=3)
        sd.circle(start_point_right_pupil, radius=3, color=colors[5], width=3)

        start_point_left_pupil_next = sd.get_point(start_coordinate_x - 5, start_coordinate_y - 1)
        start_point_right_pupil_next = sd.get_point(start_coordinate_x + 20, start_coordinate_y - 1)
        sd.circle(start_point_left_pupil_next, radius=3, color=sd.COLOR_WHITE, width=3)
        sd.circle(start_point_right_pupil_next, radius=3, color=sd.COLOR_WHITE, width=3)

        # TODO Все рисуется одновременно поэтому нет смещение зрачков
        # TODO Можно использовать переменную в глобальном скопе и по ней выводить либо одни глаза или другие
        sd.circle(start_point_left_pupil_next, radius=3, color=colors[5], width=3)
        sd.circle(start_point_right_pupil_next, radius=3, color=colors[5], width=3)

    sd.line(start_point_eyes_line, end_point_eyes_line, color=colors[5], width=1)


def draw_mouth(start_coordinate_x, start_coordinate_y):
    start_point_mouth = sd.get_point(start_coordinate_x + 5, start_coordinate_y - 30)
    end_point_mouth = sd.get_point(start_coordinate_x - 5, start_coordinate_y - 30)

    sd.line(start_point_mouth, end_point_mouth, color=colors[5], width=2)

