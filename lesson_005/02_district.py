# -*- coding: utf-8 -*-

# Составить список всех живущих на районе и Вывести на консоль через запятую
# Формат вывода: На районе живут ...
# подсказка: для вывода элементов списка через запятую можно использовать функцию строки .join()
# https://docs.python.org/3/library/stdtypes.html#str.join


from lesson_005.district.central_street.house1.room1 import folks as room1_h1_central_street_room1
from lesson_005.district.central_street.house1.room2 import folks as room1_h1_central_street_room2
from lesson_005.district.central_street.house2.room1 import folks as room1_h2_central_street_room1
from lesson_005.district.central_street.house2.room2 import folks as room1_h2_central_street_room2

from lesson_005.district.soviet_street.house1.room1 import folks as room1_h1_soviet_street_room1
from lesson_005.district.soviet_street.house1.room2 import folks as room1_h1_soviet_street_room2
from lesson_005.district.soviet_street.house2.room1 import folks as room1_h2_soviet_street_room1
from lesson_005.district.soviet_street.house2.room2 import folks as room1_h2_soviet_street_room2

separator = ', '

central_house1 = separator.join(room1_h1_central_street_room1) + ', ' + separator.join(room1_h1_central_street_room2)
central_house2 = separator.join(room1_h2_central_street_room1) + ', ' + separator.join(room1_h2_central_street_room2)
central_street = 'На центральной улице: ' + central_house1 + ', ' + central_house2

soviet_house1 = separator.join(room1_h1_soviet_street_room1) + ', ' + separator.join(room1_h1_soviet_street_room2)
soviet_house2 = separator.join(room1_h2_soviet_street_room1) + ', ' + separator.join(room1_h2_soviet_street_room2)
soviet_street = 'На советской улице: ' + soviet_house1 + ', ' + soviet_house2

print('На районе живут: ')
print(central_street)
print(soviet_street)

