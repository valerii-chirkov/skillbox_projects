from lesson_014 import bowling

FILENAME = 'tournament.txt'
FILENAME_OUT = 'tournament_result.txt'


def tournament_results_file():
    tournament_stat = {}

    with open(FILENAME, 'r') as ff_in, open(FILENAME_OUT, 'w') as ff_out:
        tour_stat = {}
        previous_score, previous_winner = 0, ''

        for line in ff_in:

            # this line is useless to calculate the result, but we need to write it out into an output doc.
            if line.count('Tour') or line == '\n':
                ff_out.write(line)

            # if line starts with a CAPITAL letter
            if line[0].isupper():
                # we are trying to get a score unless there're a mistake in a row
                try:
                    current_score = bowling.get_score(line.split()[1])
                # if we get an exception - the player gets zero points for the game
                except Exception:
                    current_score = 0

                # write the result out - Name(Yan) Score(X71-3) Points(31)
                ff_out.write(line[:-1] + ' ' + str(current_score) + '\n')
                current_winner = line.split()[0]

                # fill the dict for defining the winner of 1 game
                tour_stat[current_winner] = current_score

                if previous_score > current_score:
                    current_winner = previous_winner
                elif current_score > previous_score:
                    previous_score = current_score
                    previous_winner = current_winner

            if line.count('winner'):
                # it could be possible that everyone in the tour got zero points due mistakes in their scores
                no_winners = all(value == 0 for value in tour_stat.values())  # True of False
                if no_winners:
                    ff_out.write('no winners' + '\n')
                else:
                    ff_out.write('winner is ' + current_winner + '\n')
                    previous_score = 0
                    previous_winner = ''
                tour_stat = {}  # clear it for a new tour

    return tournament_stat


tournament_results_file()


