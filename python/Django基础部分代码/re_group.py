#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:18:28 2019

@author: stevenyang

find obj group

"""
import re

message='hello, everyone  I am steven , now live in shanghai ,\
        my teletephone num 86-18812345678, num2 (86)-19912345678'
        
#zz=re.compile(r'(\d\d)-(\d\d\d\d\d\d\d\d\d\d\d)')
#obj_match=zz.search(message)
        
zz=re.compile(r'(\(\d\d\))-(\d\d\d\d\d\d\d\d\d\d\d)')
obj_match=zz.search(message)
print(obj_match.group(1))