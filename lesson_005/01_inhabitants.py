# -*- coding: utf-8 -*-

# Вывести на консоль жителей комнат (модули room_1 и room_2)
# Формат: В комнате room_1 живут: ...

from lesson_005.room_1 import folks as folks1
from lesson_005.room_2 import folks as folks2

separator = ', '
print(f'В комнате room_1 живут: {separator.join(folks1)}')
print(f'В комнате room_2 живут: {separator.join(folks2)}')

# зачет!
