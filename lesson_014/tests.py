import unittest
from lesson_014.bowling import get_score


class ScoreTest(unittest.TestCase):

    def test_zero(self):
        with self.assertRaises(Exception):
            get_score('1234XХ-102')

    def test_ten_plus(self):
        with self.assertRaises(Exception):
            get_score('1234XХ-199')

    def test_slash_first(self):
        with self.assertRaises(TypeError):
            get_score('1234XХ-1/5')

    def test_inappropriate_symbols(self):
        with self.assertRaises(TypeError):
            get_score('1234XХ-1T7')

    def test_even_odd(self):
        with self.assertRaises(ValueError):
            get_score('12X12X12X1')

    def test_10_frames(self):
        with self.assertRaises(TypeError):
            get_score('XXXXXXXXXXX')
            get_score('1122334411223344-1--11')


if __name__ == '__main__':
    unittest.main()
