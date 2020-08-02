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


class Level1:

    class Water:
        def __add__(self, other):
            if other == Level1.Air():
                return Level2.Storm
            elif other == Level1.Fire():
                return Level2.Steam
            elif other == Level1.Earth():
                return Level2.Dirt
            else:
                return None

        def __str__(self):
            return 'WATER'

    class Air:
        def __add__(self, other):
            if other is Level1.Water():
                return Level2.Storm
            elif other is Level1.Fire():
                return Level2.Thunder
            elif other is Level1.Earth():
                return Level2.Dust
            else:
                return None

        def __str__(self):
            return 'AIR'

    class Fire:
        def __add__(self, other):
            if other is Level1.Water:
                return Level2.Steam
            elif other is Level1.Air:
                return Level2.Thunder
            elif other is Level1.Earth:
                return Level2.Lava
            else:
                return None

        def __str__(self):
            return 'FIRE'

    class Earth:
        def __add__(self, other):
            if other is Level1.Water:
                return Level2.Dirt
            elif other is Level1.Air:
                return Level2.Dust
            elif other is Level1.Fire:
                return Level2.Lava
            else:
                return None

        def __str__(self):
            return 'EARTH'


class Level2:

    class Storm:
        def __str__(self):
            return 'STORM'

    class Steam:
        def __str__(self):
            return 'STEAM'

    class Dirt:
        def __str__(self):
            return 'DIRT'

    class Thunder:
        def __str__(self):
            return 'THUNDER'

    class Dust:
        def __str__(self):
            return 'DUST'

    class Lava:
        def __str__(self):
            return 'LAVA'


#   Вода + Воздух = Шторм
print(Level1.Water(), '+', Level1.Air(), '=', Level1.Water() + Level1.Air())

#   Вода + Огонь = Пар
print(Level1.Water(), '+', Level1.Fire(), '=', Level1.Water() + Level1.Fire())

#   Вода + Земля = Грязь
print(Level1.Water(), '+', Level1.Earth(), '=', Level1.Water() + Level1.Earth())

#   Воздух + Огонь = Молния
print(Level1.Air(), '+', Level1.Fire(), '=', Level1.Air() + Level1.Fire())

#   Воздух + Земля = Пыль
print(Level1.Air(), '+', Level1.Earth(), '=', Level1.Air() + Level1.Earth())

#   Огонь + Земля = Лава
print(Level1.Fire(), '+', Level1.Earth(), '=', Level1.Fire() + Level1.Earth())


# Усложненное задание (делать по желанию)
# Добавить еще элемент в игру.
# Придумать что будет при сложении существующих элементов с новым.
