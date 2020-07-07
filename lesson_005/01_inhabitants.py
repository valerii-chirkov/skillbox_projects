# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from lesson_005.room_1 import folks

# TODO Есть еще жильцы в других комнатах!
# TODO А если жильцов будет больше 100, используйте format, join
print(f'В комнате room_1 живут: {folks[0]} и {folks[1]}')
