# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join

from lesson_005.district.central_street.house1 import room1 as room1_h1_central_street, room2 as room2_h1_central_street
from lesson_005.district.soviet_street.house1 import room1 as room1_h1_soviet_street, room2 as room2_h1_soviet_street
from lesson_005.district.soviet_street.house2 import room1 as room1_h2_soviet_street, room2 as room2_h2_soviet_street

district_inhabitants = room1_h1_central_street.folks + room2_h1_central_street.folks + \
      room1_h1_soviet_street.folks + room2_h1_soviet_street.folks + \
      room1_h2_soviet_street.folks + room2_h2_soviet_street.folks

print('На районе живут: ', district_inhabitants)

# TODO .join почему-то выводил ошибку AttributeError: 'list' object has no attribute 'join'