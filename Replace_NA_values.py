import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Read a csv file
data = pd.read_csv("train.csv")
data.isnull().sum()
data.shape # 1460 rows and 81 columns
data.head()
data.columns
#set option to display all columns
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
# Let us plot the missing values as heatmap
plt.figure(figsize=(25,25))
sns.heatmap(data.isnull(), yticklabels=False, cbar=False)
plt.show()
#Let us find the percentage of missing values
null_var=data.isnull().sum()/data.shape[0]*100
null_var
#Let us find the columns with more than 20% missing values
columns_drop= null_var[null_var>17].keys()
#Direct method to do the above
columns_drop= data.columns[data.isnull().sum()/data.shape[0]*100>17]
columns_drop
data_drop_col=data.drop(columns_drop, axis=1)
data_drop_col.shape

#Look at the heatmap again
plt.figure(figsize=(25,25))
sns.heatmap(data_drop_col.isnull())
plt.show()
#The other method is to drop the null values
data_drop_col_rows=data_drop_col.dropna()
data_drop_col_rows.shape
##Look at the heatmap again
plt.figure(figsize=(25,25))
sns.heatmap(data_drop_col_rows.isnull())
plt.show()
# How to slect the numerical and float columns
data_drop_col_rows.select_dtypes(include=['int64', 'float64']).columns
numeric_columns= ['Id', 'MSSubClass', 'LotArea', 'OverallQual', 'OverallCond','YearBuilt', 'YearRemodAdd', 'MasVnrArea', 'BsmtFinSF1', 'BsmtFinSF2','BsmtUnfSF', 'TotalBsmtSF', '1stFlrSF', '2ndFlrSF', 'LowQualFinSF','GrLivArea', 'BsmtFullBath', 'BsmtHalfBath', 'FullBath', 'HalfBath','BedroomAbvGr', 'KitchenAbvGr', 'TotRmsAbvGrd', 'Fireplaces','GarageYrBlt', 'GarageCars', 'GarageArea', 'WoodDeckSF', 'OpenPorchSF','EnclosedPorch', '3SsnPorch', 'ScreenPorch', 'PoolArea', 'MiscVal','MoSold', 'YrSold', 'SalePrice']

type(numeric_columns)
numeric_columns[0]

for i, var in enumerate(numeric_columns):
   print(i, var)
#Let us see the distribution of the numeric columns using distplot
#Let us superimpose the distplot of clean data over the original data
for i, var in enumerate(numeric_columns):
    plt.figure(i)
    sns.distplot(data[var], color='red', bins=20)
    sns.distplot(data_drop_col_rows[var], color='green', bins=20)
    plt.show()
#Let us see the information of object columns in clean and original data
data_drop_col_rows.select_dtypes(include=['object']).columns

object_columns=['MSZoning', 'Street', 'LotShape', 'LandContour', 'Utilities','LotConfig', 'LandSlope', 'Neighborhood', 'Condition1', 'Condition2','BldgType', 'HouseStyle', 'RoofStyle', 'RoofMatl', 'Exterior1st','Exterior2nd', 'ExterQual', 'ExterCond', 'Foundation', 'BsmtQual','BsmtCond', 'BsmtExposure', 'BsmtFinType1', 'BsmtFinType2', 'Heating','HeatingQC', 'CentralAir', 'Electrical', 'KitchenQual', 'Functional','GarageType', 'GarageFinish', 'GarageQual', 'GarageCond', 'PavedDrive','SaleType', 'SaleCondition']
#Let us concatenate the old data anc clean data
for i, var in enumerate(object_columns):
    pd.concat([data[var].value_counts()/data.shape[0]*100, data_drop_col_rows[var].value_counts()/data_drop_col_rows.shape[0]*100], axis=1, keys=['Original', 'Clean'])
 
