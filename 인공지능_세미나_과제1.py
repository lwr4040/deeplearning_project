# -*- coding: utf-8 -*-
"""인공지능 세미나 과제1

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1zCfz4bGmJ8cSqgY6f0S63qZyRGVatqz8
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import pandas as pd
dt_clf= DecisionTreeClassifier(random_state=156, max_depth=1)

DF=pd.read_csv("최영준_심박수.csv")
print(DF)
data=DF['heartrate']
target=DF['drowneiss']
X_train, x_test, y_train, y_test=train_test_split(data,target,test_size=0.7)
dt_clf.fit(X_train,y_train)