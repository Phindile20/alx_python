#!/usr/bin/python3
# models/base.py
#Write the first class Base

"""
This module contains the Base class.

"""


class Base:
    """the base class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """__Init__ method"""
        if id is not None:
            self.id = id
        else:
            self.id = self.__class__.__nb_objects + 1
            self.__class__.__nb_objects += 1

    def __repr__(self):
        """this shows the base"""
        return f"<Base id={self.id}>"
