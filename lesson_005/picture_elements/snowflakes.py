import simple_draw as sd
sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)
add_parameters = []
add_drift_parameters = []


def snowflake_parameters():
    for _ in range(3):
        add_parameters.append([sd.random_number(250, 255), sd.random_number(5, 10), 600])


def snowdrift_parameters():
    for i in range(500):
        add_drift_parameters.append([sd.random_number(0, 1200), sd.random_number(5, 10), sd.random_number(0, 160)])


def snowdrift():
    snowdrift_parameters()
    for i in range(500):
        parameter_drift_x = add_drift_parameters[i][0]  # для индекс, координата_х из списка координат снежинок
        parameter_drift_y = add_drift_parameters[i][2]
        point = sd.get_point(parameter_drift_x, parameter_drift_y)  # создать новую точку отрисовки снежинки
        sd.snowflake(center=point, length=add_drift_parameters[i][1])


def snowflakes_fall():
    snowflake_parameters()
    level_snow = 140

    for i in range(3):
        parameter_x = add_parameters[i][0]  # для индекс, координата_х из списка координат снежинок
        parameter_y = add_parameters[i][2]  # получить координата_у по индексу

        if parameter_y <= 150:
            sd.background_color = (71, 232, 17)
        else:
            sd.background_color = (15, 116, 235)
        point = sd.get_point(parameter_x, parameter_y)  # создать точку отрисовки снежинки
        sd.snowflake(center=point, length=add_parameters[i][1], color=sd.background_color)  # нарис снеж цветом фона

        parameter_x += sd.random_number(-10, 10)
        parameter_y -= sd.random_number(10, 30)

        point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
        sd.snowflake(center=point, length=add_parameters[i][1])  # нарисовать снежинку на новом месте белым цветом

        add_parameters[i][0] = parameter_x
        add_parameters[i][2] = parameter_y

        if level_snow > parameter_y:
            level_snow += 1
            add_parameters[i][2] = 600
