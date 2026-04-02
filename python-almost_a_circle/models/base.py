#!/usr/bin/python3
"""Base class for all models"""


class Base:
    """This class manages id attribute for all future classes"""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
