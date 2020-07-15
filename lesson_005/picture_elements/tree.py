import simple_draw as sd

sd.set_screen_size(width=1200, height=600)
width = 20


def draw_branches(point=sd.get_point(840, 100), angle=90, length=50, width=20):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=width)
    v1.draw(color=(160, 82, 45))
    if 14 >= length >= 10:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw(color=sd.COLOR_DARK_GREEN)
    if length < 10:
        return
    next_point = v1.end_point
    next_angle1 = angle - (sd.random_number(110, 112) / 100 * 30)
    next_angle2 = angle + (sd.random_number(110, 112) / 100 * 30)
    next_length = length * (sd.random_number(110, 112) / 100 * 0.75)
    next_width = int(width * 0.75)
    draw_branches(next_point, next_angle1, next_length, next_width)
    draw_branches(next_point, next_angle2, next_length, next_width)
