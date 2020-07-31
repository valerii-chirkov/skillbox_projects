import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)

snowflakes = []
snowflakes_out_numbers = []


def snowflakes_create(N):  # создать_снежинки(N) - создает N снежинок
    global snowflakes_out_numbers, snowflakes

    for _ in range(N):
        snowflakes.append([sd.random_number(50, 1150), sd.random_number(5, 10), 600])

    snowflakes_out_numbers = []


def snowflakes_draw(color):  # нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
    for snowflake in range(len(snowflakes)):
        parameter_x = snowflakes[snowflake][0]  # для индекс, координата_х из списка координат снежинок
        parameter_y = snowflakes[snowflake][2]  # получить координата_у по индексу

        point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
        sd.snowflake(center=point, length=snowflakes[snowflake][1], color=color)  # нарисовать на новом месте цветом


def snowflakes_shift():  # сдвинуть_снежинки() - сдвигает снежинки на один шаг
    global snowflakes

    for i in range(len(snowflakes)):
        parameter_x = sd.random_number(-10, 10)
        parameter_y = sd.random_number(10, 30)

        snowflakes[i][0] += parameter_x
        snowflakes[i][2] -= parameter_y
        # print(f'moove snowflake {i}, x - {snowflakes[i][0]} , y - {snowflakes[i][2]}')


def snowflakes_numbers_out():  # выдает список номеров снежинок, которые вышли за границу экрана
    global snowflakes_out_numbers

    for index, snowflake in enumerate(snowflakes):
        parameter_y = snowflake[2]
        if (parameter_y <= 0) and (index not in snowflakes_out_numbers):
            snowflakes_out_numbers.append(index)

    if snowflakes_out_numbers:
        # сортируем
        snowflakes_out_numbers.sort()
        # сортируем переворачиваем по возрастанию
        snowflakes_out_numbers.reverse()
        print(snowflakes_out_numbers)
        return snowflakes_out_numbers


def snowflakes_delete(snowflakes_out):  # удалить_снежинки(номера) - удаляет снежинки с номерами из списка
    global snowflakes
    for idx in snowflakes_out:
        if idx <= len(snowflakes)-1:
            snowflakes.remove(snowflakes[idx])
        # del snowflakes[index] - удаляет по индексу
        # snowflakes.remove(snowflakes[index]) удаляет по первому совпадению, названию объекта!


# зачет!
