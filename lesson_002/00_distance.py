#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint

sites = {'Moscow': (550, 370), 'London': (510, 510), 'Paris': (480, 480)}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def distance(city1, city2):
    return ((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2) ** 0.5


# Объявляем переменные
moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

# Расстояния между городами
moscow_london = round(distance(moscow, london))
moscow_paris = round(distance(moscow, paris))
london_paris = round(distance(london, paris))

moscow_distance = {'Расстояние от Москвы до Лондона': f'Расстояние от Москвы до Лондона = {moscow_london}',
                   'Расстояние от Москвы до Парижа': f'Расстояние от Москвы до Парижа = {moscow_paris}'}

london_distance = {'Расстояние от Лондона до Москвы': f'Расстояние от Лондона до Москвы = {moscow_london}',
                   'Расстояние от Лондона до Парижа': f'Расстояние от Лондона до Парижа = {london_paris}'}

paris_distance = {'Расстояние от Парижа до Москвы': f'Расстояние от Парижа до Москвы = {moscow_paris}',
                  'Расстояние от Парижа до Лондона': f'Расстояние от Парижа до Лондона = {london_paris}'}


distances = {moscow_distance['Расстояние от Москвы до Лондона'], moscow_distance['Расстояние от Москвы до Парижа'],
             london_distance['Расстояние от Лондона до Парижа'], london_distance['Расстояние от Лондона до Москвы'],
             paris_distance['Расстояние от Парижа до Москвы'], paris_distance['Расстояние от Парижа до Лондона']}


pprint(distances)




