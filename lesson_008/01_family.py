# -*- coding: utf-8 -*-

from termcolor import cprint
from random import randint, choice

######################################################## Часть первая
#
# Создать модель жизни небольшой семьи.
#
# Каждый день участники жизни могут делать только одно действие.
# Все вместе они должны прожить год и не умереть.
#
# Муж может:
#   есть,
#   играть в WoT,
#   ходить на работу,
# Жена может:
#   есть,
#   покупать продукты,
#   покупать шубу,
#   убираться в доме,

# Все они живут в одном доме, дом характеризуется:
#   кол-во денег в тумбочке (в начале - 100)
#   кол-во еды в холодильнике (в начале - 50)
#   кол-во грязи (в начале - 0)
#
# У людей есть имя, степень сытости (в начале - 30) и степень счастья (в начале - 100).
#
# Любое действие, кроме "есть", приводит к уменьшению степени сытости на 10 пунктов
# Кушают взрослые максимум по 30 единиц еды, степень сытости растет на 1 пункт за 1 пункт еды.
# Степень сытости не должна падать ниже 0, иначе чел умрет от голода.
#
# Деньги в тумбочку добавляет муж, после работы - 150 единиц за раз.
# Еда стоит 10 денег 10 единиц еды. Шуба стоит 350 единиц.
#
# Грязь добавляется каждый день по 5 пунктов, за одну уборку жена может убирать до 100 единиц грязи.
# Если в доме грязи больше 90 - у людей падает степень счастья каждый день на 10 пунктов,
# Степень счастья растет: у мужа от игры в WoT (на 20), у жены от покупки шубы (на 60, но шуба дорогая)
# Степень счастья не должна падать ниже 10, иначе чел умирает от депрессии.
#
# Подвести итоги жизни за год: сколько было заработано денег, сколько сьедено еды, сколько куплено шуб.


class House:

    def __init__(self):
        self.name = 'Home'
        self.money = 100
        self.annual_income = 0
        self.ate_food_total = 0
        self.fur_coats = 0
        self.food = 50
        self.dirt = 0  # Если поставить 1000, то все работает
        self.cat_food = 30
        self.inhabitants = []
        self.cats = 0

    def __str__(self):
        return 'There are {} money, {} food, {} dirt and {} cats'.format(self.money, self.food, self.dirt, self.cats)

    def pollute(self):
        self.dirt += 5
        if self.dirt % 15 == 0:
            cprint('There is {} dirt in the house.'.format(self.dirt), color='red')

    def incident(self):
        chance = randint(0, 100)
        if chance == 100:
            dice = randint(1, 2)
            print('')
            if dice == 1:
                cprint('Someone stole a half of money', color='red')
                self.money /= 2
                self.money = int(self.money)
            else:
                cprint('Someone stole a half of food', color='red')
                self.food /= 2
                self.food = int(self.food)


class Human:

    def __init__(self, name, home=None):
        self.name = name
        self.fullness = 30
        self.happiness = 100
        self.home = home
        self.home.inhabitants.append(self)  # Поправил - доступ к home должен быть только через self.

    def __str__(self):
        return 'It is {}, my fullness is {}, my happiness is {}'.format(self.name, self.fullness, self.happiness)

    def eat(self):
        ate_food = 0
        if self.home.food >= 30:
            self.fullness += 30
            ate_food += 30
            self.home.ate_food_total += 30
            self.home.food -= 30
        else:
            self.fullness += self.home.food
            ate_food += self.home.food
            self.home.ate_food_total += self.home.food
            self.home.food -= self.home.food
        print('{} ate {} food'.format(self.name, ate_food))

    def pollution_happiness(self):
        if self.home.dirt >= 90:
            self.happiness -= 10

    def check_dead(self):
        if self.happiness <= 10:
            cprint('{} is dead cause of depression'.format(self.name), color='red')
            return True
        if self.fullness <= 0:
            cprint('{} is dead cause of hunger'.format(self.name), color='red')
            return True

    def pet_cat(self):
        print('{} pet the cat'.format(self.name))
        self.happiness += 15  # добавил +10 потому что умирала


