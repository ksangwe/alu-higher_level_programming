#!/usr/bin/python3
"""Square module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def to_dictionary(self):
        """Return dictionary representation of Square"""
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }

    def update(self, *args, **kwargs):
        """Assign attributes using args or kwargs"""
        attrs = ['id', 'size', 'x', 'y']
        # Use args first
        for i, val in enumerate(args):
            if i < len(attrs):
                if attrs[i] == 'size':
                    self.width = val
                    self.height = val
                else:
                    setattr(self, attrs[i], val)
        # If no args, use kwargs
        if not args:
            for key, val in kwargs.items():
                if key == 'size':
                    self.width = val
                    self.height = val
                elif key in attrs:
                    setattr(self, key, val)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )
