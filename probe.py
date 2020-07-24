import simple_draw as sd

COLOR_FOOTER = (41, 11, 72)
FLOOR_COLORS = [(203, 69, 129), (173, 48, 103), (133, 0, 60)]
WALL_COLORS = ([79, 50, 130], [42, 10, 75], [120, 65, 140])
WINDOW_COLORS = ([246, 89, 161], [217, 62, 137], [114, 25, 94], [141, 30, 84], [192, 52, 125], [207, 62, 135], [97, 33, 95])
TREE_COLOR = (93, 35, 95)
CURTAINS_COLORS = [(181, 30, 190), (160, 6, 163)]
CEILING_COLOR = ([223, 100, 168], [176, 46, 103], [41, 11, 72])
DOOR_COLORS = ([115, 6, 51], [75, 6, 64], [201, 98, 157], [126, 0, 76], [227, 120, 172])
CLOCK_COLORS = ([158, 58, 120], [220, 107, 172], [125, 0, 67], [49, 2, 76])
PICTURE_COLORS = ([97, 13, 71], [166, 51, 114], [71, 0, 77], [222, 104, 175], [255, 135, 200], [168, 50, 97], [124, 0, 59], [87, 54, 123])
WARDROBE_COLORS = ([116, 5, 141], [64, 0, 78])


def footer():
    left_bottom = sd.get_point(0, 0)
    right_top = sd.get_point(600, 75)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=COLOR_FOOTER, width=0)


def floor():
    start_height_1 = 76
    length = 600
    length_random = [sd.random_number(50, 500), sd.random_number(10, 50)]
    for i in range(75):
        start = sd.get_point(0, start_height_1+(1*i))
        sd.vector(start=start, angle=0, color=FLOOR_COLORS[0], length=length-(1*i))
    for i in range(30):
        start_random = sd.get_point(sd.random_number(-100, 600), sd.random_number(80, 145))
        sd.vector(start=start_random, angle=0, color=FLOOR_COLORS[1], length=length_random[0], width=sd.random_number(1,5))
    for i in range(50):
        start_random = sd.get_point(sd.random_number(-100, 600), sd.random_number(80, 145))
        sd.vector(start=start_random, angle=0, color=FLOOR_COLORS[2], length=length_random[1])


def wall():
    left_bottom = sd.get_point(0, 150)
    right_top = sd.get_point(525, 550)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=WALL_COLORS[0], width=0)
    sd.rectangle(left_bottom=sd.get_point(0, 150), right_top=sd.get_point(525, 230), color=WALL_COLORS[1], width=0)
    sd.vector(start=sd.get_point(0, 235), angle=0, color=WALL_COLORS[1], length=525, width=3)
    for i in range(75):
        sd.vector(start=sd.get_point(3 + (i*7), 535), angle=0, color=WALL_COLORS[1], length=1, width=2)
        sd.vector(start=sd.get_point(3 + (i*7), 545), angle=0, color=WALL_COLORS[1], length=1, width=2)
    for z in range(3, 10, 3):
        for i in range(210):
            start = sd.get_point(3 + (i*(5/(z/5))), 535+z)
            sd.vector(start=start, angle=0, color=WALL_COLORS[1], length=1, width=1)
    sd.rectangle(left_bottom=sd.get_point(0, 545), right_top=sd.get_point(525, 550), color=WALL_COLORS[1], width=0)
    sd.vector(start=sd.get_point(0, 150), angle=0, color=DOOR_COLORS[1], length=600, width=4)


