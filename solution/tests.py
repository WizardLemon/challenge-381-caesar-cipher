import unittest
from main import *


class WarmupTestCase(unittest.TestCase):
    """
    This class contains tests for the warmup section of the challenge.
    """

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


class ChallengeTestCase(unittest.TestCase):
    """
    This class contains the tests for the actual challenge
    """

    def test_1(self):
        expected = "b"
        actual = caesar("a", 1)

        self.assertEqual(expected, actual)

    def test_2(self):
        expected = "bcda"
        actual = caesar("abcz", 1)

        self.assertEqual(expected, actual)

    def test_3(self):
        expected = "vex"
        actual = caesar("irk", 13)

        self.assertEqual(expected, actual)

    def test_4(self):
        expected = "layout"
        actual = caesar("fusion", 6)

        self.assertEqual(expected, actual)

    def test_5(self):
        expected = "jgorevxumxgsskx"
        actual = caesar("dailyprogrammer", 6)

        self.assertEqual(expected, actual)

    def test_6(self):
        expected = "dailyprogrammer"
        actual = caesar("jgorevxumxgsskx", 20)

        self.assertEqual(expected, actual)


class FirstOptionalBonusTestCase(unittest.TestCase):
    """
    Contains test for first optional bonus challenge
    """

    def test_sentence(self):
        expected = "Jgore Vxumxgsskx!"
        actual = caesar("Daily Programmer!", 6)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
