import sys

from SortingAlgorithms.bubble_sort import bubble_sort
from SortingAlgorithms.insertion_sort import insertion_sort
from SortingAlgorithms.merge_sort import merge_sort
from SortingAlgorithms.quick_sort import quick_sort, quick_sort_f_math

import unittest

sys.setrecursionlimit(10 ** 6)
with open("test_array/array.txt", "r") as f:
    array = [int(x) for x in f.read()[1:-1].split(", ")]

with open("test_array/sorted.txt", "r") as f:
    sorted_array = [int(x) for x in f.read()[1:-1].split(", ")]

K = 200
large_sorted = sorted(sorted_array * K)


class TestSortingMethods(unittest.TestCase):
    def test_bubble_sort(self):
        self.assertEqual(bubble_sort(array.copy()), sorted_array)

    def test_insertion_sort(self):
        self.assertEqual(insertion_sort(array.copy()), sorted_array)

    def test_merge_sort(self):
        self.assertEqual(merge_sort(array.copy() * K), large_sorted)

    def test_quick_sort(self):
        self.assertEqual(quick_sort(array.copy() * K), large_sorted)

    def test_quick_sort_f_maths(self):
        self.assertEqual(quick_sort_f_math(array.copy() * K), large_sorted)
