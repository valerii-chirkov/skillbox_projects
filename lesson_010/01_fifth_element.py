# -*- coding: utf-8 -*-

# Умножить константу BRUCE_WILLIS на пятый элемент строки, введенный пользователем

while True:
    try:
        BRUCE_WILLIS = 42  # TODO Константу расположите в начале файла
        input_data = input('Если хочешь что-нибудь сделать, сделай это сам: ')
        leeloo = int(input_data[4])
        result = BRUCE_WILLIS * leeloo
        print(f'- Leeloo Dallas! Multi-pass № {result}!')
        break
    except IndexError:
        print('Введите более 5ти элементов')
    except ValueError:
        print('Введите только число')
    except Exception:
        print('Введите только число больше 5ти символов')


# Ообернуть код и обработать исключительные ситуации для произвольных входных параметров
# - ValueError - невозможно преобразовать к числу
# - IndexError - выход за границы списка
# - остальные исключения
# для каждого типа исключений написать на консоль соотв. сообщение
