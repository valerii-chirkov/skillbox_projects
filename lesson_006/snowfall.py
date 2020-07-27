import simple_draw as sd


sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)

snowflakes = []
snowflakes_out = []
N = int(input('Введите количество снежинок: '))
snowflakes_out_numbers = []


def snowflakes_create():  # создать_снежинки(N) - создает N снежинок
    for _ in range(N):
        snowflakes.append([sd.random_number(50, 1150), sd.random_number(5, 10), 600])


def snowflakes_draw(color):  # нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
    for snowflake in range(N):
        parameter_x = snowflakes[snowflake][0]  # для индекс, координата_х из списка координат снежинок
        parameter_y = snowflakes[snowflake][2]  # получить координата_у по индексу

        point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
        sd.snowflake(center=point, length=snowflakes[snowflake][1], color=color)  # нарисовать на новом месте цветом


def snowflakes_shift():  # сдвинуть_снежинки() - сдвигает снежинки на один шаг
    for i in range(N):
        parameter_x = sd.random_number(-10, 10)
        parameter_y = sd.random_number(10, 30)

        parameter_x = snowflakes[i][0]  # для индекс, координата_х из списка координат снежинок
        parameter_y = snowflakes[i][2]


def snowflakes_numbers_out():  # выдает список номеров снежинок, которые вышли за границу экрана
    global snowflakes_out_numbers
    for i in snowflakes_out:
        parameter_y = snowflakes[i][2]
        if parameter_y < 0:
            snowflakes_out_numbers += enumerate(snowflakes_out)
        return snowflakes_out_numbers


def snowflakes_delete():  # удалить_снежинки(номера) - удаляет снежинки с номерами из списка
    for i in snowflakes_out_numbers:
        if enumerate(snowflakes_out[i]) == snowflakes_out_numbers[i]:
            del snowflakes[snowflakes_out[i]]


