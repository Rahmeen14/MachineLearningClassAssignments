#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:21:16 2019

@author: rahmeen
"""
import math
import numpy as np
import pandas as pd
attributes = []
def probability(A, val):
    countYes = 0
    indexVector = []
    for i in range(0, len(A)):
        if A[i] == val:
            countYes = countYes + 1
            indexVector.append(i)
    prob = countYes/len(A)
    return prob, indexVector
def probability2(A):
    countYes = 0
    for i in A:
        if i == 'Yes':
            countYes = countYes + 1
    prob = countYes/len(A)
    return prob
def populateAttributes(X):
    global attributes
    tempAttributes = []
    for j in range(0, len(X.iloc[0, :])):
        for i in range(0, len(X)):
            if X.iloc[i, j] not in tempAttributes:
                tempAttributes.append(X.iloc[i, j])
        attributes.append(tempAttributes)
        tempAttributes = []
        
def entropyEval(decisionVector):
    prob = probability2(decisionVector)  
    if prob == 1:
        return 0
    if prob == 0:
        return 0
    return ((math.log2(prob))*prob*-1) + (math.log2(1-prob))*(prob-1)


def findEntropySum(X, y, attributesList, index):
    summer = 0
    global dataset
    for i in range(0, len(attributesList)):
        prob, indices = probability(X.iloc[:, index], attributesList[i])
        newY = dataset.iloc[indices, 5]
        #print(prob)
        entro = entropyEval(newY)
        #print(entro, " Loop", i)
        summer = summer + prob*entro
    return summer

def mainFunction(X, y):
    entropySystem = entropyEval(y)
    index = 0 
    maxi = 0
    significantFeature = ''
    for i in X :
        entropyVal = entropySystem - findEntropySum(X, y, attributes[index], index)
        print("Entropy with respect to ", i, " is ", entropyVal)
        index = index+1
        if entropyVal > maxi:
            maxi = entropyVal
            significantFeature = i
    print("Maximum gain is observed in ",significantFeature, " with a value of", maxi )
# Importing the dataset
dataset = pd.read_csv('/home/rahmeen/SEM-6/ML/Experiments/EnjoySportMore.csv')
X = dataset.iloc[:, 1:5]
y = dataset.iloc[:, 5]
populateAttributes(X)
mainFunction(X, y)   
'''
Z = []
for i in X:
    Z.append(X[i])
Z[0]
mainFunction(X,y)
#print(len(X.iloc[0, :]))
ar = [0,1,4,5,7]
y = y[ar]
print(y)
print(entropyEval(y))
'''
