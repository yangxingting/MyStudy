#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 16:10:37 2019

@author: stevenyang

零到多个相符的方法

"""

import re

text='I am soooooooo happy right now ,   yeah~~~~~~~'

# ? 匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式  0 or 1
#zz=re.compile(r'yeah(~)?')

# + 匹配1个或多个的表达式
#zz=re.compile(r'yeah(~)+')



# 匹配0个或多个的表达式。
zz=re.compile(r'yeah(~)*')
obj_match=zz.search(text)
print(obj_match.group())

