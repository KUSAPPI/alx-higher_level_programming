#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
Created on Wed June 6 2023
@author: Bright Kusi Appiah
"""


class LockedClass:
    """A locked class that only lets the user dynamically create the instance
    attribute 'first_name'"""
    __slots__ = ['first_name']
