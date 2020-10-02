# -*- coding: utf-8 -*-


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

# TODO после подтверждения части 1 преподователем, можно делать
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
    count_left = 0
    count_right = 0
    number_length = len(str(number))
    number_list = list(str(number))
    if len(str(number)) % 2 == 0:
        for i in range(number_length):
            if i <= (number_length / 2) - 1:
                count_left += int(number_list[i])
            else:
                count_right += int(number_list[i])
        print(f'{number} -> {count_left} = {count_right} -> {count_left == count_right}')
    else:
        for i in range(number_length//2):
            count_left += int(number_list[i])
        for i in range((number_length//2)+1, number_length):
            count_right += int(number_list[i])
        print(f'{number} -> {count_left} = {count_right} -> {count_left == count_right}')


# lucky_number(number=552066200)
for number in prime_numbers_generator(n=10000):
    print(lucky_number(number))


def palindrome(number):
    pass


def pentatope(n):
    pass


