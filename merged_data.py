#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 21 16:23:25 2019

@author: ayushitandon
"""
import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split 
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from scipy.stats import spearmanr, pearsonr
from sklearn import ensemble

storeNumber = int(sys.argv[1])

train = pd.read_csv('train.csv')
weather = pd.read_csv('weather.csv')
key = pd.read_csv('key.csv')


def merge_store_nbr(train, weather, key, store_nbr):
    train = train[train['store_nbr'] == store_nbr]
    df = weather.merge(key, how = 'outer', on = ['station_nbr'])
    df = df.merge(train, how = 'outer', on = ['store_nbr','date'])
    df = df[df['units'] > 0]
    return df

df = merge_store_nbr(train, weather, key, storeNumber)
df.to_csv('merged_data.csv', index=False)