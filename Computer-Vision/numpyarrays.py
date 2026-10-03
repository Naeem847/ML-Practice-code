import numpy as np
from pyparsing import col
x=[1,2,3,4,5]
type(x)
print(type(x))
arr=np.array(x)

print(arr)

print(type(arr))

print(type(arr))
arr=np.arange(1,13)
print(arr)
arr=np.arange(1,13,3)
print(arr)
arr=np.zeros((2,4))
print(arr)
arr=np.ones((2,4))
print(arr)
np.random.seed(0)
arr1=np.random.randint(10,1000,50)
arr1=arr1.reshape(5,10)
print(arr1)
# practice array 2
np.random.seed(0)
arr2=np.random.randint(10,1000,50)
arr2=arr2.reshape(5,10)
arr2.min()
arr2.mean()
arr2.argmin()
print(arr2.argmin())
column = 0
row=0
arr2[0:5,0:5]=2
print(arr2[0:5,0:5])
print("arr3")
arr3=arr2.copy()
print(arr3[0:5,0:5])
