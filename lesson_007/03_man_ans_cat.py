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
    def __init__(self, name, house):
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
        self.fullness = 10

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

    def pick_up_cat(self):  # подобрать кота
        self.house = house
        self.fullness -= 10
        inhabitants[1].go_to_the_house()
        cprint(f'{self.name} picked up a cat', color='cyan')

    def freelance(self):
        cprint(f'{self.name} needed extra money, he was doing freelance', color='blue')
        self.house.money += 50
        self.house.income += 50
        self.fullness -= 10

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} is died cause of hunger', color='red')
            cprint(f'{Cat} is in danger', color='red')
            return
        dice = randint(1, 7)
        promotion_chance = randint(0, 100)

        self.eat()
        if promotion_chance == 100:
            self.work_promotion()

        if dice == 1 or 2 or 3 or 4 or 5:  # TODO через range(1, 5) почему-то не работало
            self.work()
            self.eat()
        else:
            self.rest()

        if self.house.money <= 50:
            self.freelance()

        if self.fullness < 20:
            self.eat()

        if self.house.food < 10:
            self.shop_for_self()

        if self.house.cat_food < 10:
            self.shop_for_cat()

        if self.house.mess < 20:
            self.clean_house()
        else:
            self.rest()
        self.eat()
        self.sleep()


class Cat:
    def __init__(self, name):
        self.name = name
        self.fullness = 20
        self.house = None

    def go_to_the_house(self):
        self.house = house
        cprint(f'{self.name} has a new house!', color='cyan')

    def eat(self):
        if self.house.cat_food >= 10:
            cprint(f'{self.name} ate', color='yellow')
            self.fullness += 20
            self.house.cat_food -= 10
        else:
            cprint(f'{self.name} has no cat-food', color='red')

    def sleep(self):
        self.fullness -= 10
        cprint(f'{self.name} slept', color='cyan')

    def make_mess(self):
        self.fullness -= 10
        self.house.mess += 10
        cprint(f'{self.name} made a mess', color='red')

    def make_super_mess(self):
        self.fullness -= 30
        self.house.mess += 100
        cprint(f'{self.name} destroyed the house', color='red')

    def act(self):
        if self.fullness <= 0:
            cprint(f'{self.name} is died cause of hunger', color='red')
            return
        dice = randint(1, 5)

        if self.fullness <= 40:
            self.eat()
        else:
            self.sleep()
        if dice == 1:
            self.make_mess()
        if dice == 1 or 2:
            self.sleep()
        if dice == 1 or 2 or 3:
            self.eat()
        if dice == 4:
            self.make_super_mess()
        else:
            self.sleep()

    def __str__(self):
        return f'Meow - {self.name}, meow meowness is {self.fullness}'


class House:
    def __init__(self):
        self.name = 'Home'
        self.food = 50
        self.cat_food = 0
        self.money = 100
        self.mess = 0
        self.income = 0
        self.expenses = 0

    def __str__(self):
        return f'''There are {self.food} food and {self.cat_food} food for cat, money left {self.money}
Income for today = {self.income}, expenses = {self.expenses}'''


house = House()
inhabitants = [
    Man(name='Den', house=house),
    Cat(name='Bunny'),
]
inhabitants[0].pick_up_cat()

for day in range(1, 366):
    print('================= day {} ==================='.format(day))
    for inhabitant in range(len(inhabitants)):  # TODO В этом случае нужно использовать enumerate?
        if inhabitant == 0:
            print('        How the human spent his day: ')
            inhabitants[inhabitant].act()
        else:
            print('')
            print('         How the cat spent his day: ')
            inhabitants[inhabitant].act()
    # if house.money % 1000 == 0:  # TODO вылетает с ошибкой
    #     inhabitants[0].pick_up_cat()
    #     inhabitants.append(Cat(name='Murzik'))


    print('------------- in the evening ---------------')
    for inhabitant in inhabitants:
        print(inhabitant)
    print(house)
    print('')
    house.income = 0
    house.expenses = 0
# Усложненное задание (делать по желанию)
# Создать несколько (2-3) котов и подселить их в дом к человеку.
# Им всем вместе так же надо прожить 365 дней.

# (Можно определить критическое количество котов, которое может прокормить человек...)
