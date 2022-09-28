#!/usr/bin/python3
"""
Write a class MyList that inherits from list
"""


class MyList(list):
    """contains list
    """
    def print_sorted(self):
        """print_sorted-method to sort a list"""
        print(sorted(self[:]))
