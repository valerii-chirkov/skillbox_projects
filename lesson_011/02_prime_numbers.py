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
        self.amount = n   # todo точнее это "максимальное число" или "предел" вычислений
        self.prime_numbers = []
        self.i = 0  # todo назовите "текущее_число"

    def __iter__(self):
        self.i = 1
        return self

    def get_prime(self):
        self.i += 1
        for prime in self.prime_numbers:
            if self.i % prime == 0:
                return None
        self.prime_numbers.append(self.i)
        return self.i

    def __next__(self):
        value = None
        while value is None:
            value = self.get_prime()
        if self.i < self.amount:
            return value
        else:
            raise StopIteration()


prime_number_iterator = PrimeNumbers(n=10000)
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


# for number in prime_numbers_generator(n=10000):
#     print(number)

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
    count_left = 0  # TODO Назвалбы left_summa и right_summa
    count_right = 0
    number_length = len(str(number))
    number_list = list(str(number))  # TODO Строка уже и есть список символов
    #  первая попытка
    # for i in range(number_length):
    #     if i < (number_length//2):
    #         count_left += int(number_list[i])
    #     elif i > (number_length//2):
    #         count_right += int(number_list[i])

    #  вторая попытка
    # for i in range(number_length//2):  # если просто делением делать, то он коряво выдает числа с правой стороны
    #     count_left += int(number_list[i])
    # for i in range(number_length//2, number_length): # тк если начинать с половины, то он берет с собой среднюю цифру
    #     count_right += int(number_list[i])
    # # а если сделать половину +1, то в четных числах тоже беда будет

    #  с импортом math.ceil
    # for i in range(number_length//2):
    #     count_left += int(number_list[i])
    # for i in range(ceil(number_length/2), number_length):
    #     count_right += int(number_list[i])
    # todo Мой вариант
    half_lenght = number_length // 2
    count_left = sum(map(int, number_list[:half_lenght]))
    count_right = sum(map(int, number_list[-half_lenght:]))
    if count_left == count_right:
        print(f'{number} -> {count_left} = {count_right} -> {count_left == count_right}')


lucky_number_generator = filter(lucky_number, prime_number_iterator)
# for number in lucky_number_generator:
#     print(number)

print(lucky_number(1234321))


def palindrome(number):
    number = str(number)
    left_part = number[:len(number)//2]
    right_part = number[ceil(len(number)/2):]
    right_part = right_part[::-1]

    if left_part == right_part:
        print(f'{number} is {left_part == right_part}')
    # todo Палиндром это слово читающееся в обе стороны одинаково, поэтому достаточно сравнить строковые представления
    #  числа прямое и обратное


# test_numbers = [x for x in range(100000)]  # TODO в счастливых числах были только 3х значные цифры, проверил на больших
# palindrome_generator = filter(palindrome, test_numbers)

palindrome_generator = filter(palindrome, prime_number_iterator)
# for number in palindrome_generator:
#     print(number)


def own_number(number):
    # Есть число 1256, если сумма цифр (14) содержится в числе, то True, в нашем случае False
    number = str(number)
    sum_digit = sum(map(int, number))
    if number.count(str(sum_digit)):
        print(f'It\'s {sum_digit}, {number} is {True}')


own_number(123143)
