#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Есть словарь кодов товаров

goods = {
    'Лампа': '12345',
    'Стол': '23456',
    'Диван': '34567',
    'Стул': '45678',
}

# Есть словарь списков количества товаров на складе.

store = {
    '12345': [
        {'quantity': 27, 'price': 42},
    ],
    '23456': [
        {'quantity': 22, 'price': 510},
        {'quantity': 32, 'price': 520},
    ],
    '34567': [
        {'quantity': 2, 'price': 1200},
        {'quantity': 1, 'price': 1150},
    ],
    '45678': [
        {'quantity': 50, 'price': 100},
        {'quantity': 12, 'price': 95},
        {'quantity': 43, 'price': 97},
    ],
}
# Присваиваем переменной код товара:
lamp_code = goods['Лампа']
table_code = goods['Стол']
sofa_code = goods['Диван']
chair_code = goods['Стул']

# Присваиваем переменной первое значение кода:
lamps_item = store[lamp_code][0]
tables_item1 = store[table_code][0]
tables_item2 = store[table_code][1]
sofas_item1 = store[sofa_code][0]
sofas_item2 = store[sofa_code][1]
chairs_item1 = store[chair_code][0]
chairs_item2 = store[chair_code][1]
chairs_item3 = store[chair_code][2]
# Присваиваем переменной количество по ключу:
lamps_quantity = lamps_item['quantity']
tables_quantity1 = tables_item1['quantity']
tables_quantity2 = tables_item2['quantity']
sofas_quantity1 = sofas_item1['quantity']
sofas_quantity2 = sofas_item2['quantity']
chairs_quantity1 = chairs_item1['quantity']
chairs_quantity2 = chairs_item2['quantity']
chairs_quantity3 = chairs_item3['quantity']

# Присваиваем переменной стоимость по ключу:
lamps_price = lamps_item['price']
tables_price1 = tables_item1['price']
tables_price2 = tables_item2['price']
sofas_price1 = sofas_item1['price']
sofas_price2 = sofas_item2['price']
chairs_price1 = chairs_item1['price']
chairs_price2 = chairs_item2['price']
chairs_price3 = chairs_item3['price']

# Присваиваем переменной сумму значений:
lamps_cost = lamps_quantity * lamps_price
tables_cost = tables_quantity1 * tables_price1 + tables_quantity2 * tables_price2
sofas_cost = sofas_quantity1 * sofas_price1 + sofas_quantity2 * sofas_price2
chairs_cost = chairs_quantity1 * chairs_price1 + chairs_quantity2 * chairs_price2 + chairs_quantity3 * chairs_price3

tables_quantity_overall = tables_quantity1 + tables_quantity2
sofas_quantity_overall = sofas_quantity1 + sofas_quantity2
chairs_quantity_overall = chairs_quantity1 + chairs_quantity2 + chairs_quantity3
# Выводим в консоль:
print('Лампа -', lamps_quantity, 'шт, стоимость', lamps_cost, 'руб')
print('Стол -', tables_quantity_overall, 'шт, стоимость', tables_cost, 'руб')
print('Диван -', sofas_quantity_overall, 'шт, стоимость', sofas_cost, 'руб')
print('Стул -', chairs_quantity_overall, 'шт, стоимость', chairs_cost, 'руб')


# Вывести стоимость каждого вида товара на складе:

# один раз распечать сколько всего столов и их общая стоимость,
# один раз распечать сколько всего стульев и их общая стоимость,
#   и т.д. на складе
# Формат строки <товар> - <кол-во> шт, стоимость <общая стоимость> руб

# WARNING для знающих циклы: БЕЗ циклов. Да, с переменными; да, неэффективно; да, копипаста.
# Это задание на ручное вычисление - что бы потом понять как работают циклы и насколько с ними проще жить.


##########################################################################################
# ВНИМАНИЕ! После того как __ВСЯ__ домашняя работа сделана и запушена на сервер,         #
# нужно зайти в ЛМС (LMS - Learning Management System ) по адресу http://go.skillbox.ru  #
# и оформить попытку сдачи ДЗ! Без этого ДЗ не будет проверяться!                        #
# Как оформить попытку сдачи смотрите видео - https://youtu.be/qVpN0L-C3LU               #
##########################################################################################

# зачет!
