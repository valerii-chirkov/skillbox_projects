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
        raise NotNameError('There is not enough symbols')  # TODO Опечатка - не то исключение выбросили


def check_age(age):
    if age in range(10, 99):
        return True
    else:
        raise ValueError('Value Error')  # TODO Тут надо дать пояснение: "возраст вне диапазона допустимых значенией"
                                         #  или "неверный возраст"


with open(FILE, 'r') as ff:  # TODO продолжайте открывать файлы через запятую, with умеет работать с несклькими файлами
                             #  сразу
    file_good = open(FILE_OUT_GOOD, 'w')
    file_bad = open(FILE_OUT_BAD, 'w')
    for line in ff:
        try:  # TODO Вы сделали вложенный try, но вот этот "внешний" не работает, так как внутренний всё перехватывает
              #  и отрабатывает, тогда зачем он нужен?
            try:
                name, email, age = line.split(' ')
                name = str(name)
                email = str(email)
                age = int(age)
                if check_name(name) and check_email(email) and check_age(age):
                    file_good.write(line)

            except Exception as ex:  # todo Вместо Exception укажите кортеж с конкретными классами которые обрабатываются
                file_bad.write(line[:-1] + " " + str(ex) + '\n')  # TODO Используйте f-строки, а вот так можно получить
                                                                  #  имя класса исключения f'{ex.__class__.__name__}'
                continue

        except ValueError as ex:
            file_bad.write(line + " " + str(ex))
            continue
    file_good.close()
    file_bad.close()
