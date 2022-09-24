#!/usr/bin/python3
"""
Program that defines a Rectangle
"""

class Rectangle:
    """
    Defines methods to create attributes.
    """

    def __init__(self, width=0, height=0):
        """init the object's attribute"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """get the width"""
        return self.__width

     @width.setter
    def width(self, value):
        """Set the width and raise"""
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height and raise"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
