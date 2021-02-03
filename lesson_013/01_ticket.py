# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
from PIL import Image, ImageDraw, ImageFont, ImageColor
import argparse

# constants (may be changed)
TEMPLATE_TICKET = 'lesson_013/images/ticket_template.png'
FONT_PATH = 'lesson_013/font_dud.ttf'

# using argparse module
parser = argparse.ArgumentParser(description='Filling a ticket')
parser.add_argument('-q', '--fio', metavar='', type=str, required=True, help='Your full name.')
parser.add_argument('-w', '--from_', metavar='', type=str, required=True, help='Departure')
parser.add_argument('-e', '--to', metavar='', type=str, required=True, help='Destination')
parser.add_argument('-r', '--date', metavar='', type=str, required=True, help='Flight date.')
parser.add_argument('-t', '--save_to', metavar='', type=str, required=False, help='Ticket path', default='ticket_out.jpg')
args = parser.parse_args()


def make_ticket(fio, from_, to, date, save_to):
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
    im.save(args.save_to)


make_ticket(fio=args.fio, from_=args.from_, to=args.to, date=args.date, save_to=args.save_to)
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

# python3 lesson_013/01_ticket.py -q ValeriiChirkov -w Barnaul,Russia -e Moscow,Russia -r 25Feb2021
# TODO так тоже запускается

# python3 01_ticket.py -q ValeriiChirkov -w Barnaul,Russia -e Moscow,Russia -r 25Feb2021
# TODO так нет
