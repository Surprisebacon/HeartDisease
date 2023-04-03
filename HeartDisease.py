# importing necessary packages
import pandas as pd 
import numpy as np
from sklearn.linear_model import LinearRegression
clf = LinearRegression()
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import cross_val_score
from sklearn import linear_model

# Reading the file, and make it into a DataFrame
HD = pd.read_csv('HeartDisease.csv')
hd = pd.DataFrame(HD)

hd.head()
