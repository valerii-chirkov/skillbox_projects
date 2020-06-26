# -*- coding: utf-8 -*-

# (цикл while)

# Ежемесячная стипендия студента составляет educational_grant руб., а расходы на проживание превышают стипендию
# и составляют expenses руб. в месяц. Рост цен ежемесячно увеличивает расходы на 3%, кроме первого месяца
# Составьте программу расчета суммы денег, которую необходимо единовременно попросить у родителей,
# чтобы можно было прожить учебный год (10 месяцев), используя только эти деньги и стипендию.
# Формат вывода:
#   Студенту надо попросить ХХХ.ХХ рублей

educational_grant, expenses = 10000, 12000
month = 0
expenses_year = 0
educational_grant_sum = educational_grant * 10

# 9 периодов, так как 1 месяц расходы не увеличиваются
while month < 9:
    month += 1
    expenses = expenses * 1.03
    expenses_year += expenses
expenses_year += 12000
needs = round((expenses_year - educational_grant_sum), 2)
print(f'Студенту надо попросить {needs} рублей')

