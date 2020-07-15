import simple_draw as sd
sd.resolution = (1200, 600)

add_parameters = []


def snowflake_parameters():
    for _ in range(3):
        add_parameters.append([sd.random_number(50, 1150), sd.random_number(10, 100), 600])


def snowflakes_fall():
    snowflake_parameters()
    level_snow = 10
    # TODO вот про этот цикл while я вам говорил его тут не должно быть, главный цикл будет один в основном файле,
    # TODO он и будет двигать снежинку
    while True:  # навсегда
        sd.start_drawing()  # начать рисование кадра
        for i in range(3):
            parameter_x = add_parameters[i][0]  # для индекс, координата_х из списка координат снежинок
            parameter_y = add_parameters[i][2]  # получить координата_у по индексу

            point = sd.get_point(parameter_x, parameter_y)  # создать точку отрисовки снежинки
            sd.snowflake(center=point, length=add_parameters[i][1], color=sd.background_color)  # нарис снеж цветом фона

            # Поправил
            parameter_x += sd.random_number(-30, 30)
            parameter_y -= sd.random_number(10, 30)

            point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
            sd.snowflake(center=point, length=add_parameters[i][1])  # нарисовать снежинку на новом месте белым цветом

            add_parameters[i][0] = parameter_x
            add_parameters[i][2] = parameter_y

            if level_snow > parameter_y:
                level_snow += 1
                add_parameters[i][2] = 600

        sd.finish_drawing()  # закончить рисование кадра

        sd.sleep(0.1)  # немного поспать
        if sd.user_want_exit():  # если пользователь хочет выйти
            break  # прервать цикл

# TODO Убрать вызов, делать его в главном модуле
snowflakes_fall()
sd.pause()
