message="learning python is fun!!"
print(f"message: {message}")
x=12
y="hello world!"
z=3.14
print(f"x:{x},type of x:{type(x)}")
print(f"y:{y},type of y:{type(y)}")
print(f"z:{z},type of z:{type(z)}")
# basic arithmetic operations
a=10
b=5
print(f"a+b={a+b}")
print(f"a-b={a-b}")
print(f"a*b={a*b}")
print(f"a/b={a/b}")

# # intiger datatypes
integer_variable=10
negative_integer_variable=-5
large_integer_variable=1000000000
print(f"integer_variable: {integer_variable}, type: {type(integer_variable)}")
print(f"negative_integer_variable: {negative_integer_variable}, type: {type(negative_integer_variable)}")
print(f"large_integer_variable: {large_integer_variable}, type: {type(large_integer_variable)}")
# floating point numbers
float_variable=3.14
negative_float_variable=-2.5
scientific_variable=3e4
print(f"float_variable: {float_variable}, type: {type(float_variable)}")
print(f"negative_float_variable: {negative_float_variable}, type: {type(negative_float_variable)}")
print(f"scientific_variable: {scientific_variable}, type: {type(scientific_variable)}")
# Strings (str)
# # string is a sequence of characters enclosed in single or double quotes
string_variable="Hello, World!"
string_variable2='Python is fun!'
multiple_line_string="""This is a multi-line string.
It can span multiple lines."""
print(f"string_variable: {string_variable}, type: {type(string_variable)}")
print(f"string_variable2: {string_variable2}, type: {type(string_variable2)}")
print(f"multiple_line_string: {multiple_line_string}, type: {type(multiple_line_string)}")
# string cancatination
full_name="John"+" "+"Doe"
print(f"full_name: {full_name}, type: {type(full_name)}")
# complex numbers
complex_variable=2+3j
another_complex_variable=1-2j
print(f"complex_variable: {complex_variable}, type: {type(complex_variable)}")
print(f"real part of complex_variable: {complex_variable.real}, imaginary part of complex_variable: {complex_variable.imag}")
print(f"another_complex_variable: {another_complex_variable}, type: {type(another_complex_variable)}")
# boolean values
# boolean represents truth values and can be either True or False
boolean_variable=True
boolean_variables=False
print(f"boolean_variable: {boolean_variable}, type: {type(boolean_variable)}")
print(f"boolean_variables: {boolean_variables}, type: {type(boolean_variables)}")
# boolean operations
a=True
b=False
print(f"a and b: {a and b}")
print(f"a or b: {a or b}")
print(f"not a: {not a}")

# type conversion(casting)
# python allow you convert one data to another data type
int_value=10
float_value=2.3435
str_val="123"
bool_val=True
int_from_str=int(str_val)
converted_float=float(int_value)
print(f"converted_float: {converted_float}, type: {type(converted_float)}")
converted_str=str(float_value)
print(f"converted_str: {converted_str}, type: {type(converted_str)}")
converted_bool=bool(int_value)
print(f"converted_bool: {converted_bool}, type: {type(converted_bool)}")
# list changeble data type
my_list=[1,2,3,"apple","banana",True,3.14]
print(f"my_list: {my_list}, type: {type(my_list)}")
print(f"first element of my_list: {my_list[0]}")
# list are changeble muatable
my_list.append("cherry")
print(f"my_list after append: {my_list}")
my_list.remove("banana")
print(f"my_list after removing 'banana': {my_list}")
my_list[1]=20
print(f"my_list after changing second element: {my_list}")
# tuple immutable data type
my_tuple=(1,2,3,"apple","banana",True,3.14)
print(f"my_tuple: {my_tuple}, type: {type(my_tuple)}")
# Dictionary key-value pairs
my_dict={"name":"John","age":30,"city":"New York"}
print(f"my_dict: {my_dict}, type: {type(my_dict)}")
print(f"name from my_dict: {my_dict['name']}")
print(f"age from my_dict: {my_dict['age']}")
print(f"city from my_dict: {my_dict['city']}")
# dictionary are changeble mutable
my_dict["age"]=31
print(f"my_dict after changing age: {my_dict}")
my_dict["country"]="USA"
print(f"my_dict after adding country: {my_dict}")
# the range function()
for i in range(5):
    print(i)

