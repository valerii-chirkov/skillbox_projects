import simple_draw as sd

sd.resolution = (1200, 600)
sd.background_color = (15, 116, 235)

snowflakes = []
snowflakes_out_numbers = []
amount = 0


def snowflakes_create(N):  # создать_снежинки(N) - создает N снежинок
    global amount
    amount = N
    for _ in range(amount):
        snowflakes.append([sd.random_number(50, 1150), sd.random_number(5, 10), 600])


def snowflakes_draw(color):  # нарисовать_снежинки_цветом(color) - отрисовывает все снежинки цветом color
    for snowflake in range(amount):
        parameter_x = snowflakes[snowflake][0]  # для индекс, координата_х из списка координат снежинок
        parameter_y = snowflakes[snowflake][2]  # получить координата_у по индексу

        point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
        sd.snowflake(center=point, length=snowflakes[snowflake][1], color=color)  # нарисовать на новом месте цветом


def snowflakes_shift():  # сдвинуть_снежинки() - сдвигает снежинки на один шаг
    for i in range(amount):
        parameter_x = sd.random_number(-10, 10)
        parameter_y = sd.random_number(10, 30)

        snowflakes[i][0] += parameter_x
        snowflakes[i][2] -= parameter_y


# TODO индексы можно записать вот так:
# TODO заводим цикл по snowflakes используя enumerate, в цикле получаем сразу index и параметры_снежинки(список)
# TODO Потом условие если снежинка по Y <= 0 и индекса нет в списке snowflakes_out_numbers(это список индексов будет, нейминг)
# TODO то мы добавляем этот индекс в nowflakes_out_numbers(это список индексов будет, нейминг)
# TODO Потом вне цикла делаем проверку если nowflakes_out_numbers не пустой, то возвращаем его, ретурном!

def snowflakes_numbers_out():  # выдает список номеров снежинок, которые вышли за границу экрана
    global snowflakes_out_numbers
    y = 0
    for i in range(len(snowflakes)):
        parameter_y = snowflakes[i][2]
        y += 1
        if parameter_y <= 50:
            snowflakes_out_numbers.append(y)
            #print(snowflakes_out_numbers)

    if snowflakes_out_numbers:
        return snowflakes_out_numbers


def snowflakes_delete():  # удалить_снежинки(номера) - удаляет снежинки с номерами из списка
    for i in range(len(snowflakes_out_numbers)):
        if snowflakes_out_numbers[i]:
            snowflakes.remove(snowflakes[i])
            snowflakes_out_numbers.remove(snowflakes_out_numbers[i])

