#!/usr/bin/python3
"""Unittest for Base class."""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base class."""

    def test_id_none(self):
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id + 1, b2.id)

    def test_id_given(self):
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_multiple_ids(self):
        b1 = Base()
        b2 = Base(5)
        b3 = Base()
        self.assertEqual(b3.id, b1.id + 1)


if __name__ == "__main__":
    unittest.main()
