#!/usr/bin/python3
"""
Class BaseGeometry based in the last task
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square data that inherits from Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(self.__size, self.__size)

    def area(self):
        """the area() method must be implemented
        """

        return self.__size*self.__size
