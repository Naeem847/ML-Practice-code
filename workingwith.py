
import pandas as pd
df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\psl_matches.csv')
print(df)

# # # opening a CSV file from an url

import requests
from io import StringIO

url="D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submission.csv"

req=requests.get(url)
data=StringIO(req.text)
df=pd.read_csv(data)
print(df)

# #  seperate paramenters
# import pandas as pd
df=pd.read_csv('myenv/sample_submission.tsv',sep='\t')
print(df)

# # index__col parameter 
df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submissio.csv',index_col='EmployeeID',header=1)
print(pd)

# # use cols__parameters in ML not necessary you will use all that necessart columns:

df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submissio.csv',usecols=['Name','Gender','Education'])
print(df)          

# # squaze parameters: if we execute this statement then return pandas series not return the data frame of pandas :
df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submissio.csv',usecols=['Name'],squeeze=True)
print(df)  

# # # skip/nrows parameters
df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submissio.csv',skiprows=[1,2,3])
print(df)

# # skip/nrows parameters
df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submissio.csv',nrows=3)
print(df)

df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submissio.csv',nrows=3)
print(df)

# # Encoding paremeters in this statement in any csv file not working properly then use ths statement
# # in this code any mistakes in any lines then that mistakes will be skip.then output will display
df=pd.read_csv('zomato.csv',encoding='latin-1',error_bad_lines=False)
print(df)

# # dtypes parameters
df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submissio.csv').info()

# # if we need spacific column convert into integer

df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submissio.csv',dtype={'salary':float})

#handling dates
df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submissio.csv',parse_dates=['Date'])
print(df.info())

# converters
# in this statement if we need in any column name change their properties  we shuld use this techniques

def rename(Winner):
    if Winner=="Karachi Kings":
        return "Kk"
    else:
        return Winner
rename("Karachi kings")

df=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\psl_matches.csv',converters={'Winner':rename})
print(df)

# Loading the huge dataset in chunks 

dfs=pd.read_csv('D:\object_oriented_programming1.py\ML-Practice-code\myenv\psl_matches.csv',chunksize=3)
for chunks in dfs:
   print(chunks.shape)