#Read a CSV from a URL
import pandas as pd
import requests
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
#Read aan xls file
data = pd.read_csv("Planets.csv")
#Let us find the columns names
data.columns
data
data.info()
data.__len__()
data.Mass
type(data['FirstVisited'])
#Let us convert it to datetime
data['FirstVisited'] = pd.to_datetime(data['FirstVisited'])
data['FirstVisited']
type(data['FirstVisited'])
data.FirstVisited.dt.day #You can find year, month, day, hour, minute, second, dayofweek, dayofyear, weekofyear, weekday, quarter
data.FirstVisited.dt.dayofweek
#

