#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:34:53 2019

@author: aiding  

柱状图：bar
"""
import matplotlib.pyplot as plt

x1=[1,3,5]
y1=[4,7,11]

x2=[2,4,6]
y2=[5,8,10]



plt.title('2019 copany sales')
plt.xlabel('month')
plt.ylabel('money')

plt.bar(x1,y1,label='company A')
plt.bar(x2,y2,label='company B')
plt.legend() 

plt.show()


