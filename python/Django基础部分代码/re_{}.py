#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:22:51 2019

@author: stevenyang

{}确定重复次数

"""

import re

#text='I am soooooooo happy right now ,   yeah~~~~~~~'
#
#regular=re.compile(r'yeah(~){3}')
#obj_match=regular.search(text)
#print(obj_match.group())


message='hello , my phone num is 86-18888888888123456789'

regular=re.compile(r'(\d){0,3}-(\d){9,11}?')
obj_match=regular.search(message)
print(obj_match.group()) 