import pandas as pd

df = pd.read_csv("D:\object_oriented_programming1.py\ML-Practice-code\Knn_alghorithms.csv")
# print(df.shape)
print(df.columns)
# df.drop(columns=['id','Unnamed: 0'], inplace=True)
# print(df.shape)
# print(df.isnull().sum())
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df.iloc[:,1],df.iloc[:,0],test_size=0.2, random_state=2)
# print(X_train.head())
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(X_train)
# print(X_test)