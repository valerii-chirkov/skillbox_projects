#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# моя семья
my_family = ['Mother', 'Dad', 'Uncle', 'Granny']

# список списков приблизителного роста членов вашей семьи
my_family_height = [
    [my_family[0], 170],
    [my_family[1], 165],
    [my_family[2], 185],
    [my_family[3], 167]
]

# рост членов семьи
mother_height = my_family_height[0][1]
father_height = my_family_height[1][1]
uncle_height = my_family_height[2][1]
granny_height = my_family_height[3][1]

# общий вес
sum_height = mother_height + father_height + uncle_height + granny_height

print(f'Рост отца - {father_height} см')
print(f'Общий рост моей семьи (без учета меня) - {sum_height} см')

