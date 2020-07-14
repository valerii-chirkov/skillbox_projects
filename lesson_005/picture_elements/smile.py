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
        start_coordinate_x, start_coordinate_y = 300, 300
        draw_smiles(start_coordinate_x=start_coordinate_x, start_coordinate_y=start_coordinate_y, color=color)


def draw_smiles(start_coordinate_x, start_coordinate_y, color):
    sd.resolution = (1200, 600)
    sd.background_color = color
    draw_face(start_coordinate_x, start_coordinate_y)
    draw_eyes(start_coordinate_x, start_coordinate_y)
    draw_mouth(start_coordinate_x, start_coordinate_y)
    # draw_hood(start_coordinate_x, start_coordinate_y)


def draw_face(start_coordinate_x, start_coordinate_y):
    start_point = sd.get_point(start_coordinate_x, start_coordinate_y)

    sd.circle(start_point, radius=50, color=colors[6], width=50)
    sd.circle(start_point, radius=50, color=colors[5], width=1)


def draw_eyes(start_coordinate_x, start_coordinate_y):
    start_point_left_eye = sd.get_point(start_coordinate_x - 15, start_coordinate_y)
    start_point_right_eye = sd.get_point(start_coordinate_x + 15, start_coordinate_y)

    start_point_eyes_line = sd.get_point(start_coordinate_x, start_coordinate_y + 3)
    end_point_eyes_line = sd.get_point(start_coordinate_x, start_coordinate_y - 3)

    start_point_left_pupil = sd.get_point(start_coordinate_x - 10, start_coordinate_y - 1)
    start_point_right_pupil = sd.get_point(start_coordinate_x + 10, start_coordinate_y - 1)

    sd.circle(start_point_left_eye, radius=15, color=colors[0], width=15)
    sd.circle(start_point_right_eye, radius=15, color=colors[0], width=15)

    sd.circle(start_point_left_pupil, radius=3, color=colors[5], width=3)
    sd.circle(start_point_right_pupil, radius=3, color=colors[5], width=3)

    sd.line(start_point_eyes_line, end_point_eyes_line, color=colors[5], width=1)


def draw_mouth(start_coordinate_x, start_coordinate_y):
    start_point_mouth = sd.get_point(start_coordinate_x + 5, start_coordinate_y - 30)
    end_point_mouth = sd.get_point(start_coordinate_x - 5, start_coordinate_y - 30)

    sd.line(start_point_mouth, end_point_mouth, color=colors[5], width=2)


