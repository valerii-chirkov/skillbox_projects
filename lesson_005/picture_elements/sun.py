import simple_draw as sd
import random


def sun():
    color = random.choice(sd.COLOR_RED, sd.COLOR_ORANGE, sd.COLOR_YELLOW)

    for delta in range(0, 361, 90):
        function = sd.get_vector(start_point=sd.get_point(100, 480), angle=delta + 145, length=80, width=80)
        function.draw(color=color)