def window():
    left_bottom = sd.get_point(0, 270)
    right_top = sd.get_point(160, 500)
    sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=WINDOW_COLORS[0], width=0)

    def tree():
        sd.vector(start=sd.get_point(0, 425), angle=0, color=TREE_COLOR, length=5, width=2)
        sd.vector(start=sd.get_point(0, 428), angle=0, color=TREE_COLOR, length=10, width=2)
        sd.vector(start=sd.get_point(5, 427), angle=0, color=TREE_COLOR, length=10, width=4)
        sd.vector(start=sd.get_point(15, 429), angle=0, color=TREE_COLOR, length=8, width=4)
        sd.vector(start=sd.get_point(24, 431), angle=0, color=TREE_COLOR, length=6, width=4)
        sd.vector(start=sd.get_point(31, 433), angle=0, color=TREE_COLOR, length=40, width=4)
        sd.vector(start=sd.get_point(52, 431), angle=0, color=TREE_COLOR, length=28, width=4)
        sd.vector(start=sd.get_point(55, 429), angle=0, color=TREE_COLOR, length=28, width=4)
        sd.vector(start=sd.get_point(63, 427), angle=0, color=TREE_COLOR, length=28, width=4)
        sd.vector(start=sd.get_point(72, 425), angle=0, color=TREE_COLOR, length=25, width=4)
        for i in range(4):
            sd.vector(start=sd.get_point(81+(3*i), 423-(2*i)), angle=0, color=TREE_COLOR, length=25, width=4)
        for i in range(13):
            sd.vector(start=sd.get_point((96+(3*i)), 415-(2*i)), angle=0, color=TREE_COLOR, length=25, width=4)
        for i in range(3):
            sd.vector(start=sd.get_point(61-(i*2), 435+(i*2)), angle=0, color=TREE_COLOR, length=10, width=4)
        for i in range(3):
            sd.vector(start=sd.get_point(55-(i*2), 443+(i*2)), angle=0, color=TREE_COLOR, length=9, width=4)
        for i in range(3):
            sd.vector(start=sd.get_point(47-(i*2), 451+(i*2)), angle=0, color=TREE_COLOR, length=7, width=4)
        for i in range(3):
            sd.vector(start=sd.get_point(41-(i*2), 458+(i*2)), angle=0, color=TREE_COLOR, length=6, width=4)
        for i in range(3):
            sd.vector(start=sd.get_point(35-(i*2), 465+(i*2)), angle=0, color=TREE_COLOR, length=5, width=4)
        sd.vector(start=sd.get_point(16, 470), angle=0, color=TREE_COLOR, length=20, width=2)
        sd.vector(start=sd.get_point(12, 468), angle=0, color=TREE_COLOR, length=5, width=2)
        sd.vector(start=sd.get_point(0, 485), angle=-25, color=TREE_COLOR, length=40, width=3)
        sd.vector(start=sd.get_point(20, 485), angle=-50, color=TREE_COLOR, length=20, width=3)
        sd.vector(start=sd.get_point(90, 462), angle=-80, color=TREE_COLOR, length=40, width=3)
        sd.vector(start=sd.get_point(86, 464), angle=-20, color=TREE_COLOR, length=5, width=3)
        sd.vector(start=sd.get_point(84, 482), angle=-80, color=TREE_COLOR, length=20, width=2)
        sd.vector(start=sd.get_point(84, 475), angle=30, color=TREE_COLOR, length=10, width=2)
        sd.vector(start=sd.get_point(78, 480), angle=-30, color=TREE_COLOR, length=10, width=2)
        sd.vector(start=sd.get_point(140, 300), angle=90, color=TREE_COLOR, length=100, width=20)
        sd.vector(start=sd.get_point(130, 400), angle=60, color=TREE_COLOR, length=50, width=20)
    tree()

    for i in range(22):
        sd.vector(start=sd.get_point(5+(i*7), 285), angle=90, color=WINDOW_COLORS[1], length=30, width=3)
    sd.vector(start=sd.get_point(5, 308), angle=0, color=WINDOW_COLORS[1], length=148, width=3)
    for i in range(4):
        sd.vector(start=sd.get_point(0, (445+(i*3))), angle=0, color=WINDOW_COLORS[2+i], length=159, width=3)
    sd.vector(start=sd.get_point(25, 451), angle=0, color=WINDOW_COLORS[2], length=5, width=10)
    for i in range(3):
        sd.vector(start=sd.get_point(0, (495+(i*3))), angle=0, color=WINDOW_COLORS[2+i], length=159, width=3)
    sd.vector(start=sd.get_point(0, 270), angle=0, color=WINDOW_COLORS[6], length=159, width=3)
    sd.vector(start=sd.get_point(0, 273), angle=0, color=WINDOW_COLORS[4], length=159, width=3)
    sd.vector(start=sd.get_point(0, 276), angle=0, color=WINDOW_COLORS[5], length=159, width=3)

    def curtains():
        sd.vector(start=sd.get_point(140, 175), angle=90, color=CURTAINS_COLORS[0], length=323, width=50)
        sd.vector(start=sd.get_point(118, 175), angle=90, color=CURTAINS_COLORS[1], length=323, width=5)
        sd.vector(start=sd.get_point(118, 175), angle=90, color=CURTAINS_COLORS[1], length=20, width=12)
        sd.vector(start=sd.get_point(122, 175), angle=90, color=CURTAINS_COLORS[1], length=150, width=7)
        sd.vector(start=sd.get_point(130, 175), angle=90, color=CURTAINS_COLORS[1], length=150, width=2)
        sd.vector(start=sd.get_point(125, 250), angle=90, color=CURTAINS_COLORS[1], length=245, width=2)
        sd.vector(start=sd.get_point(160, 402), angle=90, color=CURTAINS_COLORS[1], length=96, width=20)
        sd.vector(start=sd.get_point(157, 302), angle=90, color=CURTAINS_COLORS[1], length=100, width=17)
        sd.vector(start=sd.get_point(164, 202), angle=90, color=CURTAINS_COLORS[1], length=100, width=15)
        sd.vector(start=sd.get_point(166, 175), angle=90, color=CURTAINS_COLORS[1], length=100, width=17)
        sd.vector(start=sd.get_point(166, 165), angle=90, color=CURTAINS_COLORS[1], length=20, width=10)
        for i in range(30):
            sd.vector(start=sd.get_point(sd.random_number(120, 150), sd.random_number(180, 450)), angle=90,
                      color=CURTAINS_COLORS[1], length=sd.random_number(5, 50), width=3)
    curtains()


