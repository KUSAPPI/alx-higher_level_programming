#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 13 10:35:00 2023

@author: Bright Kusi Appiah
"""


def class_to_json(obj):
    """
    Creates a json representation of an object

    Arguments:
        obj (obj): The object inputted to create a class

    Return:
        A jason representation
    """
    return {key: value for (key, value) in obj.__dict__.items()
            if key in list(obj.__dict__.keys())}
