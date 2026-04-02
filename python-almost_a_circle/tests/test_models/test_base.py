#!/usr/bin/python3
"""Unit tests for Base class"""

import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """Test cases for Base"""

    def test_id(self):
        b1 = Base()
        b2 = Base()
        b3 = Base(10)

        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 10)


if __name__ == "__main__":
    unittest.main()
