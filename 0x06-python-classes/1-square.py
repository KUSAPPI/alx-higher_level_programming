#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 30 21:49:50 2023
@author: Bright Kusi Appiah
"""


class Square:
    """Class Square that has attributes. Instantiation with size

    Attributes:
        size (int): The size of the square
    """

    def __init__(self, size):
        """The __init__ method for Square class

        Args:
            size: (:obj: 'int'): A private instance size
        """
        self.__size = size
