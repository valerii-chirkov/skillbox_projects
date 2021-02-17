# -*- coding: utf-8 -*-

# Прибежал менеджер и сказал что нужно срочно просчитать протокол турнира по боулингу в файле tournament.txt
#
# Пример записи из лога турнира
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/
#   Татьяна	62334/6/4/44X361/X
#   Давид	--8/--8/4/8/-224----
#   Павел	----15623113-95/7/26
#   Роман	7/428/--4-533/34811/
#   winner is .........
#
# Нужно сформировать выходной файл tournament_result.txt c записями вида
#   ### Tour 1
#   Алексей	35612/----2/8-6/3/4/    98
#   Татьяна	62334/6/4/44X361/X      131
#   Давид	--8/--8/4/8/-224----    68
#   Павел	----15623113-95/7/26    69
#   Роман	7/428/--4-533/34811/    94
#   winner is Татьяна

# Код обаботки файла расположить отдельном модуле, модуль bowling использовать для получения количества очков
# одного участника. Если захочется изменить содержимое модуля bowling - тесты должны помочь.
#
# Из текущего файла сделать консольный скрипт для формирования файла с результатами турнира.
# Параметры скрипта: --input <файл протокола турнира> и --output <файл результатов турнира>

from lesson_014.tournament_result import tournament_results_file
import argparse

parser = argparse.ArgumentParser(description='Count score of a bowling frame')
parser.add_argument('-i', '--input', type=str, default='tournament.txt', help='Input file')
parser.add_argument('-o', '--output', type=str, default='tournament_result.txt', help='Output file')

args = parser.parse_args()

tournament_results_file(filename=args.input, filename_out=args.output)


# Усложненное задание (делать по желанию)
#
# После обработки протокола турнира вывести на консоль рейтинг игроков в виде таблицы:
#
# +----------+------------------+--------------+
# | Игрок    |  сыграно матчей  |  всего побед |
# +----------+------------------+--------------+
# | Татьяна  |        99        |      23      |
# ...
# | Алексей  |        20        |       5      |
# +----------+------------------+--------------+

tournament_stat, _ = tournament_results_file(filename=args.input, filename_out=args.output)
_, participated = tournament_results_file(filename=args.input, filename_out=args.output)

print('+----------+------------------+--------------+')
print('| Игрок    |  сыграно матчей  |  всего побед |')
print('+----------+------------------+--------------+')
for player in tournament_stat:
    games = participated.get(player)
    wins = tournament_stat.get(player)
    print(f'| {player.center(8)} | {str(games).center(16)} | {str(wins).center(12)} |')

print('+----------+------------------+--------------+')