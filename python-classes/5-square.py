#!/usr/bin/python3
"""Square generation module for Python project 0x06
"""


class Square:
    """class defined for square generation
    """

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """square area
        """
        return self . __size * self . __size

    def my_print(self):
        """prints in stdout the square with the character #
        """
        if self.size > 0:
            for l in range(self . size):
                for w in range(self.size):
                    print("#", end='')
                print()
        else:
            print()
