#!/usr/bin/python3
"""define a class"""


class Square:
    """represent a square class"""
    def __init__(self, size=0):
        """ inti func square
        Args:
            size: the nw number squared
        """
        self.__size = size

    @property
    def size(self):
        """retrive itself"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """init fucn
        Args:
            value: new value given
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")

