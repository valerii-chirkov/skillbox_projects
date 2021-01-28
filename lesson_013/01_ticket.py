# -*- coding: utf-8 -*-


# Заполнить все поля в билете на самолет.
# Создать функцию, принимающую параметры: ФИО, откуда, куда, дата вылета,
# и заполняющую ими шаблон билета Skillbox Airline.
# Шаблон взять в файле lesson_013/images/ticket_template.png
# Пример заполнения lesson_013/images/ticket_sample.png
# Подходящий шрифт искать на сайте ofont.ru
from PIL import Image, ImageDraw, ImageFont, ImageColor

template = 'images/ticket_template.png'
font_path = 'font_dud.ttf'


def make_ticket(fio, from_, to, date, ):
    # default_size = (672, 401)
    im = Image.open(template)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(font_path, size=16)
    params = fio, from_, to, date
    positions = list()

    # coordinates iteration
    for i in range(len(params)-1):  #  так?
        # TODO Значительно удобнее был бы список словарей с ключами "текст" и "координаты"
        positions.append([45, im.size[1] - 280 + 70*i])
    positions.append([285, im.size[1] - 280 + 70*2])

    def write(position, param):
        draw.text(position, param, font=font, fill=ImageColor.colormap['black'])

    # write each line
    for i in range(len(params)):
        write(position=positions[i], param=params[i])

    # save
    out_path = 'img.jpg'
    im = im.convert('RGB')
    im.save(out_path)


make_ticket('Valerii Chirkov', 'Barnaul, Russia', 'Moscow, Russia', '27 Jan 2021')
# Усложненное задание (делать по желанию).
# Написать консольный скрипт c помощью встроенного python-модуля argparse.
# Скрипт должен принимать параметры:
#   --fio - обязательный, фамилия.
#   --from - обязательный, откуда летим.
#   --to - обязательный, куда летим.
#   --date - обязательный, когда летим.
#   --save_to - необязательный, путь для сохранения заполненнего билета.
# и заполнять билет.

