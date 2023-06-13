#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 13 10:35:00 2023

@author: Bright Kusi Appiah
"""
import json


def to_json_string(my_obj):
    """
    Returs a json string containing object's representation

    Arguments:
        my_obj (str): The inputed object to convert in json format

    Return:
        A json format text
    """
    return json.dumps(my_obj)
