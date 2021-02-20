from lesson_014.custom_exceptions import ValidSymbolsError, TenFramesError, SlashFirstError, TenPointsFrameError
from lesson_014.custom_exceptions import OddEvenEqualityError, XAfterNumber
POSSIBLE_SYMBOLS = '123456789-/XХxх'


class Bowling:

    def __init__(self, game_score):
        self.points = 0
        self.frame_length = 0
        self.split_by_two = []
        self.amount_x, self.amount_letters = 0, 0
        self.even_number, self.odd_number = None, None
        self.index, self.max_index = 0, len(game_score) - 1
        self.game_score, self.game_score_no_x = game_score, []
        self.throw, self.next_throw1, self.next_throw2 = '', '', ''

    def check_acceptance(self):
        self.amount_x = self.game_score.count('X') + self.game_score.count('Х') + self.game_score.count('x') + self.game_score.count('х')
        self.amount_letters = len(self.game_score)
        self.even_number = self.amount_x % 2 == 0 and self.amount_letters % 2 == 0
        self.odd_number = self.amount_x % 2 != 0 and self.amount_letters % 2 != 0

        if self.even_number or self.odd_number:
            for char in self.game_score:
                if char not in POSSIBLE_SYMBOLS:
                    raise ValidSymbolsError('There are some not acceptable symbols')
            self.game_score_no_x = self.game_score.translate({ord(i): None for i in 'XХxх'})
            self.split_by_two = [self.game_score_no_x[i:i + 2] for i in range(0, len(self.game_score_no_x), 2)]
            self.frame_length = len(self.split_by_two) + self.amount_x
            if self.frame_length > 10:
                raise TenFramesError('There are only 10 frames possible')
            return True
        else:
            return False

    def check_slash_first(self):
        if self.throw == '/':
            raise SlashFirstError('Slash symbol cannot be first in a frame')

    def last_throw(self):
        if self.throw in 'XxХх':
            self.points += 10
        elif self.throw == '-':
            self.points += 0
        else:
            self.points += self.throw
        return self.points

    def numeric_throw(self):
        if self.next_throw1 == '/':
            self.points += 10
        elif self.next_throw1 == '-':
            self.points += int(self.throw)
        elif self.next_throw1 in '123456789':
            if int(self.throw) + int(self.next_throw1) >= 10:
                raise TenPointsFrameError('There are more than 10 points in a frame')
            else:
                self.points += int(self.throw) + int(self.next_throw1)
        elif self.next_throw1 in 'XxХх':
            raise XAfterNumber('There cannot be X after a number in the end of the frames')
        else:
            raise ValidSymbolsError('There could be only / or - or a number')

    def xxx_throw_last(self):
        if self.next_throw1 in 'XxХх':
            self.points += 30
        else:
            self.points += 10 + int(self.next_throw1)

    def xxx_throw_main(self):
        self.points += 10
        if self.next_throw1 in 'XxХх':
            self.points += 10
            if self.next_throw2 in 'XxХх':
                self.points += 10
            elif self.next_throw2 == '-':
                self.points += 0
            else:
                self.points += int(self.next_throw2)
        elif (self.next_throw1 and self.next_throw2).count('/'):
            self.points += 10
        elif self.next_throw1.count('-'):
            self.points += 0
        else:
            self.points += int(self.next_throw1) + int(self.next_throw2)
            if int(self.next_throw1) + int(self.next_throw2) >= 10:
                raise TenPointsFrameError('There are more than 10 points in a frame')
        self.index += 1

    def dash_throw_last(self):
        if self.next_throw1 == '-':
            self.points += 0
        elif self.next_throw1 == '/':
            self.points += 10
        elif self.next_throw1 in 'XxХх':
            raise XAfterNumber('There cannot be X after slash in the end of the frames')
        else:
            self.points += int(self.next_throw1)

    def dash_next_throw1(self):
        self.points += 10
        if self.next_throw2 in 'XxХх':
            self.points += 10
        elif self.next_throw2 == '-':
            self.points += 0
        else:
            self.points += int(self.next_throw2)
        self.index += 2

    def last_two_throws(self):
        self.next_throw1 = self.game_score[self.index + 1]
        if self.throw in '123456789':
            self.numeric_throw()
        elif self.throw in 'XxХх':
            self.xxx_throw_last()
        elif self.throw == '-':
            self.dash_throw_last()

    def main_throws(self):
        if self.throw in 'XxХх':
            self.xxx_throw_main()
        elif self.next_throw1 == '/':
            self.dash_next_throw1()
        elif self.next_throw1 in 'XxХх':
            raise XAfterNumber('It is not possible to have X after a number')
        else:
            if self.throw == '-' and self.next_throw1 == '-':
                self.points += 0
            elif self.throw == '-' and self.next_throw1 in '123456789':
                self.points += int(self.next_throw1)
            elif self.throw and self.next_throw1 in '123456789':
                self.points += int(self.throw) + int(self.next_throw1)
            else:
                self.points += int(self.throw)
            self.index += 2

    def run(self):
        if self.check_acceptance():
            while self.index <= self.max_index:
                self.throw = self.game_score[self.index]
                self.check_slash_first()
                if self.index == self.max_index:
                    self.last_throw()
                    break
                elif self.index == self.max_index - 1:
                    self.last_two_throws()
                    break
                else:
                    self.next_throw1 = self.game_score[self.index + 1]
                    self.next_throw2 = self.game_score[self.index + 2]
                    self.main_throws()
            return self.points
        else:
            raise OddEvenEqualityError('There are not appropriate quantity of numbers')

# TODO ошибки выходят как надо
# bowling = Bowling(game_score='/51234XХ-1')
# get_score = bowling.run()
# print(get_score)

# TODO не понимаю как создать объект класса, чтобы он принимал значения из тестов, приходится импортировать класс
# TODO в тестах и когда идет сравнение, то понятное дело что два объекта с одинаковыми значениями будут все равно разные
# bowling = Bowling(game_score)
# get_score = bowling.run()
