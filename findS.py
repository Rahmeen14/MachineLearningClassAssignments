#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 10:53:34 2019

@author: rahmeen
"""

import numpy as np
import pandas as pd

# Importing the dataset
dataset = pd.read_csv('/home/rahmeen/SEM-6/ML/Experiments/EnjoySport.csv')
y = dataset.iloc[:, 7]
ans = []
for i in range(0, len(y)):
    if y[i] == "Yes" :
        ans.append(i)
X = (dataset.iloc[ans, 1:7])
Y = (dataset.iloc[ans, 7])
h = ['phi','phi','phi','phi','phi','phi']
print(len(X.iloc[0,:]))
print(len(Y))
for i in range(0, len(Y)):
    for j in range(0, len(X.iloc[0, :])):
       if h[j] == "phi":
           h[j] = X.iloc[i,j]
       elif h[j] != X.iloc[i,j]:
           h[j] = "?"
print(h)
