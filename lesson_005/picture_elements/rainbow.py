import simple_draw as sd
sd.set_screen_size(width=1200, height=600)
point = sd.get_point(250, -180)
step = 30
rainbow_colors = (sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW, sd.COLOR_GREEN,
                  sd.COLOR_CYAN, sd.COLOR_BLUE, sd.COLOR_PURPLE)


def rainbow():
    radius = 850
    for color in rainbow_colors:
        radius += step
        sd.circle(center_position=point, radius=radius, color=color, width=30)


rainbow()

