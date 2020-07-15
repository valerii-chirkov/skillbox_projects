import simple_draw as sd
point = sd.get_point(100, 500)
traces = []

# TODO Солнце доработать оно должно быть с лучами и переливаться!
def sun():
    sd.circle(point, radius=50, color=sd.COLOR_YELLOW, width=50)


# TODO Убрать вызов, делать его в главном модуле
sun()