def ceiling():
    sd.vector(start=sd.get_point(0, 553), angle=0, color=CEILING_COLOR[0], length=525, width=7)
    sd.vector(start=sd.get_point(0, 558), angle=0, color=CEILING_COLOR[1], length=525, width=4)
    sd.vector(start=sd.get_point(0, 585), angle=0, color=CEILING_COLOR[2], length=600, width=50)


def door():
    # left_bottom = sd.get_point(570, 0)
    # right_top = sd.get_point(525, 550)
    # sd.rectangle(left_bottom=left_bottom, right_top=right_top, color=WALL_COLORS[0], width=0)
    sd.vector(start=sd.get_point(525, 190), angle=-44, color=DOOR_COLORS[0], length=120, width=80)
    sd.vector(start=sd.get_point(525, 150), angle=-44, color=DOOR_COLORS[1], length=120, width=4)
    sd.vector(start=sd.get_point(525, 535), angle=35, color=DOOR_COLORS[0], length=120, width=30)
    sd.vector(start=sd.get_point(525, 553), angle=35, color=CEILING_COLOR[0], length=525, width=7)
    sd.vector(start=sd.get_point(525, 558), angle=35, color=CEILING_COLOR[1], length=525, width=4)
    sd.vector(start=sd.get_point(527, 190), angle=90, color=DOOR_COLORS[0], length=350, width=5)
    sd.vector(start=sd.get_point(530, 365), angle=-44, color=CEILING_COLOR[1], length=120, width=280)
    sd.vector(start=sd.get_point(530, 385), angle=35, color=CEILING_COLOR[1], length=120, width=280)
    sd.vector(start=sd.get_point(527, 235), angle=-44, color=DOOR_COLORS[0], length=120, width=5)

    sd.vector(start=sd.get_point(550, 243), angle=-44, color=DOOR_COLORS[2], length=70, width=230)
    sd.vector(start=sd.get_point(550, 360), angle=35, color=DOOR_COLORS[2], length=70, width=160)
    for i in range(130):
        sd.vector(start=sd.get_point(560, 140+(i*1)), angle=-34, color=CEILING_COLOR[1], length=20, width=2)
    for i in range(30):
        sd.vector(start=sd.get_point(560, 240 + (i * 1)), angle=-15, color=CEILING_COLOR[1], length=17, width=2)

    for i in range(130):
        sd.vector(start=sd.get_point(590, 120+(i*1)), angle=-34, color=CEILING_COLOR[1], length=20, width=2)
    for i in range(40):
        sd.vector(start=sd.get_point(590, 220 + (i * 1)), angle=-15, color=CEILING_COLOR[1], length=17, width=2)

    for i in range(100):
        sd.vector(start=sd.get_point(560, 310+(i*1)), angle=-15, color=CEILING_COLOR[1], length=20, width=2)
    for i in range(35):
        sd.vector(start=sd.get_point(560, 390 + (i * 1)), angle=35, color=CEILING_COLOR[1], length=24, width=2)

    for i in range(130):
        sd.vector(start=sd.get_point(590, 300+(i*1)), angle=-15, color=CEILING_COLOR[1], length=20, width=2)
    for i in range(40):
        sd.vector(start=sd.get_point(590, 400 + (i * 1)), angle=35, color=CEILING_COLOR[1], length=24, width=2)

    sd.vector(start=sd.get_point(549, 125), angle=90, color=DOOR_COLORS[1], length=313, width=2)
    sd.vector(start=sd.get_point(549, 438), angle=35, color=DOOR_COLORS[1], length=100, width=3)

    sd.vector(start=sd.get_point(559, 139), angle=90, color=DOOR_COLORS[3], length=130, width=2)
    sd.vector(start=sd.get_point(575, 127), angle=90, color=DOOR_COLORS[4], length=138, width=2)

    sd.vector(start=sd.get_point(559, 310), angle=90, color=DOOR_COLORS[3], length=114, width=2)
    sd.vector(start=sd.get_point(578, 303), angle=90, color=DOOR_COLORS[4], length=134, width=2)

    sd.vector(start=sd.get_point(589, 119), angle=90, color=DOOR_COLORS[3], length=140, width=2)
    sd.vector(start=sd.get_point(589, 300), angle=90, color=DOOR_COLORS[3], length=139, width=2)


