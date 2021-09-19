import unittest
from main import *


class WarmupTestCase(unittest.TestCase):
    def test_1(self):
        expected = 'a'
        actual = warmup('a', 0)

        self.assertEqual(expected, actual)

    def test_2(self):
        expected = 'b'
        actual = warmup('a', 1)

        self.assertEqual(expected, actual)

    def test_3(self):
        expected = 'f'
        actual = warmup('a', 5)

        self.assertEqual(expected, actual)

    def test_4(self):
        expected = 'a'
        actual = warmup('a', 26)

        self.assertEqual(expected, actual)

    def test_5(self):
        expected = 's'
        actual = warmup('d', 15)

        self.assertEqual(expected, actual)

    def test_6(self):
        expected = 'a'
        actual = warmup('z', 1)

        self.assertEqual(expected, actual)

    def test_7(self):
        expected = 'm'
        actual = warmup('q', 22)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
