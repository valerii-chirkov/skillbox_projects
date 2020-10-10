# -*- coding: utf-8 -*-

# Написать декоратор, который будет логировать (записывать в лог файл)
# ошибки из декорируемой функции и выбрасывать их дальше.
#
# Имя файла лога - function_errors.log
# Формат лога: <имя функции> <параметры вызова> <тип ошибки> <текст ошибки>
# Лог файл открывать каждый раз при ошибке в режиме 'a'
import logging

# def log_errors(func):
#     LOG_FILE = 'function_errors.log'
#     with open(LOG_FILE, 'a') as ff:
#         if exc:
#             ff.write(f'{exc}')


def log_errors(func):
    def wrapper(*args, **kwargs):
        with open('function_errors.log', 'a') as ff:
            try:
                func(*args, **kwargs)  # TODO Функция может и должна возвращать значение
                # TODO не понял этого todo
                # TODO у фукнции func может быть возращаемое значение, к примеру: смотрите на perky. Декоратор должен
                #  "поддержать" этот возможность: добавьте return перед func
            except Exception as exc:
                ff.write(f'{func} {args, kwargs} {type(exc)} {exc} \n')
                raise exc
            #  try except дублируется с for line in lines: так и должно быть?
            # TODO Это не дублирование - в указанном цикле поймают исключение которое выбрасывается декоратором
            #  (повторяется им) так как этот декоратор не должен "скрывать" проблему, он только логгирует её выбрасывает
            #  далее
        return ff
    return wrapper

# Проверить работу на следующих функциях
@log_errors
def perky(param):
    return param / 0


@log_errors
def check_line(line):
    name, email, age = line.split(' ')
    if not name.isalpha():
        raise ValueError("it's not a name")
    if '@' not in email or '.' not in email:
        raise ValueError("it's not a email")
    if not 10 <= int(age) <= 99:
        raise ValueError('Age not in 10..99 range')


lines = [
    'Ярослав bxh@ya.ru 600',
    'Земфира tslzp@mail.ru 52',
    'Тролль nsocnzas.mail.ru 82',
    'Джигурда wqxq@gmail.com 29',
    'Земфира 86',
    'Равшан wmsuuzsxi@mail.ru 35',
]
for line in lines:
    try:
        check_line(line)
    except Exception as exc:
        print(f'Invalid format: {exc}')
perky(param=42)


# Усложненное задание (делать по желанию).
# Написать декоратор с параметром - именем файла
#
# @log_errors('function_errors.log')
# def func():
#     pass
