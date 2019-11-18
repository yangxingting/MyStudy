#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:35:28 2019

@author: stevenyang

  re    pipe

"""
import re
message='hello, dajihao woshi linkemeng zhang, my brother linkemeng wi ,\
         this  is  for fist time in stage '
zz=re.compile(r'linkemeng(| zhang| li)');

obj_match=zz.search(message)

print(obj_match.group())

