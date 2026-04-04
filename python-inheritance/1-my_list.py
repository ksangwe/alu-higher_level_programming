#!/usr/bin/python3
"""
Module that defines a MyList class
"""


class MyList(list):
    """
    MyList inherits from list and adds a method to print sorted list
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order
        """
        print(sorted(self))
