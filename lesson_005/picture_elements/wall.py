import simple_draw as sd
sd.set_screen_size(width=1200, height=600)
COLOR_BEIGE = (249, 228, 183)
sd.background_color = COLOR_BEIGE
BRICK_COLOR = (139, 79, 57)
GRASS_COLOR = (71, 232, 17)
BACKGROUND_COLOR = (15, 116, 235)


def background():
    left_bottom = sd.get_point(350, 95)
    right_top = sd.get_point(655, 280)
    sd.rectangle(left_bottom, right_top=right_top, color=COLOR_BEIGE, width=0)


def roof():
    left_bottom_x = 330
    left_bottom_y = 273
    length = 340
    for i in range(70):
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        v1 = sd.get_vector(left_bottom, angle=0, length=length, width=5)
        v1.draw(color=(181, 101, 29))

        if i == 25:
            left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
            v1 = sd.get_vector(left_bottom, angle=0, length=length, width=5)
            v1.draw(color=sd.COLOR_BLACK)
        elif i == 50:
            left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
            v1 = sd.get_vector(left_bottom, angle=0, length=length, width=5)
            v1.draw(color=sd.COLOR_BLACK)
        left_bottom_x += 1
        left_bottom_y += 1
        length -= 2


def bricks():
    left_bottom_y = 95
    right_top_y = 120
    for i in range(6):
        left_bottom_x = 350
        right_top_x = 400
        if i % 2 != 0:
            left_bottom_x -= 22
            right_top_x -= 22
        for _ in range(6):
            left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
            right_top = sd.get_point(right_top_x, right_top_y)
            sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=BRICK_COLOR, width=0)
            left_bottom_x += 55
            right_top_x += 55
        left_bottom_y += 30
        right_top_y += 30


def angles():
    left_bottom_x = 325
    right_top_x = 350
    left_bottom_y = 95
    right_top_y = 150

    for _ in range(2):
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        right_top = sd.get_point(right_top_x, right_top_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=GRASS_COLOR, width=0)
        left_bottom_x = 650
        right_top_x = 675
    left_bottom_x = 325
    right_top_x = 350
    left_bottom_y = 150
    right_top_y = 300
    for _ in range(2):
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        right_top = sd.get_point(right_top_x, right_top_y)
        sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=BACKGROUND_COLOR, width=0)
        left_bottom_x = 650
        right_top_x = 675


def door():
    left_bottom_x = 430
    left_bottom_y = 96
    length = 144
    left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
    v1 = sd.get_vector(left_bottom, angle=90, length=length, width=80)
    v1.draw(color=(181, 101, 29))
    left_bottom_x = 415
    for _ in range(2):
        left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
        v1 = sd.get_vector(left_bottom, angle=90, length=length, width=1)
        v1.draw(color=sd.COLOR_BLACK)
        left_bottom_x += 30
    left_bottom_x = 460
    left_bottom_y = 160
    length = 5
    left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
    v1 = sd.get_vector(left_bottom, angle=0, length=length, width=3)
    v1.draw(color=sd.COLOR_BLACK)


def window():
    left_bottom_x = 480
    left_bottom_y = 120
    left_bottom = sd.get_point(left_bottom_x, left_bottom_y)
    sd.square(left_bottom, side=120, color=sd.COLOR_CYAN, width=0)

# SNOW ------------------- для того, чтобы не было видно angles


add_parameters = []


def snowdrift_house_parameters():
    for i in range(500):
        add_parameters.append([sd.random_number(300, 370), sd.random_number(5, 10), sd.random_number(90, 150)])


def snowdrift_house():
    snowdrift_house_parameters()
    for i in range(50):
        parameter_x = add_parameters[i][0]  # для индекс, координата_х из списка координат снежинок
        parameter_y = add_parameters[i][2]
        point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
        sd.snowflake(center=point, length=add_parameters[i][1])
    for i in range(50):
        parameter_x = add_parameters[i][0] + 325 # для индекс, координата_х из списка координат снежинок
        parameter_y = add_parameters[i][2]
        point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
        sd.snowflake(center=point, length=add_parameters[i][1])
# SNOW ------------------


def house():
    background()
    bricks()
    angles()
    roof()
    door()
    window()
    snowdrift_house()


