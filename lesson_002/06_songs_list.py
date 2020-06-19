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

# Распечатайте общее время звучания трех песен: 'Sweetest Perfection', 'Policy of Truth' и 'Blue Dress'
#   А другие три песни звучат приблизительно ХХХ минут
SWEETEST_PERFECTION = violator_songs_list[1][1]
HALO = violator_songs_list[3][1]
ENJOY_THE_SILENCE = violator_songs_list[5][1]
POLICY_OF_TRUTH = violator_songs_list[6][1]
BLUE_DRESS = violator_songs_list[7][1]
CLEAN = violator_songs_list[8][1]

three_songs_time_SPB = round(SWEETEST_PERFECTION + POLICY_OF_TRUTH + BLUE_DRESS)
three_songs_titles_SPB = {violator_songs_list[1][0], violator_songs_list[6][0], violator_songs_list[7][0]}
three_songs_time_HEC = round(HALO + ENJOY_THE_SILENCE + CLEAN)

print(f'Три песни звучат {three_songs_time_HEC} минут')
print(f'Общее время звучания трех песен: {three_songs_titles_SPB} = {three_songs_time_SPB} минут')


