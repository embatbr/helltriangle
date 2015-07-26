#!/usr/bin/python3.4


"""Module covering the tests for module helltriangle.py.
"""


import unittest

from helltriangle import *


class HellTriangleTests(unittest.TestCase):
    """Class containing all unit tests.
    """
    def setUp(self):
        self.num_lines = 4
        self.lim_min = -10
        self.lim_max = 10
        self.default_example = [[6], [3, 5], [9, 7, 1], [4, 6, 8, 4]]

    def test_should_not_create_an_example_with_zero_lines(self):
        with self.assertRaises(InvalidNumLinesError) as context_manager:
            create_example(0, (self.lim_min, self.lim_max))

        e = context_manager.exception
        self.assertEqual(e.msg, 'The triangle must have at least 1 line.')

    def test_should_not_create_an_example_with_negative_lines(self):
        with self.assertRaises(InvalidNumLinesError) as context_manager:
            create_example(-1, (self.lim_min, self.lim_max))

        e = context_manager.exception
        self.assertEqual(e.msg, 'Negative number of lines? Really? Try again.')

    def test_should_not_create_an_example_with_equal_limit_ends(self):
        with self.assertRaises(InvalidLimitsError) as context_manager:
            create_example(self.num_lines, (self.lim_min, self.lim_min))

        e = context_manager.exception
        self.assertEqual(e.msg, 'No variability of values.')

    def test_should_not_create_an_example_with_limit_ends_swapped(self):
        with self.assertRaises(InvalidLimitsError) as context_manager:
            create_example(self.num_lines, (self.lim_max, self.lim_min))

        e = context_manager.exception
        self.assertEqual(e.msg, 'How can you have an interval starting from a point\
 higher than the end? Try again.')

    def test_should_create_a_valid_example(self):
        example = create_example(self.num_lines, (self.lim_min, self.lim_max))

        self.assertEqual(len(example), self.num_lines)
        for i in range(self.num_lines):
            self.assertEqual(len(example[i]), i + 1)
            self.assertTrue(min(example[i]) >= self.lim_min)
            self.assertTrue(max(example[i]) <= self.lim_max)

    def test_should_return_a_correct_path_and_maximum_total_for_a_valid_example(self):
        (path, result) = maximum_total(self.default_example)

        self.assertEqual(path, [(0, 0), (1, 1), (2, 1), (3, 2)])
        self.assertEqual(result, 26)


if __name__ == '__main__':
    unittest.main()