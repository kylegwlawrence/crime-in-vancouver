#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 23:11:08 2018

@author: kyle
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('/home/kyle/Documents/crime-in-vancouver/crime.csv')

#describe
df.describe()

#table of crimes by year
df2 = df.groupby('YEAR', as_index = False)['YEAR'].size()
print(df2)
#bar plot crimes by year
plt.bar(df2[



