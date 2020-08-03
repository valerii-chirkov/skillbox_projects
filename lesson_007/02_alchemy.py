# -*- coding: utf-8 -*-

# Создать прототип игры Алхимия: при соединении двух элементов получается новый.
# Реализовать следующие элементы: Вода, Воздух, Огонь, Земля, Шторм, Пар, Грязь, Молния, Пыль, Лава.
# Каждый элемент организовать как отдельный класс.
# Таблица преобразований:
#   Вода + Воздух = Шторм
#   Вода + Огонь = Пар
#   Вода + Земля = Грязь
#   Воздух + Огонь = Молния
#   Воздух + Земля = Пыль
#   Огонь + Земля = Лава

# Сложение элементов реализовывать через __add__
# Если результат не определен - то возвращать None
# Вывод элемента на консоль реализовывать через __str__
#
# Примеры преобразований:
#   print(Water(), '+', Air(), '=', Water() + Air())
#   print(Fire(), '+', Air(), '=', Fire() + Air())


class Water:
    def __add__(self, other):
        if isinstance(other, Air):
            return Storm()
        elif isinstance(other, Fire):
            return Steam()
        elif isinstance(other, Earth):
            return Dirt()
        elif isinstance(other, Water):
            return Lake()
        else:
            return None

    def __str__(self):
        return 'WATER'


class Air:
    def __add__(self, other):
        if isinstance(other, Water):
            return Storm()
        elif isinstance(other, Fire):
            return Thunder()
        elif isinstance(other, Earth):
            return Dust()
        else:
            return None

    def __str__(self):
        return 'AIR'


class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam()
        elif isinstance(other, Air):
            return Thunder()
        elif isinstance(other, Earth):
            return Lava()
        else:
            return None

    def __str__(self):
        return 'FIRE'


class Earth:
    def __add__(self, other):
        if isinstance(other, Water):
            return Dirt()
        elif isinstance(other, Air):
            return Dust()
        elif isinstance(other, Fire):
            return Lava()
        else:
            return None

    def __str__(self):
        return 'EARTH'


class Storm:
    def __str__(self):
        return 'STORM🌪'


class Steam:
    def __str__(self):
        return 'STEAM🧖‍'


class Dirt:
    def __str__(self):
        return 'DIRT💩'


class Thunder:
    def __add__(self, other):
        if isinstance(other, Lake):
            return Fish()
        else:
            return None

    def __str__(self):
        return 'THUNDER⚡'


class Dust:
    def __str__(self):
        return 'DUST️🧹'


class Lava:
    def __str__(self):
        return 'LAVA🔥'


class Lake:
    def __add__(self, other):
        if isinstance(other, Thunder):
            return Fish()
        else:
            return None

    def __str__(self):
        return 'LAKE💦'


class Fish:
    def __str__(self):
        return 'FISH🐠'


#   Вода + Воздух = Шторм
print(Water(), '+', Air(), '=', Water() + Air())

#   Вода + Огонь = Пар
print(Water(), '+', Fire(), '=', Water() + Fire())

#   Вода + Земля = Грязь
print(Water(), '+', Earth(), '=', Water() + Earth())

#   Воздух + Огонь = Молния
print(Air(), '+', Fire(), '=', Air() + Fire())

#   Воздух + Земля = Пыль
print(Air(), '+', Earth(), '=', Air() + Earth())

#   Огонь + Земля = Лава
print(Fire(), '+', Earth(), '=', Fire() + Earth())

# Новый эелемент
#   Вода + Вода = Озеро
print(Water(), '+', Water(), '=', Water() + Water())

# Соединяем элементы второго уровня
#   Озеро + Молния = Рыба
print(Lake(), '+', Thunder(), '=', Lake() + Thunder())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
