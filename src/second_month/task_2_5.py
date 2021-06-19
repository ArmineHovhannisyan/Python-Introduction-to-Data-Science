import pandas as pd
import numpy as np


df = pd.read_csv('Data/data.csv')
df_table = pd.read_table('Data/data.csv', sep=',')
print(df)
print(df_table)