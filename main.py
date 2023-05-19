import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("Hello World!")
 
# Assign data
data = {'Name': ['Jai', 'Princi', 'Gaurav',
                 'Anuj', 'Ravi', 'Natasha', 'Riya'],
        'Age': [17, 17, 18, 17, 18, 17, 17],
        'Gender': ['M', 'F', 'M', 'M', 'M', 'F', 'F'],
        'Marks': [90, 76, 'NaN', 74, 65, 'NaN', 71]}
# Convert into DataFrame
df = pd.DataFrame(data)
 
# Display data
print(df)
#Replace Nan in Marks with average of Marks column which is a string
#df['Marks'] = df['Marks'].replace('NaN', np.nan)
df['Marks'] = df['Marks'].astype(float)
#To check the data type of each column
#print(df.dtypes)
df['Marks'] = df['Marks'].fillna(df['Marks'].mean())

print(df)