class Husband(Human):
    cats_names = ['Barsik', 'Stepa', 'Murzik', 'Dymka', 'Persik', 'Vaska', ]
    cats_Surnames = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    cats_namespace = []

    def __init__(self, name, home=None):
        super().__init__(name=name, home=home)
        self.salary = 100

    def act(self):
        self.pollution_happiness()
        dice = randint(1, 7)
        if self.home.money <= 100:
            self.work()
        elif self.fullness <= 30:
            self.eat()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.work()
        elif dice == 3:
            self.gaming()
        else:
            self.pet_cat()
        if self.happiness >= 100:
            self.happiness = 100
        if self.fullness >= 100:
            self.fullness = 100

    def work(self):
        promotion_chance = randint(0, 50)
        if promotion_chance == 50:
            self.salary += 100
        print('{} earn {}'.format(self.name, self.salary))
        self.fullness -= 10
        self.home.money += self.salary  # 150
        self.home.annual_income += self.salary  # 150

    def gaming(self):
        print('{} played WoT'.format(self.name))
        self.fullness -= 10
        self.happiness += 20
        if self.happiness >= 100:
            self.happiness = 100

    def pick_up_cat(self, cat):  # todo Тут кота надо передавать через параметер метода
                            #  если передавать, то где он тут будет использоваться?
        # todo Предлагал вот так: self.home.inhabitants.append(cat), а выбор имени делать во внешнем коде. Но можно и
        #  как у вас сейчас.
        name = choice(self.cats_names) + ' ' + choice(self.cats_Surnames) + '.' + choice(self.cats_Surnames) + '.'
        if not self.cats_namespace.count(name):  #  получилось сделать проверку на повтор?
            # todo Проще удалять выбранное имя из списка, тогда при следующем выборе не надо будет проверять
            # Если в списке имен нет только что зарандомленого имени, то пропускаем, если есть, то еще раз пробует
            self.home.inhabitants.append(Cat(name=name))  # Добавить кота
            cprint('{} picked up {}'.format(self.name, name), color='green')  # Принт подбора кота
            self.cats_namespace.append(name)  # Добавляем имя кота в список
            home.cats += 1  # Плюсуем кота для проверки главного цикла и для вывода 'сколько всего котов'
        else:
            self.pick_up_cat()  # todo Рекурсию старайте не использовать, если можно обойтись циклом


class Wife(Husband):

    def act(self):
        dice = randint(1, 7)
        if self.fullness <= 30:
            self.eat()
        elif self.home.food <= 30:
            self.shopping()
        elif self.happiness <= 30:
            self.pet_cat()
        # elif self.happiness <= 20:
        #     self.buy_fur_coat()
        # elif self.home.dirt >= 90:
        #     self.clean_house()
        elif self.home.cat_food <= 30:
            self.shopping_for_cat()
        # elif self.happiness <= 30:
        #     self.pet_cat()
        elif self.home.dirt >= 80:
            self.clean_house()
        elif dice == 1:
            self.eat()
        elif dice == 2:
            self.shopping()
        elif dice == 3:
            self.clean_house()
        elif dice == 4:
            self.pet_cat()
        elif dice == 5:
            self.shopping_for_cat()
        else:
            self.buy_fur_coat()
        if self.happiness >= 100:
            self.happiness = 100
        if self.fullness >= 100:
            self.fullness = 100

    def shopping(self):
        bought_food = 0
        self.fullness -= 10
        if self.home.money >= (100 - self.home.food):  # если есть возможность - покупает еду до 100
            self.home.money -= (100 - self.home.food)
            bought_food += 100 - self.home.food
            self.home.food = 100
        else:
            self.home.money -= self.home.money  # покупает еду на все что есть
            bought_food += self.home.money
            self.home.food += self.home.money
        print('{} bought {} food'.format(self.name, bought_food))

    def shopping_for_cat(self):  # Пусть будет разные методы
        bought_food = 0
        self.fullness -= 10
        if self.home.money >= (100 - self.home.cat_food):  # если есть возможность - покупает еду до 100
            self.home.money -= (100 - self.home.cat_food)
            bought_food += 100 - self.home.cat_food
            self.home.cat_food = 100
        else:
            self.home.money -= self.home.money  # покупает еду на все что есть
            bought_food += self.home.money
            self.home.cat_food += self.home.money
        print('{} bought {} food for cats'.format(self.name, bought_food))

    def buy_fur_coat(self):
        if self.happiness >= 100 and self.home.money >= 350:
            print('{} bought a new fur coat'.format(self.name))
            self.fullness -= 10
            self.happiness += 60
            self.home.money -= 350
            self.happiness = 100
            self.home.fur_coats += 1
        else:
            print('{} tried to buy a new fur coat, buy she had no money'.format(self.name))

    def clean_house(self):
        print('{} cleaned their house'.format(self.name))
        self.fullness -= 10
        self.home.dirt -= 100  # Чтобы при числе больше ста, оно не превращалось в ноль (было self.home.dirt = 0)
        if self.home.dirt < 0:  # Чтобы грязь не уходила в минус
            self.home.dirt = 0


