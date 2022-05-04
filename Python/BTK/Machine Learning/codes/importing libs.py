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

datas = pd.read_csv('/home/pectonic/Documents/GitHub/What-I-learned/Python/BTK/Machine Learning/datas/veriler.csv')

print(datas)

height = datas[['boy']]
print(height)

height_and_weight = datas[['boy','kilo']]
print(height_and_weight)