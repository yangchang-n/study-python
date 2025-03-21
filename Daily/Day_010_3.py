#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_csv('./dataset/auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']
print(df.info(), df.dtypes)
print(df.describe(include = 'all'))


# In[ ]:


import pandas as pd

df = pd.read_csv('./dataset/auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

print(df.mpg.count())
print(df['origin'].value_counts())
print(df.origin.dtype)
print(df['mpg'].mean())
print(df.mean(numeric_only = True))
print(df[['mpg', 'cylinders']].corr())
print(df['mpg'].median())

