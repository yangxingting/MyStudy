#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug  9 15:10:59 2019

@author: stevenyang

tushare data 接口

"""

import tushare as ts

df=ts.get_hist_data('000001',start='2017-01-01',end='2018-01-01'
                  ).reset_index().sort_values('date'))
'''
df=ts.get_hist_data('000001',start='2017-01-01',end='2018-01-01'
                  ).sort_index(ascending=True)
'''



df.low.plot()