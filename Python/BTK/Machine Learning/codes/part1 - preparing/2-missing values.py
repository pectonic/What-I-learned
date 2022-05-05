#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May  4 19:02:38 2022

@author: pectonic
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# data importing and reading

datas = pd.read_csv('/home/pectonic/Documents/GitHub/What-I-learned/Python/BTK/Machine Learning/datas/eksikveriler.csv')

# from sci - kit learn
from sklearn.impute import SimpleImputer

imputer = SimpleImputer(missing_values=np.nan, strategy='mean') # taking mean the column and giving to non values

Age = datas.iloc[:,1:4].values # adding 3 column to Age 
print(Age)
imputer = imputer.fit(Age[:,1:4]) # this is for non values of ages
Age[:,1:4] = imputer.transform(Age[:,1:4]) 
print(Age)