# -*- coding: utf-8 -*-

# (цикл while)

# даны целые положительные числа a и b (a > b)
# Определить результат целочисленного деления a на b, с помощью цикла while,
# __НЕ__ используя стандартную операцию целочисленного деления (// и %)
# Формат вывода:
#   Целочисленное деление ХХХ на YYY дает ZZZ

dividend, divider = 100, 25
counter = 0
sum = -1

while counter <= dividend:
    counter += divider
    sum += 1
print(f'Целочисленное деление {dividend} на {divider} дает {counter}')

