import pandas as pd
from sklearn.preprocessing import MinMaxScaler, StandardScaler

from sklearn.preprocessing import StandardScaler

from sklearn.preprocessing import LabelEncoder

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

df_cleaned=df.drop_duplicates()

# cleaned the duplicates in the dataset

# print the missing values in the dataset
print(df.isnull().sum())

df['Age'].fillna(df['Age'].mean(), inplace=True)

df['Salary'].fillna(df['Salary'].mean(), inplace=True)

print(df['Age'])

print(df['Salary'])

# initialize the scaler

scaler = MinMaxScaler()

# scale the features

df[['Age', 'Salary']] = scaler.fit_transform(df[['Age', 'Salary']])

# show normalized DataFrame

print(df[['Age', 'Salary']].head())

Scaler = StandardScaler()

# apply normalization

df[['Age', 'Salary']] = Scaler.fit_transform(df[['Age', 'Salary']])

# show normalized DataFrame

print("After Standard Scaling:")

print(df[['Age', 'Salary']].head())

# encode 'gender' column using label encoding

le=LabelEncoder()

df['Gender_encoded'] = le.fit_transform(df['Gender'])

print("Display the label encoded 'Gender' column:")

print(df[['Gender','Gender_encoded']].head())

# onehot encode 

df=pd.get_dummies(df, drop_first=True)

# display update data frame

print(df.head())

# # define featured x and target y
# X=df[['Age']]
# Y=df['Salary']


