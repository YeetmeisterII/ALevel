import unittest


def is_one(value):
    return value == 1


class TestIsOneMethod(unittest.TestCase):

    def test_true_int(self):
        self.assertEqual(is_one(1), True)

    def test_false_int(self):
        self.assertEqual(is_one(87361287), False)

    def test_string(self):
        self.assertEqual(is_one("The moon"), False)

    def test_list(self):
        self.assertEqual(is_one([1, 2, 4, 5, 6, 2, 6, 2, 7, 5, 4]), False)

    def test_long_list(self):
        self.assertEqual(is_one(list(range(2000))), False)
