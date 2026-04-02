#!/usr/bin/python3
"""Rectangle class"""

from models.base import Base


class Rectangle(Base):
    """Rectangle that inherits from Base"""

    def __init__(self, width, height, *args):
        """Initialize Rectangle with flexible arguments"""

        # Default values
        x = 0
        y = 0
        id = None

        if len(args) == 1:
            # Could be id OR x depending on type
            if isinstance(args[0], int):
                id = args[0]
        elif len(args) == 2:
            x, y = args
        elif len(args) == 3:
            id, x, y = args

        super().__init__(id)

        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # WIDTH
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    # HEIGHT
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    # X
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    # Y
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    # AREA METHOD
    def area(self):
        """Returns area of the rectangle"""
        return self.width * self.height
