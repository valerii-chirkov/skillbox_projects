#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {'Moscow': (550, 370), 'London': (510, 510), 'Paris': (480, 480)}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

# Начиная с третьего модуля буду обращать внимание на то что подчеркивает Пайчар. Придерживаемся PEP8
# Большинство комментариев излишне, нужно писать читаемый код тогда комментарии будут не так нужны

# Объявляем переменные
moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

# Расстояние от Москвы
moscow_london = round((((moscow[0] - london[0])**2) + ((moscow[1] - london[1])**2))**0.5)
moscow_paris = round((((moscow[0] - paris[0])**2) + ((moscow[1] - paris[1])**2))**0.5)
london_paris = round((((london[0] - paris[0])**2) + ((london[1] - paris[1])**2))**0.5)

moscow_distance = {'Москва Лондон': f'Расстояние от Москвы до Лондона = {moscow_london}',
                   'Москва Париж': f'Расстояние от Москвы до Парижа = {moscow_paris}'}

london_distance = {'Лондон Москва': f'Расстояние от Лондона до Москвы = {moscow_london}',
                   'Лондон Париж': f'Расстояние от Лондона до Парижа = {london_paris}'}

paris_distance = {'Париж Москва': f'Расстояние от Парижа до Москвы = {moscow_paris}',
                  'Париж Лондон': f'Расстояние от Парижа до Лондона = {london_paris}'}

# Выводим дистанцию по запросу
distances = {moscow_distance['Москва Лондон'], moscow_distance['Москва Париж'],
             london_distance['Лондон Париж'], london_distance['Лондон Москва'],
             paris_distance['Париж Москва'], paris_distance['Париж Лондон']}

# Выводим дистанции по ключу
pprint(distances)