for i in range(2,8):
    print(i)
    
for i in range(0,5,11):
    print(i)
    
for number in range(5):
    if number==3:
        pass
    print(f"number: {number}")
# using the break statement in loop
for number in range(5):
    if number==3:
        break
    print(f"number: {number}")

else:
    print("Loop completed without break")

#     # loop inside th e another loop
#     # outer loop control rows and inner loop control columns
for rows in range(3):
    for columns in range(2):
        print(f"rows: {rows}, columns: {columns}")
# built in punctuation module
text="Hello, World! This is a test string."
print(f"Original text: {text}")
print(f"Length of text: {len(text)}")

# functions greeting
def greeting():
    print(f"hello my name is Muhammad Naeem!")
# calling the function
greeting()
# calculation the area
def calculate_area(length,width):
    area=length*width
    print("length:",length)
    print("width:",width)
    print("area:",area)

calculate_area(5,10)
# local scope variables:
def roll_no():
    roll_number=12345
    print(f"roll_number inside function: {roll_number}")

roll_no()
# global scope variable we access outside the function or anywhere in the program we can access
global_roll_number=67890

def display_roll_number():
    print(f"global_roll_number inside function: {global_roll_number}")

display_roll_number()
print(f"global_roll_number outside function: {global_roll_number}")
# function in parameters
def desplay_result(name,marks):
    print(f"Name: {name}, Marks: {marks}")
    if marks>=50:
        print("results is pass")
    else:
        print("results is fail")
desplay_result("Ali",75)     

# # working on numpy
import numpy as np
arr=np.array([1,2,3,4])
print(arr)
# zeros in numpy
arr=np.zeros((2,3))
print(arr)
# np .empty
arr=np.empty((2,2))
print(arr)
# arrange functions
arr=np.arange(0,10,2)
print(arr)
# # linespace functions
arr=np.linspace(0,1,5)
print(arr)
# check the arrays dimensions
arr=np.array([[1,2,3],[3,4,5]])
print("2 ndim",arr.ndim)
print("2 ndim",arr.size)
print("2 ndim",arr.dtype)

# flatten() function
arr=np.array([[1,2,3],[3,4,5]])
print(arr.flatten())
# worknig with pandas
import pandas as pd
marks=pd.Series([80,90,70,85],index=['Ali','Ahmed','Sara','Zara'])
print(marks)
print("ali",marks['Ali'])
print("Ahmed",marks.iloc[1])
print(marks.values)
print(marks.index)
# worknig with data json data set
import pandas as pd
import numpy as np
data={
  "name": ["Naeem","Ali","Ahmed"],
  "age": [25, 30, 35],
  "marks": [85, 90, 75],
  "department": ["Computer Science", "Mathematics", "Physics"]
}
df=pd.DataFrame(data)
print(df)  
# # add some more key and values in this json file?
df=pd.read_csv("student.csv")
print(df.head(n=3))
print(df.tail(n=2))
print(df.sample(3,random_state=1))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
# selecting a single column
ages=df['age']
print(ages)
# selecting a multiple columns
subsets=df[['name','marks']]
print(subsets)
# selecting rows by index
import matplotlib.pyplot as plt
x = ['A', 'B', 'AB','A+', 'B+']
# x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

