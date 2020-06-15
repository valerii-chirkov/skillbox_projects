#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {'Moscow': (550, 370), 'London': (510, 510), 'Paris': (480, 480)}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

#Объявляем переменные
moscow = sites['Moscow']
london = sites['London']
paris = sites['Paris']

#Расстояние от Москвы
moscow_london = round((((moscow[0] - london[0])**2) + ((moscow[1] - london[1])**2))**0.5)
moscow_paris = round((((moscow[0] - paris[0])**2) + ((moscow[1] - paris[1])**2))**0.5)

#Расстояние от Лондона
london_moscow = round((((london[0] - moscow[0])**2) + ((london[1] - moscow[1])**2))**0.5)
london_paris = round((((london[0] - paris[0])**2) + ((london[1] - paris[1])**2))**0.5)

#Расстояние от Парижа
paris_moscow = round((((paris[0] - moscow[0])**2) + ((paris[1] - moscow[1])**2))**0.5)
paris_london = round((((paris[0] - london[0])**2) + ((paris[1] - london[1])**2))**0.5)

#Приводим к виду  {                ключ                  :                значение                      }
moscow_distance = {'Расстояние от Москвы до Лондона':f'Расстояние от Москвы до Лондона = {moscow_london}',
                   'Расстояние от Москвы до Парижа':f'Расстояние от Москвы до Парижа = {moscow_paris}'}

london_distance = {'Расстояние от Лондона до Москвы':f'Расстояние от Лондона до Москвы = {london_moscow}',
                   'Расстояние от Лондона до Парижа':f'Расстояние от Лондона до Парижа = {london_paris}'}

paris_distance = {'Расстояние от Парижа до Москвы':f'Расстояние от Парижа до Москвы = {paris_moscow}',
                  'Расстояние от Парижа до Лондона':f'Расстояние от Парижа до Лондона = {paris_london}'}

#Выводим дистанцию по запросу
distances = {moscow_distance['Расстояние от Москвы до Лондона'], moscow_distance['Расстояние от Москвы до Парижа'],
             london_distance['Расстояние от Лондона до Парижа'], london_distance['Расстояние от Лондона до Москвы'],
             paris_distance['Расстояние от Парижа до Москвы'], paris_distance['Расстояние от Парижа до Лондона']}

#Выводим дистанции по ключу
pprint(distances)




