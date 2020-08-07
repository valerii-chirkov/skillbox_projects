# -*- coding: utf-8 -*-

from random import randint
from termcolor import cprint

# Доработать практическую часть урока lesson_007/python_snippets/08_practice.py

# Необходимо создать класс кота. У кота есть аттрибуты - сытость и дом (в котором он живет).
# Кот живет с человеком в доме.
# Для кота дом характеризируется - миской для еды и грязью.
# Изначально в доме нет еды для кота и нет грязи.

# Доработать класс человека, добавив методы
#   подобрать кота - у кота появляется дом.
#   купить коту еды - кошачья еда в доме увеличивается на 50, деньги уменьшаются на 50.
#   убраться в доме - степень грязи в доме уменьшается на 100, сытость у человека уменьшается на 20.
# Увеличить кол-во зарабатываемых человеком денег до 150 (он выучил пайтон и устроился на хорошую работу :)

# Кот может есть, спать и драть обои - необходимо реализовать соответствующие методы.
# Когда кот спит - сытость уменьшается на 10
# Когда кот ест - сытость увеличивается на 20, кошачья еда в доме уменьшается на 10.
# Когда кот дерет обои - сытость уменьшается на 10, степень грязи в доме увеличивается на 5
# Если степень сытости < 0, кот умирает.
# Так же надо реализовать метод "действуй" для кота, в котором он принимает решение
# что будет делать сегодня

# Человеку и коту надо вместе прожить 365 дней.


class Man:

    def __init__(self, name, house=None):
        self.name = name
        self.fullness = 50
        self.house = house
        self.wage = 50

    def __str__(self):
        return f'I am - {self.name}, my fullness is {self.fullness}, my wage is {self.wage}'

    def eat(self):
        if self.house.food >= 10:
            cprint(f'{self.name} ate', color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            self.fullness -= 10
            cprint(f'{self.name} wanted to eat, but had no food', color='red')

    def work(self):
        cprint(f'{self.name} left for work', color='blue')
        self.house.money += self.wage
        self.house.income += self.wage
        self.fullness -= 10

    def work_promotion(self):
        cprint(f'{self.name} has learnt new skills, + 50 to wage', color='blue')
        self.wage += 50

    def sleep(self):
        cprint(f'{self.name} went to sleep', color='cyan')
        self.fullness -= 10

    def rest(self):
        cprint(f'{self.name} had a rest', color='blue')
        self.fullness -= 10

    def shop_for_self(self):
        if self.house.money >= 50:
            cprint(f'{self.name} bought some food', color='magenta')
            self.house.money -= 50
            self.house.expenses -= 50
            self.house.food += 50
        else:
            cprint(f'{self.name} spent all his money', color='red')

    def shop_for_cat(self):  # купить коту еды
        if self.house.money >= 50:
            cprint(f'{self.name} bought some food for his cat', color='magenta')
            self.house.money -= 50
            self.house.expenses -= 50
            self.house.cat_food += 50
        else:
            cprint(f'{self.name} spent all his money', color='red')

    def clean_house(self):  # убраться в доме
        cprint(f'{self.name} cleaned his house', color='magenta')
        self.house.mess = 0
        self.fullness -= 20

    def pick_up_cat(self, cat):  # подобрать кота
        self.fullness -= 10
        if self.house:
            cat.house = self.house
        cprint(f'{self.name} picked up a cat', color='cyan')
        cprint(f'{cat.name} has a new house!', color='cyan')
        print('')

    def freelance(self):
        cprint(f'{self.name} needed extra money, he was doing freelance', color='blue')
        self.house.money += 50
        self.house.income += 50
        self.fullness -= 10

    def act(self):
        dice = randint(1, 4)
        promotion_chance = randint(0, 100)

        if promotion_chance == 100:
            self.work_promotion()

        # TODO У вас много котов так что не все коты смогут жить в доме, поэтому к этому стремится не стоит
        if self.fullness <= 20:
            self.eat()
        elif self.house.food <= 20:
            self.shop_for_self()
            # TODO Тоже лишнее вложение
            if not self.shop_for_self():
                self.work()
                # continue # TODO так было бы хорошо, но не дает continue написать
        elif self.house.cat_food <= 20:
            self.shop_for_cat()
        elif self.house.money <= 50:
            self.work()
        elif self.house.mess >= 50:
            self.clean_house()
        elif dice == 1 or 2:
            self.sleep()
        elif dice == 3:
            self.rest()
        elif dice == 4:
            self.freelance()

    def dead(self):
        if self.fullness <= 0:
            cprint(f'{self.name} is died cause of hunger', color='red')
            # TODO Метод возвращает None, поэтому условие не срабатывает, return True
            return


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def eat(self):
        if self.house.cat_food >= 10:
            cprint(f'{self.name} ate', color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            # TODO сильно усложнено тут просто путь рапортует что нет еды, и пока что все!
            self.fullness -= 10
            cprint(f'{self.name} has no cat-food', color='red')
            if self.fullness <= 0:  # нет рекурсия это когда функция вызывает сама себя!
                # TODO Чекать это будем в основном цикле для каждого кота в цикле
                self.dead()
                cats.remove(self)

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} slept', color='cyan')

    def make_mess(self):
        self.fullness -= 10
        self.house.mess += 10
        cprint(f'{self.name} made a mess', color='red')

    def act(self):
        # TODO можно сделать randint(1, 7) больше вероятность
        dice = randint(1, 3)
        if self.fullness <= 20:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.make_mess()
        else:
            self.sleep()

    # TODO данный метод тоже чекаем в главном цикле у все котов
    def dead(self):
        if self.fullness <= 0:
            cprint(f'{self.name} is died cause of hunger', color='red')
            # TODO Метод возвращает None, поэтому условие не срабатывает, return True
            return

    def __str__(self):
        return f'Meow - {self.name}, meow meowness is {self.fullness}'


class House:
    def __init__(self):
        self.name = 'Home'
        self.food = 50
        self.cat_food = 50
        self.money = 100
        self.mess = 0
        self.income = 0
        self.expenses = 0

    def __str__(self):
        return f'''There are {self.food} food and {self.cat_food} food for cat, money left {self.money}
Income for today = {self.income}, expenses = {self.expenses}'''


my_house = House()
man = Man(name='Den', house=my_house)
# TODO уменьшаем количество котов, начинаем с 2 если норм, увеличим до 3. Как только 3 из 5 будет фейл останавливаемся
cats = [Cat(name='Bunny'), Cat(name='Fuzzy'), Cat(name='King'), Cat(name='Tiger'), Cat(name='Sleepy')]
days = range(1, 366)
if man.house == my_house:
    for new_cat in cats:
        man.pick_up_cat(new_cat)


for day in days:
    print('================= day {} ==================='.format(day))
    print(f'          How {man.name} spent his day: ')
    man.act()

    print('')
    print(f'         How cats spent their day: ')
    if not cats:
        cprint('Den has no cats anymore', color='red')
        break
    for cat in cats:
        cat.act()

    print('')
    print('------------- in the evening ---------------')
    print(man)
    for cat in cats:
        print(cat)
    print('- - - - - - - - - - - - - - - - - - - - - - -')
    print(my_house)
    print('')
    my_house.income = 0
    my_house.expenses = 0

    if man.dead():  # TODO Метод возвращает NONE поэтому не срабатывает!
        print('It is a pity')
        break
    # if not any(cats.act):
    #     print('It is a pity')
    #
    #     break
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)