plt.plot(x, y)
print("Line graph plotted successfully!")
print(plt.plot(x, y))
print(plt.show())
plt.scatter(x, y)
print("Line graph plotted successfully!")
print(plt.scatter(x, y))
print(plt.show())
plt.bar(x, y)
plt.title("blood groups vs men count")
plt.grid(True)
plt.xlabel("blood groups")
plt.ylabel("men count")
plt.legend(["blood groups"])
print("Line graph plotted successfully!")
print(plt.bar(x, y))
print(plt.show())
# # from matplotlip.line import Linestyle
nx=np.linspace(0, 10*np.pi, 1000)
ny=np.sin(nx)
fig, ax=plt.subplots(figsize=(10, 3))
ax.plot(nx, ny, color="C1")
print(plt.show())
# plt.plot(nx, ny, linestyle=Linestyle.DASHDOT)
import matplotlib.pyplot as plt
import numpy as np
x=["A","B","AB","A+","B+"]
y=[2,4,6,8,10]
plt.bar(x,y)
plt.title("blood groups vs men count")
plt.grid()
plt.xlabel("blood groups")
plt.ylabel("men count")
plt.legend(["blood groups"])
print(plt.show())
nx=np.linspace(0,10*np.pi,1000)
x=np.cos(nx)
ny=np.sin(nx)
# data for pie plot
pie_data=[30,20,15,10]
pie_labels=["Category1","Category2","Category3","Category4"]
fig,((plot1,plot2),(plot3,plot4))=plt.subplots(2,2,figsize=(10,5))

plot1.plot(nx,ny,color="C1")

plot2.pie(pie_data,labels=pie_labels,autopct="%1.1f%%",startangle=90)
plot3.hist(ny)
plot4.barh(pie_labels,pie_data)
print(plt.show())
# # exploring the data preprocessing and visualization
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

df=pd.read_csv("heart_desease_ML.csv")
print(df.head())
target_values = [
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
    1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
        1, 1, 1, 1, 1, 1, 1, 1, 1, 1,1, 1, 1, 1, 1, 1, 1, 1, 1, 1,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
0,0,0,0
    # continue until you have one value for every row
]

df["target"] = target_values
print(len(df))
print(len(target_values))

df.to_csv("heart_desease_ML.csv", index=False)

print(df.head())
print(df.notnull())
print(df.drop_duplicates())
print(df.info())
# print(df.fillna())
print(df['target'].unique())
df['target'].value_counts().plot(kind="bar",color=["blue","green"]);
plt.xlabel("Target")
plt.ylabel("Number of Patients")
plt.title("Heart Disease Target Distribution")
print(plt.show())
# checking for any missing value
df.isna().sum()
print(df.isna().sum())
# gender vs target
print(pd.crosstab(df.target,df.gender.map({0:"female-0",1:"male-1"})))
pd.crosstab(df.target,df.gender).plot(kind='bar')
# print(pd.crosstab(df.target,df.gender.map({0:"female-0",1:"male-1"}))).plot(kind='bar')
plt.xlabel("0=No Disease,1=Disease")
plt.ylabel("Count")
plt.legend(['Females','Males'])
print(plt.show())
# finding the others patterns
plt.figure(figsize=(10,5))
# take a look at the age VS thalach in a seatter plot
plt.scatter(df.age[df.target==0],df.maximumHeartrate[df.target==0],c="green");
plt.scatter(df.age[df.target==1],df.maximumHeartrate[df.target==1],c="red");
df.age.plot.hist()
plt.title("Age VS Heart Rate")
plt.xlabel("Age")
plt.ylabel("Heart Rate")
plt.legend(['No Desease','Desease'])
print(plt.show())
# check the age distribution
df.age.plot.hist()
print(df.show())
print("hello world")
import numpy as np
part=30
total=120
pct=(part/total) * 100
print(f"Percentage: {pct}%")
# A shop has 149 items and sold 44.so what percentege sold
total_item=149
sold=44
t_percentage=(sold/total_item)*100
print(t_percentage)

# To simplify the ratio 20:12 to its lowest form
import math

a = 20
b = 12

gcd = math.gcd(a, b)

print(f"Simplified ratio: {a // gcd}:{b // gcd}")