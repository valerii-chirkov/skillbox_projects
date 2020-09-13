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
        raise NotEmailError('There is not enough symbols')


def check_age(age):
    if age in range(10, 99):
        return True
    else:
        raise ValueError('Wrong age')


exceptions = (NotNameError, NotEmailError)
with open(FILE, 'r') as file, open(FILE_OUT_GOOD, 'w') as g_file, open(FILE_OUT_BAD, 'w') as b_file:
    for line in file:
        try:
            name, email, age = line.split(' ')
            name = str(name)
            email = str(email)
            age = int(age)
            if check_name(name) and check_email(email) and check_age(age):
                g_file.write(line)

        except Exception as ex:  # Почему-то не работает с exceptions
            b_file.write(f'{line[:-1]} {ex.__class__.__name__} \n')  # ex.__class__.__name__
            continue
