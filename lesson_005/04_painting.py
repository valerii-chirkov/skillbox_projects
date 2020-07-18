# -*- coding: utf-8 -*-
import simple_draw as sd

from lesson_005.picture_elements.sun import sun
from lesson_005.picture_elements.grass import grass
from lesson_005.picture_elements.rainbow import rainbow
from lesson_005.picture_elements.wall import house
from lesson_005.picture_elements.tree import draw_branches as tree
from lesson_005.picture_elements.smile import draw_smiles as smile
from lesson_005.picture_elements.snowflakes import snowflakes_fall as snowflakes
from lesson_005.picture_elements.snowflakes import snowdrift

sd.set_screen_size(width=1200, height=600)
sd.background_color = (15, 116, 235)
grass()
snowdrift()
tree()

while True:
    sd.start_drawing()
    house()
    rainbow()
    sun()
    smile()
    snowflakes()
    sd.finish_drawing()
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

# Создать пакет, в который скопировать функции отрисовки из предыдущего урока
#  - радуги
#  - стены
#  - дерева
#  - смайлика
#  - снежинок
# Функции по модулям разместить по тематике. Название пакета и модулей - по смыслу.
# Создать модуль с функцией отрисовки кирпичного дома с широким окном и крышей.

# С помощью созданного пакета нарисовать эпохальное полотно "Утро в деревне".
# На картине должны быть:
#  - кирпичный дом, в окошке - смайлик.
#  - слева от дома - сугроб (предположим что это ранняя весна)
#  - справа от дома - дерево (можно несколько)
#  - справа в небе - радуга, слева - солнце (весна же!)
# пример см. lesson_005/results/04_painting.jpg
# Приправить своей фантазией по вкусу (коты? коровы? люди? трактор? что придумается)

# Усложненное задание (делать по желанию)
# Анимировать картину.
# Пусть слева идет снегопад, радуга переливается цветами, смайлик моргает, солнце крутит лучами, етс.
# Задержку в анимировании все равно надо ставить, пусть даже 0.01 сек - так библиотека устойчивей работает.

# зачет!
