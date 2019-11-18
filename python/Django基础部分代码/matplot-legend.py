# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import matplotlib.pyplot as plt

#x=['1月','2月','3月','4月','5月','6月','7月','8月','9月','10月','11月','12月']

x1=['Jan','Feb','mar','Apr','may','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
y1=[3,6,7,4,5,6,7,4,5,9,11,12]

x2=['Jan','Feb','mar','Apr','may','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
y2=[2,4,5,3,4,5,6,4,8,7,6,9]

plt.title('2019 company turnover')
plt.xlabel('month');
plt.ylabel('money(million)')


plt.plot(x1,y1,label='A company')
plt.plot(x2,y2,label='B company')

#legend 为每条图线添加图例
plt.legend()
plt.show