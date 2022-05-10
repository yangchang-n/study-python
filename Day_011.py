#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df = pd.read_excel('./dataset/남북한발전전력량.xlsx')

df_ns = df.iloc[[0, 5], 3 : ]
df_ns.index = ['South', 'North']
df_ns.columns = df_ns.columns.map(int)
df_nst = df_ns.T
df_nst.plot(kind = 'bar')


# In[ ]:


import pandas as pd

df = pd.read_csv('./dataset/auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df.plot(x = 'mpg', y = 'weight', kind = 'scatter')


# In[ ]:


import pandas as pd

df = pd.read_csv('./dataset/auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df[['mpg', 'cylinders']].plot(kind = 'box')

