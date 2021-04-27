import pandas as pd
import re,os
from scipy import stats
import statsmodels.formula.api as smf

df=pd.read_csv('survey.csv')

#print(df.head())

#print(df.mean())
'''print(df.income.describe())

print(df.sex.value_counts())

print(df.groupby(df.sex).describe())
'''
male=df.income[df.sex=="m"]
female=df.income[df.sex=='f']

print(stats.ttest_ind(male,female))
'''
corr=df.corr()
print(corr)
corr.to_csv('corr.csv')
'''
model=smf.ols(formula='jobSatisfaction~English',data=df)

result=model.fit()

print(result.summary())