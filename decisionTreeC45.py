#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 14 16:36:00 2019

@author: rahmeen
"""

import math
import pandas as pd
import numpy as np
attributes = []
lastSigFeature = []
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
def probability2(A, val):
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

def probability(A, val):
    #print("In prob")
    countYes = 0
    indexVector = []
    if len(A) == 0:
        return 0, []
    for i in range(0, len(A)):
        if A[i] == val:
            countYes = countYes + 1
            indexVector.append(i)
    prob = countYes/len(A)
    return prob, indexVector
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
    #print("In entropyEval")
    prob = probabilityYesNo(decisionVector)  
    if prob == 1:
        return 0, 'yes'
    if prob == 0:
        return 0, 'no'
    return (((math.log2(prob))*prob*-1) + (math.log2(1-prob))*(prob-1)), 'none'

def gainEval(vector, decision, attributesList):
    summer = 0
    #print("In findEntropySum")
    for i in range(0, len(attributesList)):
        #print(X.iloc[:, index], attributesList[i])
        prob, indices = probability(vector, attributesList[i])
        newY = decision[indices]#dataset.iloc[indices, 5]
        #print(prob)
        entro, dec = entropyEval(newY)
        #print(entro, " Loop", i)
        summer = summer + prob*entro
    return summer, dec

def discretise(vector, threshold):
    for i in range(0, len(vector)):
        if vector[i] <= threshold:
            vector[i] = 'low'
        else:
            vector[i] = 'high'
    return vector

def findBestThreshold(vector, decision):
    unique = list(set(vector))
    finalVec = []
    maxGain = 0
    thresh = 0
    for i in range(0, len(unique)):
        hum = list(vector)
        vect = discretise(hum, unique[i])
        gain, dec = gainEval(hum, y, ['low', 'high'])
        gain = 0.94 -  gain
        if gain > maxGain:
            maxGain = gain
            thresh = unique[i]
            finalVec = vect
    print(thresh)
    return finalVec
def findEntropySum(X, y, attributesList, index):
    summer = 0
    #print("In findEntropySum")
    for i in range(0, len(attributesList)):
        #print(X.iloc[:, index], attributesList[i])
        prob, indices = probability2(X.iloc[:, index], attributesList[i])
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

dataset = pd.read_csv('/home/rahmeen/SEM-6/ML/Experiments/EnjoySportContinuous.csv')

y = dataset.iloc[:, 5]
humidity = np.array(dataset.iloc[:,3])
temp = np.array(dataset.iloc[:, 2])
vecHum = findBestThreshold(humidity, y)
vecTemp = findBestThreshold(temp, y)
# Find the name of the column by index
n = dataset.columns[3]
dataset[n] = vecHum
n = dataset.columns[2]
dataset[n] = vecTemp
X = dataset.iloc[:, 1:5]
populateAttributes(X)
mainFunction(X, y, [], 'root')
print(thresh)
