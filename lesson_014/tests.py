import unittest
from lesson_014.bowling import get_score
from lesson_014.custom_exceptions import *


class ScoreTest(unittest.TestCase):

    def test_ten_plus(self):
        with self.assertRaises(TenPointsFrameError):
            get_score('1234XХ-199')

    def test_slash_first(self):
        with self.assertRaises(SlashFirstError):
            get_score('1234XХ-1/5')

    def test_inappropriate_symbols(self):
        with self.assertRaises(ValidSymbolsError):
            get_score('1234XХ-1T701')

    def test_even_odd(self):
        with self.assertRaises(OddEvenEqualityError):
            get_score('12X12X12X1')

    def test_10_frames(self):
        with self.assertRaises(TenFramesError):
            get_score('XXXXXXXXXXX')
            get_score('1122334411223344-1--11')

    def test_equal_score(self):
        result_even_1 = get_score('Xx1234xX')
        result_even_2 = get_score('-244XXXX')
        self.assertEqual(result_even_1, result_even_2)

        result_odd_1 = get_score('Xx1234x')
        result_odd_2 = get_score('-244XXX')
        self.assertEqual(result_odd_1, result_odd_2)

        result_mixed_1 = get_score('Xx1234x')  # odd number = 70
        result_mixed_2 = get_score('-244XX11-3-/--')  # even number = 70
        self.assertEqual(result_mixed_1, result_mixed_2)


if __name__ == '__main__':
    unittest.main()
