#!/usr/bin/python3
"""This module defines a function that prints a square."""


def print_square(size):
    """Prints a square with the character '#'."""

    # Check type
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    # Check value
    if size < 0:
        raise ValueError("size must be >= 0")

    # Print square
    for _ in range(size):
        print("#" * size)
