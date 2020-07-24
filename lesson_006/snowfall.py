import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)
snowflakes = []
snowflakes_out = []


def snowflakes_create():  # создать_снежинки(N) - создает N снежинок
    for i in range(10):
        snowflakes.append([sd.random_number(50, 1150), sd.random_number(5, 10), 600, i])


def snowflakes_draw():  # нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
    for snowflake in range(10):
        parameter_x = snowflakes[snowflake][0]  # для индекс, координата_х из списка координат снежинок
        parameter_y = snowflakes[snowflake][2]  # получить координата_у по индексу

        point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
        sd.snowflake(center=point, length=snowflakes[snowflake][1])  # нарисовать снежинку на новом месте белым цветом

        snowflakes[snowflake][0] = parameter_x
        snowflakes[snowflake][2] = parameter_y


def snowflakes_shift():  # сдвинуть_снежинки() - сдвигает снежинки на один шаг
    for i in range(10):
        parameter_x = snowflakes[i][0]  # для индекс, координата_х из списка координат снежинок
        parameter_y = snowflakes[i][2]

        parameter_x += sd.random_number(-10, 10)
        parameter_y -= sd.random_number(10, 30)


def snowflakes_numbers_out():  # выдает список номеров снежинок, которые вышли за границу экрана
    for i in range(10):
        parameter_y = snowflakes[i][2]
        if parameter_y < 0:
            snowflakes_out.append([i, snowflakes[i][3]])
            return snowflakes_out


def snowflakes_delete():  # удалить_снежинки(номера) - удаляет снежинки с номерами из списка
    for i in range(10):
        parameter_y = snowflakes[i][2]
        if parameter_y < 0:
            del snowflakes[snowflakes_out[i]]


# while True:
#     sd.start_drawing()
#     snowflakes_create()
#     snowflakes_draw()
#     snowflakes_shift()
#     snowflakes_numbers_out()
#     snowflakes_delete()
#     sd.sleep(0.1)
#     sd.finish_drawing()
#     sd.pause()

