# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse

TEMPLATE_TICKET = '/Users/valeriichirkov/PycharmProjects/python_base/lesson_013/images/ticket_template.png'
FONT_PATH = '/Users/valeriichirkov/PycharmProjects/python_base/lesson_013/font_dud.ttf'
# TODO без абсолютного пути не видит файлы
TICKET_OUT_PATH = 'ticket_out.jpg'

parser = argparse.ArgumentParser(description='Filling a ticket')
parser.add_argument('-q', '--fio', metavar='', type=str, required=True, help='Your full name.')
parser.add_argument('-w', '--from_', metavar='', type=str, required=True, help='Departure')
parser.add_argument('-e', '--to', metavar='', type=str, required=True, help='Destination')
parser.add_argument('-r', '--date', metavar='', type=str, required=True, help='Flight date.')
parser.add_argument('-t', '--name', metavar='', type=str, required=False, help='Ticket path')
args = parser.parse_args()


def make_ticket(fio, from_, to, date):
    # default_size = (672, 401)
    im = Image.open(TEMPLATE_TICKET)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(FONT_PATH, size=16)

    # coordinates iteration
    filling_data = [
        {'text': fio, 'cords': (45, im.size[1] - 280 + 70*0)},
        {'text': from_, 'cords': (45, im.size[1] - 280 + 70 * 1)},
        {'text': to, 'cords': (45, im.size[1] - 280 + 70 * 2)},
        {'text': date, 'cords': (285, im.size[1] - 280 + 70*2)},
    ]

    # define a function to write information
    def write(position, param):
        draw.text(position, param, font=font, fill=ImageColor.colormap['black'])

    # write each line
    for i in range(len(filling_data)):
        line = filling_data[i]
        key = line.get('text')
        write(position=filling_data[i]['cords'], param=key)

    # save
    im = im.convert('RGB')
    im.save(TICKET_OUT_PATH)


# TODO приходится писать в консоли без пробелов, потому что он слова после пробела воспринимает за другие аргументы,
# TODO как можно это исправить?
make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date)
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.