class Child(Human):

    def act(self):
        self.eat() if self.fullness <= 20 else self.sleep()

    def eat(self):
        ate_food = 0
        if self.home.food >= 10:
            self.fullness += 10
            ate_food += 10
            self.home.ate_food_total += 10
            self.home.food -= 10
        else:
            self.fullness += self.home.food
            ate_food += self.home.food
            self.home.ate_food_total += self.home.food
            self.home.food -= self.home.food
        print('{} ate {} food'.format(self.name, ate_food))

    def sleep(self):
        self.fullness -= 5
        print('{} slept'.format(self.name))


class Cat:

    def __init__(self, name):
        self.name = name
        self.fullness = 30
        self.home = home

    def __str__(self):
        return 'It is {}, my fullness is {}'.format(self.name, self.fullness)

    def act(self):
        dice = randint(1, 3)
        if self.fullness <= 10:
            self.eat()
        elif dice == 1:
            self.sleep()
        elif dice == 2:
            self.soil()
            self.home.dirt += 5
        else:
            self.eat()

    def eat(self):
        ate_food = 0
        if self.home.cat_food >= 5:
            self.fullness += 10
            self.home.cat_food -= 5
            ate_food += 5
        else:
            self.fullness += 2*self.home.cat_food
            self.home.cat_food -= self.home.cat_food
            ate_food += self.home.cat_food
        print('{} ate {} food'.format(self.name, ate_food))

    def sleep(self):
        self.fullness -= 10
        print('{} slept'.format(self.name))

    def soil(self):
        print('{} made a mess'.format(self.name))
        self.fullness -= 10

    def check_dead(self):
        if self.fullness <= 0:
            print('{} is dead cause of hunger'.format(self.name))
            return True


home = House()
serge = Husband(name='Сережа', home=home)
masha = Wife(name='Маша', home=home)
# barsik = Cat(name='Barsik')
nick = Child(name='Nick', home=home)
# possible_cats = [Cat('Stepa'), Cat('Murzik'), Cat('Dymka'), Cat('Persik'), Cat('Vaska')]

for inhabitant in home.inhabitants:
    cprint(inhabitant, color='cyan')
cprint(home, color='cyan')

for day in range(1, 1366):  # TODO сделал чтобы посмотреть как добавляются коты
    cprint('================== День {} =================='.format(day), color='red')
    home.pollute()
    dice = randint(0, 100)

    if home.cats == 0:
        serge.pick_up_cat()
    elif dice == 100:
        serge.pick_up_cat()

    for inhabitant in home.inhabitants:
        inhabitant.act()
        if inhabitant.check_dead():
            exit()

    for inhabitant in home.inhabitants:
        cprint(inhabitant, color='cyan')

    home.incident()
    cprint(home, color='cyan')

print('The household earn {} for this year'.format(home.annual_income))
print('The household ate {} food'.format(home.ate_food_total))
print('The woman bought {} fur coats'.format(home.fur_coats))
print('They have {some} cats'.format(some=home.cats))

# зачет первого этапа
# зачет второго этапа



# Усложненное задание (делать по желанию)
#
# Сделать из семьи любителей котов - пусть котов будет 3, или даже 5-10.
# Коты должны выжить вместе с семьей!
#
# Определить максимальное число котов, которое может прокормить эта семья при значениях зарплаты от 50 до 400.
# Для сглаживание случайностей моделирование за год делать 3 раза, если 2 из 3х выжили - считаем что выжили.
#
# в итоге должен получится приблизительно такой код экспериментов
# for food_incidents in range(6):
#   for money_incidents in range(6):
#       life = Simulation(money_incidents, food_incidents)
#       for salary in range(50, 401, 50):
#           max_cats = life.experiment(salary)
#           print(f'При зарплате {salary} максимально можно прокормить {max_cats} котов')