def clock():
    sd.circle(center_position=sd.get_point(400, 418), radius=30, color=CLOCK_COLORS[3], width=0)
    sd.circle(center_position=sd.get_point(400, 420), radius=30, color=CLOCK_COLORS[0], width=0)
    sd.circle(center_position=sd.get_point(400, 420), radius=28, color=CLOCK_COLORS[1], width=0)
    sd.vector(start=sd.get_point(400, 420), angle=90, color=CLOCK_COLORS[2], length=20, width=2)
    sd.vector(start=sd.get_point(400, 420), angle=-45, color=CLOCK_COLORS[2], length=10, width=2)
    sd.circle(center_position=sd.get_point(380, 420), radius=2, color=CLOCK_COLORS[2], width=0)
    sd.circle(center_position=sd.get_point(420, 420), radius=2, color=CLOCK_COLORS[2], width=0)
    sd.circle(center_position=sd.get_point(400, 440), radius=2, color=CLOCK_COLORS[2], width=0)
    sd.circle(center_position=sd.get_point(400, 400), radius=2, color=CLOCK_COLORS[2], width=0)


def pictures():
    sd.rectangle(left_bottom=sd.get_point(290, 400), right_top=sd.get_point(325, 450), color=PICTURE_COLORS[0])
    sd.rectangle(left_bottom=sd.get_point(292, 402), right_top=sd.get_point(323, 448), color=PICTURE_COLORS[1])
    sd.rectangle(left_bottom=sd.get_point(294, 404), right_top=sd.get_point(321, 446), color=PICTURE_COLORS[3])

    sd.rectangle(left_bottom=sd.get_point(303, 404), right_top=sd.get_point(312, 418), color=PICTURE_COLORS[2])
    sd.vector(start=sd.get_point(307, 418), angle=90, color=PICTURE_COLORS[2], length=4, width=3)
    sd.circle(center_position=sd.get_point(307, 421), radius=3, color=PICTURE_COLORS[2], width=0)

    sd.circle(center_position=sd.get_point(300, 433), radius=4, color=PICTURE_COLORS[4], width=0)
    sd.circle(center_position=sd.get_point(304, 435), radius=3, color=PICTURE_COLORS[4], width=0)

    sd.circle(center_position=sd.get_point(312, 429), radius=3, color=PICTURE_COLORS[4], width=0)
    sd.circle(center_position=sd.get_point(315, 428), radius=5, color=PICTURE_COLORS[4], width=0)

    sd.rectangle(left_bottom=sd.get_point(220, 380), right_top=sd.get_point(275, 410), color=PICTURE_COLORS[0])
    sd.rectangle(left_bottom=sd.get_point(222, 382), right_top=sd.get_point(273, 408), color=PICTURE_COLORS[1])
    sd.rectangle(left_bottom=sd.get_point(224, 384), right_top=sd.get_point(271, 406), color=PICTURE_COLORS[3])
    sd.vector(start=sd.get_point(224, 387), angle=20, color=PICTURE_COLORS[7], length=10, width=7)
    sd.vector(start=sd.get_point(234, 391), angle=-20, color=PICTURE_COLORS[7], length=10, width=7)
    sd.vector(start=sd.get_point(244, 387), angle=20, color=PICTURE_COLORS[7], length=20, width=7)
    sd.vector(start=sd.get_point(263, 392), angle=-20, color=PICTURE_COLORS[7], length=8, width=7)
    sd.vector(start=sd.get_point(224, 387), angle=0, color=PICTURE_COLORS[7], length=46, width=7)
    sd.rectangle(left_bottom=sd.get_point(244, 384), right_top=sd.get_point(250, 392), color=PICTURE_COLORS[2])
    sd.circle(center_position=sd.get_point(247, 394), radius=3, color=PICTURE_COLORS[2], width=0)
    sd.rectangle(left_bottom=sd.get_point(234, 384), right_top=sd.get_point(240, 392), color=PICTURE_COLORS[2])
    sd.circle(center_position=sd.get_point(237, 394), radius=3, color=PICTURE_COLORS[2], width=0)
    sd.rectangle(left_bottom=sd.get_point(254, 384), right_top=sd.get_point(260, 392), color=PICTURE_COLORS[2])
    sd.circle(center_position=sd.get_point(257, 394), radius=3, color=PICTURE_COLORS[2], width=0)

    sd.rectangle(left_bottom=sd.get_point(290, 370), right_top=sd.get_point(325, 390), color=PICTURE_COLORS[6])
    sd.rectangle(left_bottom=sd.get_point(292, 372), right_top=sd.get_point(323, 388), color=PICTURE_COLORS[5])
    sd.rectangle(left_bottom=sd.get_point(296, 372), right_top=sd.get_point(300, 376), color=PICTURE_COLORS[2])
    sd.rectangle(left_bottom=sd.get_point(302, 372), right_top=sd.get_point(306, 376), color=PICTURE_COLORS[2])
    sd.rectangle(left_bottom=sd.get_point(310, 372), right_top=sd.get_point(314, 378), color=PICTURE_COLORS[2])


