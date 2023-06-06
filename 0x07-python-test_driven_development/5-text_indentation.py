#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue June 6 11:42:00 2023

@author: Bright Kusi Appiah
"""


def text_indentation(text):
    """
    prints a string with 2 new lines after '.', '?', and ':'

    Args:
        text (int): text to print

    Raises:
        TypeError: "text must be a string"
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    string = text.replace('.', '.\n\n').replace(':', ':\n\n')\
        .replace('?', '?\n\n')
    for i in range(len(text)):
        string = string.replace('\n ', '\n')

    print(string, end='')
