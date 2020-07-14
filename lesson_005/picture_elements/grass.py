import simple_draw as sd

sd.set_screen_size(width=1200, height=600)


def grass():
    sd.rectangle(left_bottom=sd.get_point(0, 0), right_top=sd.get_point(1200, 150), color=(71, 232, 17), width=0)


grass()


