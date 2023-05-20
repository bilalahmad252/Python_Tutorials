#Import Sckit Learn
from sklearn.impute import SimpleImputer
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
#Read a csv file
df_train=pd.read_csv("train.csv")
df_train.head()
#Let us read the test data
df_test=pd.read_csv("test.csv")
df_test.head()
print('Shape of Test', df_test.shape)
print('Shape of Train', df_train.shape)
#Let us set_option function to display all the columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)

#Let us drop the last column from test data
X_train=df_train.drop('SalePrice', axis=1)
Y_train=df_train['SalePrice']
X_train.shape
Y_train.shape
#Let us impute the missing values 
#Let us slect the numerical columns
numerical_columns_X_train=X_train.select_dtypes(include=['int64', 'float64']).keys() #Or .columns
numerical_columns_X_train
#Let us count the missing values in numerical columns

X_train[numerical_columns_X_train].isnull().sum()/X_train.shape[0]*100
#Let us create a heatmap to visualize the missing values
plt.figure(figsize=(25,25))
sns.heatmap(X_train[numerical_columns_X_train].isnull())
plt.show()
#plt.figure(figsize=(25,25))
#sns.heatmap(X_train.isnull())
#plt.show() For all columns

imputer_mean=SimpleImputer(strategy='mean')
#We can also use median or mode or some constant value
#Here is constant value example
#imputer_mean=SimpleImputer(strategy='constant', fill_value=0)

#imputer_mean is just an object of SimpleImputer class
#Let us fit the imputer object on the data
imputer_mean.fit(X_train[numerical_columns_X_train])
#Let us check the statistics of the imputer object
imputer_mean.statistics_
#Now put these mean values in the missing values using transform function
X_train[numerical_columns_X_train]=imputer_mean.transform(X_train[numerical_columns_X_train])
#Let us check if there are any missing values
X_train[numerical_columns_X_train].isnull().sum().sum()
#Let us apply the same imputer object on the test data
df_test[numerical_columns_X_train]=imputer_mean.transform(df_test[numerical_columns_X_train])
#Let us check if there are any missing values
df_test[numerical_columns_X_train].isnull().sum().sum()
