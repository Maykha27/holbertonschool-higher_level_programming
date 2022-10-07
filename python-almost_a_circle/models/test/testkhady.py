#!/usr/bin/python3
"Unit tests for Rectangle class"
import unittest
from unittest import mock
import io
from models.rectangle import Rectangle
from models.base import Base



class TestRectangle(unittest.TestCase):
    """class testing the to_dictionary """
    def test_to_dictionary(self):
        """test the to_dictionary method"""
        Base._Base__nb_objects = 0
        a = Rectangle(6, 2)
        output = {'id': 1, 'width': 6, 'height': 2, 'x': 0, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(1, 3, 5)
        output = {'id': 2, 'width': 1, 'height': 3, 'x': 5, 'y': 0}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(4, 4, 1, 6)
        output = {'id': 3, 'width': 4, 'height': 4, 'x': 1, 'y': 6}
        self.assertDictEqual(a.to_dictionary(), output)
        a = Rectangle(2, 7, 4, 2, 18)
        output = {'id': 18, 'width': 2, 'height': 7, 'x': 4, 'y': 2}
        self.assertDictEqual(a.to_dictionary(), output)
