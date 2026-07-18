import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

# %matplotlib inline

import sklearn

import seaborn as sns

import warnings

warnings.filterwarnings('ignore')


# plt.rcParams is a dictionary-like objects in matplotlib.it lets you customize the default 
# plt.rcParams["figure.figsize"] =[10,5]

file_path = 'D:\object_oriented_programming1.py\ML-Practice-code\data .csv'

df = pd.read_csv(file_path)

print(df.head())

plt.rcParams["figure.figsize"] =[10,5]
 
# ignore warnings

import warnings

# set the warnings filter to ignore Futurewarnings

