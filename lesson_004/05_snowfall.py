# -*- coding: utf-8 -*-
from dis import dis
import simple_draw as sd
sd.resolution = (1200, 600)
# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длинн лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()
# input_amount = int(input('Введите количество снежинок: '))
# add_parameters = []
#
#
# def snowflake_parameters(input_amount):
#     for _ in range(input_amount):
#         add_parameters.append([sd.random_number(100, 800), sd.random_number(10, 100), 600])
#
#
# def snowflakes_fall():
#     # snowflake_coordinate_x = sd.random_number(100, 800)
#     # snowflake_coordinate_y = 600
#     # snowflake_ray = sd.random_number(10, 100)
#     snowflake_parameters(input_amount)
#
#     while True:
#         sd.clear_screen()
#
#         for i in range(input_amount):
#             parameter_x = add_parameters[i][0]
#             parameter_y = add_parameters[i][2]
#             parameter_length = add_parameters[i][1]
#
#             point = sd.get_point(parameter_x, parameter_y)
#             sd.snowflake(center=point, length=parameter_length)
#
#             add_parameters[i][0] += 10
#             add_parameters[i][2] -= 10
#
#             if parameter_y < 50:
#                 sd.clear_screen()
#                 add_parameters[i][0] = sd.random_number(100, 800)
#                 add_parameters[i][2] = 600
#         sd.sleep(0.1)
#         if sd.user_want_exit():
#             break
#
#
# snowflakes_fall()
#
#
# sd.pause()

# Можно делать вторую часть


# Примерный алгоритм отрисовки снежинок
#   навсегда
#     очистка экрана
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       изменить координата_у и запомнить её в списке по индексу
#       создать точку отрисовки снежинки по координатам
#       нарисовать снежинку белым цветом в этой точке
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл


# Часть 2 (делается после зачета первой части)
#
# Ускорить отрисовку снегопада
# - убрать clear_screen() из цикла: полная очистка всего экрана - долгая операция.
# - использовать хак для стирания старого положения снежинки:
#       отрисуем её заново на старом месте, но цветом фона (sd.background_color) и она исчезнет!
# - использовать функции sd.start_drawing() и sd.finish_drawing()
#       для начала/окончания отрисовки кадра анимации
# - между start_drawing и finish_drawing библиотека sd ничего не выводит на экран,
#       а сохраняет нарисованное в промежуточном буфере, за счет чего достигается ускорение анимации
# - в момент вызова finish_drawing все нарисованное в буфере разом покажется на экране
#
# Примерный алгоритм ускоренной отрисовки снежинок
#   навсегда
#     начать рисование кадра
#     для индекс, координата_х из списка координат снежинок
#       получить координата_у по индексу
#       создать точку отрисовки снежинки
#       нарисовать снежинку цветом фона
#       изменить координата_у и запомнить её в списке по индексу
#       создать новую точку отрисовки снежинки
#       нарисовать снежинку на новом месте белым цветом
#     закончить рисование кадра
#     немного поспать
#     если пользователь хочет выйти
#       прервать цикл

# TODO все сделал по алгоритму, почему-то не работает

input_amount = int(input('Введите количество снежинок: '))
add_parameters = []


def snowflake_parameters(input_amount):
    for _ in range(input_amount):
        add_parameters.append([sd.random_number(100, 800), sd.random_number(10, 100), 600])


def snowflakes_fall():
    # snowflake_coordinate_x = sd.random_number(100, 800)
    # snowflake_coordinate_y = 600
    # snowflake_ray = sd.random_number(10, 100)
    snowflake_parameters(input_amount)
    while True:  # навсегда
        sd.start_drawing()  # начать рисование кадра
        for i in range(input_amount):
            parameter_x = add_parameters[i][0]  # для индекс, координата_х из списка координат снежинок
            parameter_y = add_parameters[i][2]  # получить координата_у по индексу

            point = sd.get_point(parameter_x, parameter_y)  # создать точку отрисовки снежинки
            sd.snowflake(center=point, length=add_parameters[i][1], color=sd.background_color)  # нарис снеж цветом фона

            add_parameters[i][2] -= 10  # изменить координата_у и запомнить её в списке по индексу
            add_parameters[i][0] += 10
            parameter_x = add_parameters[i][0]  # для индекс, координата_х из списка координат снежинок
            parameter_y = add_parameters[i][2]

            point = sd.get_point(parameter_x, parameter_y)  # создать новую точку отрисовки снежинки
            sd.snowflake(center=point, length=add_parameters[i][1])  # нарисовать снежинку на новом месте белым цветом

            if parameter_y < 50:
                return

        sd.finish_drawing()  # закончить рисование кадра

        sd.sleep(0.1)  # немного поспать
        if sd.user_want_exit():  # если пользователь хочет выйти
            break  # прервать цикл


snowflakes_fall()


sd.pause()

# TODO предлагаю вам сделать усложненное задание

# Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугоб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg

