import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Read a csv file
data = pd.read_csv("hadleydataset.csv")
data.head()
data.shape # 522 rows and 22 columns
# Data is not tidy and it is wide
# Let us melt the data
#We will keep the country and year same and change the sex and #age to sexage column using melt function
#Let us melt function
melted_data=data.melt(id_vars=['country', 'year'], value_vars=['m014', 'm1524', 'm2534', 'm3544', 'm4554', 'm5564', 'm65', 'mu', 'f04', 'f514', 'f014', 'f1524', 'f2534',
       'f3544', 'f4554', 'f5564', 'f65', 'fu'], var_name='sexage', value_name='Cases')

melted_data.head()
melted_data.tail()
melted_data['sex']=melted_data['sexage'].str.slice(0,1)
melted_data['age']=melted_data['sexage'].str.slice(1)
melted_data.head()
melted_data.tail()
#Let us convert the age to a range of values using dictionary and map function
melted_data['age'].count()
melted_data['age'].unique()
melted_data['age'].value_counts()

melted_data['age']=melted_data['age'].map({ '04': '0-4',  '514': '5-14', '014':'0-14', '1524':'15-24', '2534':'25-34', '3544':'35-44', '4554':'45-54', '5564':'55-64', '65':'65+', 'u':'unspecified'})
melted_data.head()
#Let us sort the data based on year, country and sex
melted_data=melted_data.sort_values(['country', 'year', 'sex'])
melted_data.head()
#Let us drop the sexage column
melted_data.drop('sexage', axis=1, inplace=True)
melted_data.head()
#Let us give index column a name
melted_data.index.name='index'
melted_data.head()
type(melted_data['sex'])
#Convert melted_data['sex'] to a string
melted_data['sex'] = melted_data['sex'].astype(str)
