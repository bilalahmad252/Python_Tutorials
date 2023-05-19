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
print(data.head())
data.info()
#Number of columns
data.columns.__len__() #83
#Number of rows
data.__len__() #317
