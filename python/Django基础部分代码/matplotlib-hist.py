#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  8 15:49:17 2019

@author: aiding
直方图 plt.hist 
"""
import matplotlib.pyplot as plt

scores=[56,32,12,20,55,78,56,79,80,91,95,67,58,76,74,
       78,82,83,81,45,34,37,12,9,77,56,100]
bins=[0,20,40,60,80,100]

plt.title('class student score')
plt.xlabel('score stage')
plt.ylabel('score')

plt.hist(scores,bins,histtype='bar',rwidth=0.8,label="class1")
plt.legend()

plt.show()