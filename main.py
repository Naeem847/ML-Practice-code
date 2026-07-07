import pandas as pd

df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\data .csv')

print(df.shape)

print("print first five rows of the dataset")

print(df.head())

print(df.head(10))

# print(df.tail(10))

print(df.dtypes)

print(df.isnull().sum())

df['Age']=df['Age'].fillna(df['Age'].median())

print(df['Age'])

