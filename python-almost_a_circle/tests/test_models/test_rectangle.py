#!/usr/bin/python3
"""Unit tests for Rectangle class"""

import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def test_creation(self):
        """Test rectangle creation"""
        r = Rectangle(10, 5)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 5)

    def test_inheritance(self):
        """Test inheritance from Base"""
        r = Rectangle(2, 3, 99)
        self.assertEqual(r.id, 99)

    def test_area(self):
        """Test area calculation"""
        r = Rectangle(4, 5)
        self.assertEqual(r.area(), 20)

    def test_invalid_width_type(self):
        """Test width type error"""
        with self.assertRaises(TypeError):
            Rectangle("10", 5)

    def test_invalid_height_type(self):
        """Test height type error"""
        with self.assertRaises(TypeError):
            Rectangle(10, "5")

    def test_invalid_width_value(self):
        """Test width <= 0"""
        with self.assertRaises(ValueError):
            Rectangle(0, 5)

    def test_invalid_height_value(self):
        """Test height <= 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, 0)

    def test_x_y_values(self):
        """Test x and y assignment"""
        r = Rectangle(10, 5, 2, 3)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)

    def test_invalid_x_type(self):
        """Test x type error"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, "2", 3)

    def test_invalid_y_type(self):
        """Test y type error"""
        with self.assertRaises(TypeError):
            Rectangle(10, 5, 2, "3")

    def test_invalid_x_value(self):
        """Test x < 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, -1, 0)

    def test_invalid_y_value(self):
        """Test y < 0"""
        with self.assertRaises(ValueError):
            Rectangle(10, 5, 0, -1)


if __name__ == "__main__":
    unittest.main()
