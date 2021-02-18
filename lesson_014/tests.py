import unittest
from lesson_014.bowling import get_score, get_score_rules, get_score_american
from lesson_014.custom_exceptions import TenPointsFrameError, SlashFirstError, ValidSymbolsError, OddEvenEqualityError
from lesson_014.custom_exceptions import TenFramesError, XAfterNumber


class ScoreTest(unittest.TestCase):

    def test_ten_plus(self):
        with self.assertRaises(TenPointsFrameError):
            get_score_american('1234XХ-199')

    def test_slash_first(self):
        with self.assertRaises(SlashFirstError):
            get_score_american('1234XХ-1/5')

    def test_inappropriate_symbols(self):
        with self.assertRaises(ValidSymbolsError):
            get_score_american('1234XХ-1T701')

    def test_even_odd(self):
        with self.assertRaises(OddEvenEqualityError):
            get_score_american('12X12X12X1')

    def test_10_frames(self):
        with self.assertRaises(TenFramesError):
            get_score_american('XXXXXXXXXXX')
            get_score_american('1122334411223344-1--11')

    def test_equal_score(self):
        result_even_1_american = get_score_american('Xx1234xX')  # 10+10+1 + 10+1+2 + 3 + 7 + 10+10 + 10 = 74
        result_even_2_american = get_score_american('XX9/4-4--3')  # 10+10+9 + 10+10 + 10+4 + 4 + 4 +3 = 74
        self.assertEqual(result_even_1_american, result_even_2_american)

        result_even_1_american = get_score_american('Xx12125/5-1-')  # 61
        result_even_2_american = get_score_american('-9-9-9-9-9-9-7')  # 61
        self.assertEqual(result_even_1_american, result_even_2_american)

        result_odd_1 = get_score('Xx1234x')
        result_odd_2 = get_score('-244XXX')
        self.assertEqual(result_odd_1, result_odd_2)

        result_mixed_1 = get_score('Xx1234x')  # odd number = 70
        result_mixed_2 = get_score('-244XX11-3-/--')  # even number = 70
        self.assertEqual(result_mixed_1, result_mixed_2)


if __name__ == '__main__':
    unittest.main()