# def draw_hood(start_coordinate_x, start_coordinate_y):
#         for _ in range(10):
#             start_point_hood = sd.get_point(start_coordinate_x + 0, start_coordinate_y + 30)
#             end_point_hood = sd.get_point(start_coordinate_x + 15, start_coordinate_y + 20)
#             sd.line(start_point_hood, end_point_hood, color=colors[7], width=5)
#             start_coordinate_x += 2
#             start_coordinate_y += 2
#         start_coordinate_x -= 20
#         start_coordinate_y -= 20
#
#         for _ in range(10):
#             start_point_hood = sd.get_point(start_coordinate_x + 15, start_coordinate_y + 20)
#             end_point_hood = sd.get_point(start_coordinate_x + 22, start_coordinate_y + 10)
#             sd.line(start_point_hood, end_point_hood, color=colors[7], width=5)
#             start_coordinate_x += 2
#             start_coordinate_y += 2
#         start_coordinate_x -= 20
#         start_coordinate_y -= 20
#
#         for _ in range(10):
#             start_point_hood = sd.get_point(start_coordinate_x + 23, start_coordinate_y - 10)
#             end_point_hood = sd.get_point(start_coordinate_x + 15, start_coordinate_y - 20)
#             sd.line(start_point_hood, end_point_hood, color=colors[7], width=5)
#             start_coordinate_x += 2
#             start_coordinate_y -= 2
#         start_coordinate_x -= 20
#         start_coordinate_y += 20
#
#         for _ in range(10):
#             start_point_hood = sd.get_point(start_coordinate_x + 15, start_coordinate_y - 20)
#             end_point_hood = sd.get_point(start_coordinate_x + 0, start_coordinate_y - 30)
#             sd.line(start_point_hood, end_point_hood, color=colors[7], width=5)
#             start_coordinate_x += 2
#             start_coordinate_y -= 2
#         start_coordinate_x -= 20
#         start_coordinate_y += 20
#         #
#         for _ in range(10):
#             start_point_hood = sd.get_point(start_coordinate_x + 0, start_coordinate_y - 30)
#             end_point_hood = sd.get_point(start_coordinate_x - 15, start_coordinate_y - 20)
#             sd.line(start_point_hood, end_point_hood, color=colors[7], width=5)
#             start_coordinate_x -= 2
#             start_coordinate_y -= 2
#         start_coordinate_x += 20
#         start_coordinate_y += 20
#
#         for _ in range(10):
#             start_point_hood = sd.get_point(start_coordinate_x - 15, start_coordinate_y - 20)
#             end_point_hood = sd.get_point(start_coordinate_x - 22, start_coordinate_y - 10)
#             sd.line(start_point_hood, end_point_hood, color=colors[7], width=5)
#             start_coordinate_x -= 2
#             start_coordinate_y -= 2
#         start_coordinate_x += 20
#         start_coordinate_y += 20
#
#         for _ in range(10):
#             start_point_hood = sd.get_point(start_coordinate_x - 23, start_coordinate_y + 10)
#             end_point_hood = sd.get_point(start_coordinate_x - 15, start_coordinate_y + 20)
#             sd.line(start_point_hood, end_point_hood, color=colors[7], width=5)
#             start_coordinate_x -= 2
#             start_coordinate_y += 2
#         start_coordinate_x += 20
#         start_coordinate_y -= 20
#
#         for _ in range(10):
#             start_point_hood = sd.get_point(start_coordinate_x - 15, start_coordinate_y + 20)
#             end_point_hood = sd.get_point(start_coordinate_x - 0, start_coordinate_y + 30)
#             sd.line(start_point_hood, end_point_hood, color=colors[7], width=5)
#             start_coordinate_x -= 2
#             start_coordinate_y += 2
#         start_coordinate_x += 20
#         start_coordinate_y -= 20
#
#         start_point_hood = sd.get_point(start_coordinate_x + 34, start_coordinate_y + 20)
#         end_point_hood = sd.get_point(start_coordinate_x + 34, start_coordinate_y - 20)
#         sd.line(start_point_hood, end_point_hood, color=colors[7], width=30)
#
#         start_point_hood = sd.get_point(start_coordinate_x - 35, start_coordinate_y + 20)
#         end_point_hood = sd.get_point(start_coordinate_x - 35, start_coordinate_y - 20)
#         sd.line(start_point_hood, end_point_hood, color=colors[7], width=30)
#
#         point = sd.get_point(300, 300)
#         radius = 56
#         sd.circle(center_position=point, radius=radius, color=sd.COLOR_ORANGE, width=25)
#
#         point = sd.get_point(300, 296)
#         radius = 36
#         sd.circle(center_position=point, radius=radius, color=sd.COLOR_BLACK, width=2)
#
#         start_point_hood = sd.get_point(start_coordinate_x, start_coordinate_y - 30)
#         end_point_hood = sd.get_point(start_coordinate_x - 15, start_coordinate_y - 45)
#         sd.line(start_point_hood, end_point_hood, color=sd.COLOR_BLACK, width=3)
#
#         start_point_hood = sd.get_point(start_coordinate_x, start_coordinate_y - 30)
#         end_point_hood = sd.get_point(start_coordinate_x + 5, start_coordinate_y - 45)
#         sd.line(start_point_hood, end_point_hood, color=sd.COLOR_BLACK, width=3)
#
#         start_point_hood = sd.get_point(start_coordinate_x + 5, start_coordinate_y - 45)
#         end_point_hood = sd.get_point(start_coordinate_x + 10, start_coordinate_y - 50)
#         sd.line(start_point_hood, end_point_hood, color=sd.COLOR_BLACK, width=2)



sd.pause()
