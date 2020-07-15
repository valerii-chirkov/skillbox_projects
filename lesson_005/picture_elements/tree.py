import simple_draw as sd

sd.set_screen_size(width=1200, height=600)


def draw_branches(point=sd.get_point(900, 100), angle=90, length=70):
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
    v1.draw(color=sd.COLOR_DARK_GREEN)
    # TODO большое повторение однотипного кода сделать функцию
    if length >= 70:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=30)
        v1.draw(color=(160, 82, 45))
    if 69 >= length >= 60:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=25)
        v1.draw(color=(160, 82, 45))
    if 59 >= length >= 50:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=20)
        v1.draw(color=(160, 82, 45))
    if 49 >= length >= 40:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=15)
        v1.draw(color=(160, 82, 45))
    if 39 >= length >= 30:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=10)
        v1.draw(color=(160, 82, 45))
    if 29 >= length >= 20:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=5)
        v1.draw(color=(160, 82, 45))
    if 19 >= length >= 10:
        v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=3)
        v1.draw(color=sd.COLOR_DARK_GREEN)
    if length < 10:
        return
    next_point = v1.end_point
    next_angle1 = angle - (sd.random_number(100, 140) / 100 * 30)
    next_angle2 = angle + (sd.random_number(100, 140) / 100 * 30)
    next_length = length * (sd.random_number(100, 120) / 100 * 0.75)
    draw_branches(next_point, next_angle1, next_length)
    draw_branches(next_point, next_angle2, next_length)

# TODO Убрать вызов, делать его в главном модуле
draw_branches()
