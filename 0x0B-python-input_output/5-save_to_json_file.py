#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:35:00 2023

@author: Bright Kusi Appiah
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Save object to a file

    Arguments:
        my_obj (obj): The inputed object to convert in json format
        filename (str): The name of the output file

    Return:
        A file with a text in jason format
    """
    with open(filename, 'w', encoding='utf-8') as file:
        return file.write(json.dumps(my_obj))
