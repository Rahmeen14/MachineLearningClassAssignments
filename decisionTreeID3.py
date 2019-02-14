#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 00:45:43 2019

@author: rahmeen
"""

import math
import pandas as pd
attributes = []
lastSigFeature = []
dataset = pd.read_csv('/home/rahmeen/SEM-6/ML/Experiments/EnjoySportMore.csv')
X = dataset.iloc[:, 1:5]
y = dataset.iloc[:, 5]
def populateAttributes(X):
    global attributes
    tempAttributes = []
    for j in range(0, len(X.iloc[0, :])):
        for i in range(0, len(X)):
            if X.iloc[i, j] not in tempAttributes:
                tempAttributes.append(X.iloc[i, j])
        attributes.append(tempAttributes)
        tempAttributes = []
populateAttributes(X)

def probabilityYesNo(A):
    #print("In pYN")
    countYes = 0
    if len(A) == 0:
        return 0
    for i in A:
        if i == 'Yes':
            countYes = countYes + 1
    prob = countYes/len(A)
    return prob

def entropyEval(decisionVector):
    #print("In entropyEval")
    prob = probabilityYesNo(decisionVector)  
    if prob == 1:
        return 0, 'yes'
    if prob == 0:
        return 0, 'no'
    return (((math.log2(prob))*prob*-1) + (math.log2(1-prob))*(prob-1)), 'none'

def probability(A, val):
    #print("In prob")
    countYes = 0
    indexVector = []
    if len(A) == 0:
        return 0, []
    for i in A.index.values:
        if A[i] == val:
            countYes = countYes + 1
            indexVector.append(i)
    prob = countYes/len(A)
    return prob, indexVector

def findEntropySum(X, y, attributesList, index):
    summer = 0
    #print("In findEntropySum")
    for i in range(0, len(attributesList)):
        #print(X.iloc[:, index], attributesList[i])
        prob, indices = probability(X.iloc[:, index], attributesList[i])
        newY = y[indices]#dataset.iloc[indices, 5]
        #print(prob)
        entro, dec = entropyEval(newY)
        #print(entro, " Loop", i)
        summer = summer + prob*entro
    return summer, dec

def id3(X, y, lastSigFeature, val):
    #print("In id3")
    entropySystem, dec = entropyEval(y)
    #print(entropySystem)
    if entropySystem == 0:
        #print("Endss")
        print("For ",lastSigFeature[len(lastSigFeature)-1]," as", val,  " decision is ", dec)
       
        return 'none', 0, dec
    else:
        #print("Still here")
        maxi = 0
        sigInd = 0
        index = 0
        significantFeature = ''
        for i in X :
            if i not in lastSigFeature:
                #print(attributes[index], index)
                value, dec = findEntropySum(X, y, attributes[index], index)
                entropyVal = entropySystem - value
                #print("Entropy with respect to ", i, " is ", entropyVal)
                if entropyVal > maxi:
                    maxi = entropyVal
                    significantFeature = i
                    sigInd = index
            index = index+1    
        if len(lastSigFeature) > 0:
            print("For ", lastSigFeature[len(lastSigFeature)-1],  "as", val, "Maximum gain is observed in ",significantFeature, " with a value of", maxi )
        else:
            print("For node as", val, "Maximum gain is observed in ",significantFeature, " with a value of", maxi )

        return significantFeature, sigInd, dec
 
populateAttributes(X)
def mainFunction(X, y, lastSigFeature, val):
    sigFeature, sigInd, dec = id3(X, y, lastSigFeature, val)
    if sigFeature == 'none':
       return
    lastSigFeature.append(sigFeature)
    attri = attributes[sigInd]
    for i in attri:
        df_new=X[X[sigFeature]==i]
        y_new=y[df_new.index.values]
        mainFunction(df_new, y_new, lastSigFeature, i)
    lastSigFeature.pop()
        
mainFunction(X, y, [], 'root')
