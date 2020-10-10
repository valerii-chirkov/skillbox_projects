# -*- coding: utf-8 -*-

from math import ceil
# Есть функция генерации списка простых чисел


def get_prime_numbers(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
    return prime_numbers

# Часть 1
# На основе алгоритма get_prime_numbers создать класс итерируемых обьектов,
# который выдает последовательность простых чисел до n
#
# Распечатать все простые числа до 10000 в столбик


class PrimeNumbers:
    def __init__(self, n):
        self.maximum = n
        self.prime_numbers = []
        self.current_number = 0

    def __iter__(self):
        self.current_number = 1
        return self

    def get_prime(self):
        self.current_number += 1
        for prime in self.prime_numbers:
            if self.current_number % prime == 0:
                return None
        self.prime_numbers.append(self.current_number)
        return self.current_number

    def __next__(self):
        value = None
        while value is None:
            value = self.get_prime()
        if self.current_number < self.maximum:
            return value
        else:
            raise StopIteration()


# prime_number_iterator = PrimeNumbers(n=10000)
# for number in prime_number_iterator:
#     print(number)
# print(prime_number_iterator)

# зачет первой части

#  после подтверждения части 1 преподователем, можно делать
# Часть 2
# Теперь нужно создать генератор, который выдает последовательность простых чисел до n
# Распечатать все простые числа до 10000 в столбик


def prime_numbers_generator(n):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            yield number


def prime_number_generator_filtered(n, filtered):
    prime_numbers = []
    for number in range(2, n + 1):
        for prime in prime_numbers:
            if number % prime == 0:
                break
        else:
            prime_numbers.append(number)
            if filtered:
                yield number


# зачет второй части

# Часть 3
# Написать несколько функций-фильтров, которые выдает True, если число:
# 1) "счастливое" в обыденном пониманиии - сумма первых цифр равна сумме последних
#       Если число имеет нечетное число цифр (например 727 или 92083),
#       то для вычисления "счастливости" брать равное количество цифр с начала и конца:
#           727 -> 7(2)7 -> 7 == 7 -> True
#           92083 -> 92(0)83 -> 9+2 == 8+3 -> True
# 2) "палиндромное" - одинаково читающееся в обоих направлениях. Например 723327 и 101
# 3) придумать свою (https://clck.ru/GB5Fc в помощь)
#
# Подумать, как можно применить функции-фильтры к полученной последовательности простых чисел
# для получения, к примеру: простых счастливых чисел, простых палиндромных чисел,
# простых счастливых палиндромных чисел и так далее. Придумать не менее 2х способов.
#
# Подсказка: возможно, нужно будет добавить параметр в итератор/генератор.
def lucky_number(number):
    number_length = len(str(number))
    number_list = list(str(number))

    half_length = number_length // 2
    left_sum = sum(map(int, number_list[:half_length]))
    right_sum = sum(map(int, number_list[-half_length:]))
    # if left_sum == right_sum:
    return left_sum == right_sum  # поправил - if тут не нужен


for number in prime_number_generator_filtered(n=1000, filtered=lucky_number):
    print(number)


def palindrome(number):
    # if str(number) == str(number)[::-1]:
    return str(number) == str(number)[::-1]  # поправил - if тут не нужен


def own_number(number):
    # Есть число 1256, если сумма цифр (14) содержится в числе, то True, в нашем случае False
    number = str(number)
    sum_digit = sum(map(int, number))
    # if number.count(str(sum_digit)):
    return number.count(str(sum_digit))  # поправил - if тут не нужен


# lucky_number_generator = filter(lucky_number, prime_number_iterator)
# palindrome_generator = filter(palindrome, prime_number_iterator)
# own_number_generator = filter(own_number, prime_number_iterator)

# for number in palindrome_generator:
#     print(number)

# for number in lucky_number_generator:
#     print(number)

# for number in own_number_generator:
#     print(number)

# for number in prime_numbers_generator(n=10000):
#     print(number)

# зачет!
