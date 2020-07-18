import simple_draw as sd

sd.set_screen_size(width=1200, height=600)

COLOR_SKIN = (249, 215, 177)
start_coordinate_x, start_coordinate_y = 530, 170


def draw_smiles():
    sd.resolution = (1200, 600)
    sd.background_color = sd.COLOR_WHITE
    draw_face()
    draw_eyes()
    draw_mouth()


def draw_face():
    start_point = sd.get_point(start_coordinate_x, start_coordinate_y)

    sd.circle(start_point, radius=50, color=COLOR_SKIN, width=50)
    sd.circle(start_point, radius=50, color=sd.COLOR_BLACK, width=1)


def draw_eyes():
    start_point_left_eye = sd.get_point(start_coordinate_x - 15, start_coordinate_y)
    start_point_right_eye = sd.get_point(start_coordinate_x + 15, start_coordinate_y)

    start_point_eyes_line = sd.get_point(start_coordinate_x, start_coordinate_y + 3)
    end_point_eyes_line = sd.get_point(start_coordinate_x, start_coordinate_y - 3)

    sd.circle(start_point_left_eye, radius=15, color=sd.COLOR_WHITE, width=15)
    sd.circle(start_point_right_eye, radius=15, color=sd.COLOR_WHITE, width=15)

    sd.line(start_point_eyes_line, end_point_eyes_line, color=sd.COLOR_BLACK, width=1)

    start_point_left_pupil = sd.get_point(start_coordinate_x - 20, start_coordinate_y - 1)
    start_point_right_pupil = sd.get_point(start_coordinate_x + 5, start_coordinate_y - 1)

    start_point_left_pupil_next = sd.get_point(start_coordinate_x - 5, start_coordinate_y - 1)
    start_point_right_pupil_next = sd.get_point(start_coordinate_x + 20, start_coordinate_y - 1)
    count = sd.random_number(0, 1)
    if count == 0:
        sd.circle(start_point_left_pupil, radius=3, color=sd.COLOR_BLACK, width=3)
        sd.circle(start_point_right_pupil, radius=3, color=sd.COLOR_BLACK, width=3)

        sd.circle(start_point_left_pupil_next, radius=3, color=sd.COLOR_WHITE, width=3)
        sd.circle(start_point_right_pupil_next, radius=3, color=sd.COLOR_WHITE, width=3)
    else:
        sd.circle(start_point_left_pupil_next, radius=3, color=sd.COLOR_BLACK, width=3)
        sd.circle(start_point_right_pupil_next, radius=3, color=sd.COLOR_BLACK, width=3)

        sd.circle(start_point_left_pupil, radius=3, color=sd.COLOR_WHITE, width=3)
        sd.circle(start_point_right_pupil, radius=3, color=sd.COLOR_WHITE, width=3)


def draw_mouth():
    start_point_mouth = sd.get_point(start_coordinate_x + 5, start_coordinate_y - 30)
    end_point_mouth = sd.get_point(start_coordinate_x - 5, start_coordinate_y - 30)

    sd.line(start_point_mouth, end_point_mouth, color=sd.COLOR_BLACK, width=2)

