#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 14:03:30 2019

@author: stevenyang

正则表达式 re.compile 

"""

import re 

message='hello, everyone  I am steven , now live in shanghai ,\
        my teletephone num 86-18812345678, num2 86-19912345678'

#表达式
zz=re.compile(r'\d\d-\d\d\d\d\d\d\d\d\d\d\d')
        
#表达式和字符串关联  得到匹配对象
match_obj=zz.search(message)
        
#得到匹配结果
print(match_obj.group())