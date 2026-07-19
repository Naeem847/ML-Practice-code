import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split

df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\data1.csv')

print(df.info())

df=df.iloc[:,1:]

print(df.head())

plt.scatter(df['cgpa'],df['iq'],c=df['placement'])

print(plt.show())


# so now i want to apply the loogistic regression alghorithm 
# and extract the input and output columns

X = df.iloc[:, 0:2]
Y = df.iloc[:, -1]

# show the x exix 
print(X)
# show the Y exix 
print(Y)

# X_train,X_test,Y_train,Y_test
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.1)

print("\nX_train")

print(X_train)

print("\nX_test")

print(X_test)

print("\nY_train")

print(Y_train)

print("\nY_test")

print(Y_test)

from sklearn.preprocessing import StandardScaler

scaler=StandardScaler()

X_train=scaler.fit_transform(X_train)
print("\nScallinf the Data X_train")
print(X_train)


X_test=scaler.transform(X_test)
print("\nScallinf the Data X_test")
print(X_test)

# in this stage we train the model

from sklearn.linear_model import LogisticRegression

clf=LogisticRegression()

clf.fit(X_train,Y_train)

result=clf.fit(X_train,Y_train)
print(result)

print("\nprediction of the model")

Y_pred=clf.predict(X_test)

print(Y_pred)
print(Y_test)
# calculate the accuracy of the model
print("\naccuracy of the model")
from sklearn.metrics import accuracy_score

accuracy_score(Y_test,Y_pred)
test=accuracy_score(Y_test,Y_pred)
print(test)


from mlxtend.plotting import plot_decision_regions

plot_decision_regions(X_train, Y_train.values, clf=clf, legend=2)
plt.xlabel("CGPA")
plt.ylabel("IQ")
plt.title("Logistic Regression Decision Boundary")

plt.show()

#pickle is a library pickle convert the python object into file
import pickle
pickle.dump(clf,open('model.pkl','wb'))

pkl1=pickle.dump(clf,open('model.pkl','wb'))

print(pkl1)

