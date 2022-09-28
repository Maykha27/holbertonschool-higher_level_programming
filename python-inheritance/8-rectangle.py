#!/usr/bin/python3
"""
Class BaseGeometry based in the last task
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Rectangle data inherits from BaseGeometry
    """

def ___init__(self, width, height):
    super().integer_validator("width", width)
    super().integer_validator("height", height)
    self.__width = width
    self.__height = height