def wardrobe():
    sd.rectangle(left_bottom=sd.get_point(210, 145), right_top=sd.get_point(420, 265), color=WARDROBE_COLORS[0])
    sd.vector(start=sd.get_point(213, 143), angle=90, color=WARDROBE_COLORS[0], length=46, width=7)
    sd.vector(start=sd.get_point(416, 143), angle=90, color=WARDROBE_COLORS[0], length=46, width=7)
    sd.vector(start=sd.get_point(210, 143), angle=0, color=WARDROBE_COLORS[1], length=7, width=2)
    sd.vector(start=sd.get_point(216, 143), angle=90, color=WARDROBE_COLORS[1], length=4, width=2)

    sd.vector(start=sd.get_point(216, 147), angle=0, color=WARDROBE_COLORS[1], length=197, width=2)
    sd.vector(start=sd.get_point(413, 143), angle=0, color=WARDROBE_COLORS[1], length=7, width=2)
    sd.vector(start=sd.get_point(413, 143), angle=90, color=WARDROBE_COLORS[1], length=4, width=2)
    sd.vector(start=sd.get_point(419, 143), angle=90, color=WARDROBE_COLORS[1], length=122, width=2)


while True:
    sd.start_drawing()
    footer()
    floor()
    wall()
    window()
    ceiling()
    door()
    clock()
    pictures()
    wardrobe()
    sd.sleep(0.01)
    sd.finish_drawing()
    sd.pause()