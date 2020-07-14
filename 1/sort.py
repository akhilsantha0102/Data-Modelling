import pandas as pd
import os
df = pd.read_csv('./final.csv')
df = df.sort_values('root')
df.to_csv('Full_List_sorted.csv', index=False)
df = pd.read_csv('./Full_List_sorted.csv')
df['4RF Last Test Date'] = pd.to_datetime(df['4RF Last Test Date'])
df = df.sort_values(by =['root', '4RF Last Test Date'])
df.to_csv('Full_List_sorted2.csv', index=False)
os.remove("./Full_List_sorted.csv")


