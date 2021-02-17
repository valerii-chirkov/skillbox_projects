from lesson_014.bowling import get_score_rules, get_score

# FILENAME = 'tournament.txt'
# FILENAME_OUT = 'tournament_result.txt'


def tournament_results_file(filename, filename_out):
    tournament_stat = {}
    participated = {}

    with open(filename, 'r') as ff_in, open(filename_out, 'w') as ff_out:
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
                    current_score = get_score_rules(line.split()[1])
                # if we get an exception - the player gets zero points for the game
                except Exception:
                    current_score = 0

                # write the result out - Name(Yan) Score(X71-3) Points(31)
                ff_out.write(line[:-1] + ' ' + str(current_score) + '\n')
                current_winner = line.split()[0]

                # count how many games the player participated
                if current_winner in participated:
                    participated[current_winner] += 1
                else:
                    participated[current_winner] = 1

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
                    # add the winner to the tuple
                    if current_winner in tournament_stat:
                        tournament_stat[current_winner] += 1
                    else:
                        tournament_stat[current_winner] = 1
                tour_stat = {}  # clear it for a new tour

    return tournament_stat, participated


# tournament_results_file(FILENAME, FILENAME_OUT)

