import unittest
from lesson_014.bowling import get_score


class ScoreTest(unittest.TestCase):
    def test_zero(self):
        game_result = get_score('1234XХ-102')
        self.assertEqual(game_result, Exception)

    def test_ten_plus(self):
        game_result = get_score('1234XХ-199')
        self.assertEqual(game_result, Exception)

    def test_slash_first(self):
        game_result = get_score('1234XХ-1/5')
        self.assertEqual(game_result, Exception)

    def test_inappropriate_symbols(self):
        game_result = get_score('1234XХ-1T7')
        self.assertEqual(game_result, Exception)


if __name__ == '__main__':
    unittest.main()