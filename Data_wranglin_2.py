import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Read a csv file
data = pd.read_csv("billboard.csv", encoding='ISO-8859-1')
#Let us find the columns names
data.columns
#Let us look at the head of the data
print(data.iloc[0:2, 10:12])
data.info()
#Number of columns
data.columns.__len__() #83
#Number of rows
data.__len__() #317
#Let us look at the first 10 rows
data.head(10)
#Let us plot the first song in the data from column 1 to 76
#.loc is used for indexing
#Without Range
plt.figure()
plt.plot(data.loc[0, 'x1st.week':'x76th.week'])
plt.show()
#With Range function we can get the range of values
plt.figure()
plt.plot(range(1,77), data.loc[0, 'x1st.week':'x76th.week'])
plt.show()

#Let us iterate through the data and plot the first 10 songs
plt.figure()
for index, row in data.iterrows():
    plt.plot(range(1,77), row['x1st.week':'x76th.week'], color='C0', alpha=0.1)
plt.show()

#Let us choose a subset of columns
bshort= data[['artist.inverted', 'track', 'time', 'date.entered', 'x1st.week', 'x2nd.week', 'x3rd.week']]
bshort.head()
#Let us rename the columns
bshort.columns = ['artist', 'track', 'time', 'date.entered', 'wk1', 'wk2', 'wk3']
bshort.head()
#Let us melt the data .melting is the process of converting the data from wide to long
bmelt = bshort.melt(['artist', 'track', 'time', 'date.entered'], ['wk1', 'wk2', 'wk3'], 'week', 'rank')
bmelt.head()
#Let us use query to filter the data
bmelt.query('track == "Liar"')
#Other way to do the same thing
bmelt[bmelt.track == 'Liar']
#Let us convert the week to integer
bmelt['week'] = bmelt['week'].apply(lambda s: int(s[2]))
bmelt.head()
#Let us conver the date.entered to proper date format
bmelt['date.entered'] = pd.to_datetime(bmelt['date.entered'])
bmelt.head()


#Create a data frame
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'C': [7, 8, 9]})
df
df.loc[0:2, ['A','C']]
#Select column A and B with values less than 3
df.loc[(df['A'] < 3 ) & (df['B'] < 6), ['A', 'B']]

#Subset values less than 3 in column A and less than 6 in column B
df.loc[(df['A'] < 3) & (df ['B'] < 6), ['A', 'B']]
df.iloc[1:, 2]

#LEt us create a data frame to undersatnd groupby function
df = pd.DataFrame({'key': ['A', 'B', 'C', 'A', 'B', 'C'], 'data': range(6)}, columns=['key', 'data'])

df.groupby('key').sum()
#LEt us understand ma
df.groupby('key').aggregate(['min', np.median, max])
#Let us understand the map function
#LEt us separate % from 30% and convert it to float
df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df['C'] = df['A'].map(lambda x: x * 2)
df

