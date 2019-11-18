#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:46:01 2019

@author: stevenyang

crawler requests

"""
import requests

respoonse=requests.get('http://en.people.cn/')
text=respoonse.text
print(text)
