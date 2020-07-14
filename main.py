import pandas as pd
import csv
import math
import os
from convert_function import calling
from function2 import calling2, calling3
import sys
sys.dont_write_bytecode = True



################ Food-Froup ################


################## a - path to csv file containing Text  ######################

a = pd.read_csv('file1.csv')

################## b - path to csv file containing FAQ, Fruits and others 

b = pd.read_csv('file2.csv')

calling(a,b)



########    text cleaning ####################



data = pd.read_csv('./CB All Brand Complaints Weekly_280.csv')

df = pd.DataFrame(data, columns = ['UPC','Text'])
df1 = df[(df['Text'].str.contains('- Store')) | (df['Text'].str.contains('- store')) | (df['Text'].str.contains('- STORE'))]

df1.to_csv('intermediate.csv', index = True)

b2 = pd.read_csv('intermediate.csv')

calling2(b2)
calling3(b2)

os.remove("intermediate.csv")