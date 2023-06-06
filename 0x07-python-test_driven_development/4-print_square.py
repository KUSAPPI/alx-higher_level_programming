#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue June 6 11:42:00 2023

@author: Bright Kusi Appiah
"""


def print_square(size):
    """
    print a square of char #

    Args:
        size (int): size of the square

    Raises:
        TypeError: Exception if size is not integer
        ValueError: Exception if size is less than 0
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")

    elif size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        print('#'*size)
