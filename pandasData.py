import pandas as pd
import re,os

df = pd.read_csv('실거래.csv')

print(len(df))

print(df.head())

print(df.시군구)

print(df[df.층>2])