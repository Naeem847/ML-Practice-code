import pandas as pd

df = pd.read_csv("D:\object_oriented_programming1.py\ML-Practice-code\Knn_alghorithms.csv")
print(df.shape)
print(df.columns)
# df.drop(columns=['id','Unnamed: 0'], inplace=True)
print(df.shape)
# # Features
X = df.drop('diagnosis', axis=1)

# # Target
y = df['diagnosis']
print(df.isnull().sum())
from sklearn.model_selection import train_test_split
# df.iloc[:,1:],df.iloc[:,0]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=2)
print(X_train.head())
from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print(X_train.shape)
print(X_test.shape)

from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train,y_train)
from sklearn.metrics import accuracy_score
y_pred=knn.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
score=[]

for i in range(1, 16):
    knn = KNeighborsClassifier(n_neighbors=i)
    knn.fit(X_train, y_train)
    y_pred = knn.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    score.append(accuracy)
    print(f"Accuracy for k={i}: {accuracy}")
import matplotlib.pyplot as plt
plt.plot(range(1, 16), score)

