#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 11:41:46 2019

@author: stevenyang

导入csv数据

"""
import matplotlib.pyplot as plt
import numpy as np

x,y=np.loadtxt('/Users/aiding/Desktop/example_csv.txt',delimiter=','
               ,unpack=True)

plt.title('datebase from csv')
plt.xlabel('time-month')
plt.ylabel('money')
plt.plot(x,y)
plt.show()
