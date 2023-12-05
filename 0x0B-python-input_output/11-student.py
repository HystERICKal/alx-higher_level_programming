#!/usr/bin/python3
"""The student to JSON file"""


class Student:
    """ The class of student"""

    def __init__(self, first_name, last_name, age):
        """Student Constructorr"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Student  to JSON"""
        if (type(attrs) == list and
                all(isinstance(i, str) for i in attrs)):
            return {j: getattr(self, j) for j in attrs if hasattr(self, j)}
        return self.__dict__

    def reload_from_json(self, json):
        for i, j in json.items():
            setattr(self, i, j)
