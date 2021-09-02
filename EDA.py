# -*- coding: utf-8 -*-
"""
Created on Thu Aug 12 18:30:38 2021

@author: Lenovo
"""

#Multiple linear regresssion

#importing the libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#importing the dataset
dataset = pd.read_csv('50_Startups_EDA.csv')

#shape of the data
dataset.shape 
dataset.shape[0]
dataset.shape[1]

# How the data is distributed
dataset.describe()

#Quick look on the data
dataset.head(10)
dataset.tail(10)

#Display settings
pd.options.display.max_rows  #default - 60
pd.options.display.max_columns # default - 0
pd.set_option('display.max_rows',500)
pd.set_option('display.max_columns',500)
pd.set_option('display.width',1000)

# Data type and null
dataset.info()
dataset.dtypes

# categorical data
dataset.nunique()

dataset.iloc[:,4].value_counts()

for i in range (0,dataset.shape[1]):
    print("-----------------",dataset.columns[i],"-------------------")
    print(dataset.iloc[:,i].value_counts())
    print("----------------------------------------------------------")
    
#Visualuzation of categorical data in countplot
sns.countplot(x = 'State',data = dataset)

#Total null values
dataset.isnull().sum()
sns.heatmap(dataset.isnull(), cbar=False)

#Fix the missing values in dataframes
#dataset['R&D Spend'],fillna((dataset[R&D Spend],mean()),inplace=true)
dataset.mean()
dataset.mode()
dataset['R&D Spend'],fillna((dataset['R&D Spend'].mean()))
dataset.fillna(dataset.mean(), inplace=True)

#Duplicate
dataset.duplicated().sum()
dataset[dataset.duplicated(keep='first')]
dataset[dataset.duplicated(keep='last')]
dataset[dataset.duplicated(['State'])]

#Drop duplicate
#dataset=dataset.drop_duplicates(keep='first')
dataset.drop_duplicates(keep= 'first', inplace = True)

# heatmap to identify correlation & importance of variable
dataset.corr()





