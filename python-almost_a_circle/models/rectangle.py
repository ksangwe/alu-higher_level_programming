#!/usr/bin/python3
"""Rectangle module"""
from models.base import Base


class Rectangle(Base):
    """Rectangle class inheriting from Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    def to_dictionary(self):
        """Return dictionary representation of Rectangle"""
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """Assign attributes using args or kwargs"""
        attrs = ['id', 'width', 'height', 'x', 'y']
        # Use args first
        for i, val in enumerate(args):
            if i < len(attrs):
                setattr(self, attrs[i], val)
        # If no args, use kwargs
        if not args:
            for key, val in kwargs.items():
                if key in attrs:
                    setattr(self, key, val)

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )
