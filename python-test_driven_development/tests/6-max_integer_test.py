#!/usr/bin/python3
"""Unittest for max_integer([..])"""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer function"""

    def test_empty_list(self):
        """Test empty list"""
        self.assertIsNone(max_integer([]))

    def test_single_element(self):
        """Test list with one element"""
        self.assertEqual(max_integer([5]), 5)

    def test_multiple_elements(self):
        """Test list with multiple integers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)

    def test_unsorted_list(self):
        """Test unsorted list"""
        self.assertEqual(max_integer([3, 1, 4, 2]), 4)

    def test_negative_numbers(self):
        """Test list with negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_mixed_numbers(self):
        """Test list with positive and negative numbers"""
        self.assertEqual(max_integer([-5, 10, 3]), 10)

    def test_float_numbers(self):
        """Test list with floats"""
        self.assertEqual(max_integer([1.5, 2.5, 0.5]), 2.5)

    def test_same_numbers(self):
        """Test list with same numbers"""
        self.assertEqual(max_integer([2, 2, 2]), 2)

    def test_string_list(self):
        """Test list with strings"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")


if __name__ == "__main__":
    unittest.main()
