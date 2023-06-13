#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:35:00 2023

@author: Bright Kusi Appiah
"""


def read_file(filename=""):
    """
    Reads the file

    Arguments:
        filename (str): The name of the file to open
    """
    with open(filename, encoding='utf-8') as file:
        print(file.read(), end='')
