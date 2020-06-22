#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть строка с перечислением фильмов

my_favorite_movies = 'Терминатор, Пятый элемент, Аватар, Чужие, Назад в будущее'

# Выведите на консоль с помощью индексации строки, последовательно:
#   первый фильм
#   последний
#   второй
#   второй с конца

# Запятая не должна выводиться.  Переопределять my_favorite_movies нельзя
# Использовать .split() или .find()или другие методы строки нельзя - пользуйтесь только срезами,
# как указано в задании!

movie1 = my_favorite_movies[:10]
movie2 = my_favorite_movies[12: 24]
movie3 = my_favorite_movies[27: 33]
movie4 = my_favorite_movies[35: 40]
movie5 = my_favorite_movies[42:]  # Есть вариант взять с конца строки отрицательным индексом [-15:]

print(movie1)
print(movie5)
print(movie2)
print(movie4)

# зачет!
