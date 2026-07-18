import pandas as pd

import matplotlib.pyplot as plt

df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\data1.csv')

print(df.info())

df=df.iloc[:,1:]

print(df.head())

plt.scatter(df['cgpa'],df['iq'],c=df['placement'])

print(plt.show())