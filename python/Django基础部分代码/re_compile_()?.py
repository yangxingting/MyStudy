#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:01:35 2019

@author: stevenyang

re compile ?

"""
import re

message='hell, I am Monkey   Lufy . I am king of sea'

zz=re.compile(r'Monkey (D)? Lufy')

obj_match=zz.search(message)

print(obj_match.group())