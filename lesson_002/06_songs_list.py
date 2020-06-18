#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть список песен группы Depeche Mode со временем звучания с точностью до долей минут
# Точность указывается в функции round(a, b)
# где a, это число которое надо округлить, а b количество знаков после запятой
# более подробно про функцию round смотрите в документации https://docs.python.org/3/search.html?q=round

violator_songs_list = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83],
]

# TODO Куда делся словарик ? добавил его снова!

# Есть словарь песен группы Depeche Mode
violator_songs_dict = {
    'World in My Eyes': 4.76,
    'Sweetest Perfection': 4.43,
    'Personal Jesus': 4.56,
    'Halo': 4.30,
    'Waiting for the Night': 6.07,
    'Enjoy the Silence': 4.6,
    'Policy of Truth': 4.88,
    'Blue Dress': 4.18,
    'Clean': 5.68,
}

# Распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат приблизительно ХХХ минут

# TODO константы отлично, нужные оставляем не нужные удаляем
WORLD_IN_MY_EYES = violator_songs_list[0][1]
SWEETEST_PERFECTION = violator_songs_list[1][1]
PERSONAL_JESUS = violator_songs_list[2][1]
HALO = violator_songs_list[3][1]
WAITING_FOR_THE_NIGHT = violator_songs_list[4][1]
ENJOY_THE_SILENCE = violator_songs_list[5][1]
POLICY_OF_TRUTH = violator_songs_list[6][1]
BLUE_DRESS = violator_songs_list[7][1]
CLEAN = violator_songs_list[8][1]
three_songs_time = round(SWEETEST_PERFECTION + POLICY_OF_TRUTH + BLUE_DRESS)

# TODO отлично f строки
# TODO Вычисления и преобразования из принта выносим в отдельную переменную
print(f'Три песни звучат {round(HALO + ENJOY_THE_SILENCE + CLEAN)} минут')
# TODO Этот вывод должен быть по словарю violator_songs_dict
print(f'Общее время звучания трех песен: Sweetest Perfection, Policy of Truth и Blue Dress -'
      f' {round(three_songs_time, 2)} минут')


