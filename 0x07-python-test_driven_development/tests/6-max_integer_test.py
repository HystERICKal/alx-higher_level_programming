#!/usr/bin/python3
import unittest

"""Finction for Max integer - Unittest"""

max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ Max integer testing """
    def test_isempty(self):
        """ Testing if empty """
        self.assertTrue(len(list))

    def test_isvalues(self):
        """ Y=Testing if int values """
        x = 0
        while x < len(list):
            self.assertIsInstance(list[x], int)
            x += 1
