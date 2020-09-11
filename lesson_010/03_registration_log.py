# -*- coding: utf-8 -*-

# Есть файл с протоколом регистраций пользователей на сайте - registrations.txt
# Каждая строка содержит: ИМЯ ЕМЕЙЛ ВОЗРАСТ, разделенные пробелами
# Например:
# Василий test@test.ru 27
#
# Надо проверить данные из файла, для каждой строки:
# - присутсвуют все три поля
# - поле имени содержит только буквы
# - поле емейл содержит @ и .
# - поле возраст является числом от 10 до 99
#
# В результате проверки нужно сформировать два файла
# - registrations_good.log для правильных данных, записывать строки как есть
# - registrations_bad.log для ошибочных, записывать строку и вид ошибки.
#
# Для валидации строки данных написать метод, который может выкидывать исключения:
# - НЕ присутсвуют все три поля: ValueError
# - поле имени содержит НЕ только буквы: NotNameError (кастомное исключение)
# - поле емейл НЕ содержит @ и .(точку): NotEmailError (кастомное исключение)
# - поле возраст НЕ является числом от 10 до 99: ValueError
# Вызов метода обернуть в try-except.

FILE = 'registrations.txt'
FILE_OUT_GOOD = 'registrations_good.log'
FILE_OUT_BAD = 'registrations_bad.log'


class NotNameError(Exception):
    pass


class NotEmailError(Exception):
    pass


def check_name(name):
    if name.isalpha():
        return True
    else:
        raise NotNameError('There is not only letters')


def check_email(email):
    if '.' and '@' in email:
        return True
    else:
        raise NotNameError('There is not enough symbols')


def check_age(age):
    if age in range(10, 99):
        return True
    else:
        raise ValueError('Value Error')


with open(FILE, 'r') as ff:
    for line in ff:
        try:
            name, email, age = line.split(' ')
            name = str(name)
            email = str(email)
            age = int(age)
            try:
                if check_name(name) and check_email(email) and check_age(age):
                    with open(FILE_OUT_GOOD, 'w') as file:
                        file.write(line)

            except Exception as ex:
                with open(FILE_OUT_BAD, 'w') as file:
                    file.write(line + str(ex))
                    continue

        except ValueError as ex:
            with open(FILE_OUT_BAD, 'w') as file:
                file.write(line + str(ex))
                continue

# def calc(line):
#     # print(f'Read line {line}', flush=True)
#     operand_1, operation, operand_2 = line.split(' ')
#     operand_1 = int(operand_1)
#     operand_2 = int(operand_2)
#     if operation == '+':
#         value = operand_1 + operand_2
#     elif operation == '-':
#         value = operand_1 - operand_2
#     elif operation == '/':
#         value = operand_1 / operand_2
#     elif operation == '*':
#         value = operand_1 * operand_2
#     elif operation == '//':
#         value = operand_1 // operand_2
#     elif operation == '%':
#         value = operand_1 % operand_2
#     else:
#         raise ValueError('Unknown operation {operation}')
#     return value
#
#
# total = 0
# with open('calc.txt', 'r') as ff:
#     for line in ff:
#         line = line[:-1]
#         try:
#             total += calc(line)
#         except ValueError as exc:
#             if 'unpack' in exc.args[0]:
#                 print(f'Не хватает операндов {exc} в строке {line}')
#             else:
#                 print(f'Не могу преобразовать к целому {exc} в строке {line}')
#
# print(f'Total {total}')