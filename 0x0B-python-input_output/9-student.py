#!/usr/bin/python3
"""The student to JSON file"""


class Student:
    """ The class of student"""

    def __init__(self, first_name, last_name, age):
        """Student Constructorr"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Student  to JSON"""
        return self.__dict__
