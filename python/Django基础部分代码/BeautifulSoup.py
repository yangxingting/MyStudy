#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:52:22 2019

@author: stevenyang

BeautifulSoup

"""

import requests
from bs4 import BeautifulSoup

respoonse=requests.get('http://en.people.cn/')
a=respoonse.text

soup=BeautifulSoup(a,'html.parser')


print(soup.p)
