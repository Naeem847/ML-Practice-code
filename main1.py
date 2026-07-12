import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

from sklearn.linear_model import LinearRegression

file_path = 'D:\object_oriented_programming1.py\ML-Practice-code\data .csv'

df = pd.read_csv(file_path)

print(df.head())

print("dataset load successfully")

print("\ncolumns names")

print(df.columns)

# define featured (X) and target (Y) variables

X=df[['Age']]

Y=df['Salary']

# split the dataset into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=42)

# create and train the linear regression model

model = LinearRegression()

model.fit(X_train, Y_train)

# pridict on test data

Y_pred = model.predict(X_test)

# display model cofficients and intercept

print("\n print model coefficients and intercept:")
print(f"intercept: {model.intercept_}")
print(f"Slope: {model.coef_[0]}")




