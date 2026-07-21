
import pandas as pd
df=pd.read_csv('myenv/sample_submission.tsv',sep='\t')
print(df)

# opening a CSV file from an url

import requests
from io import StringIO

url="D:\object_oriented_programming1.py\ML-Practice-code\myenv\sample_submission.csv"

req=requests.get(url)
data=StringIO(req.text)
df=pd.read_csv(data)
print(df)

#  seperate paramenters
import pandas as pd
df=pd.read_csv('myenv/sample_submission.tsv',sep='\t')
print(df)

