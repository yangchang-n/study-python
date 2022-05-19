#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

dataset_names = sns.get_dataset_names()
dataset_names


# In[ ]:


diamonds = sns.load_dataset('diamonds')
df = diamonds.loc[ : , ['carat', 'cut', 'price']]

df.set_index('cut', inplace = True)
grouped = df.groupby('cut')
diamonds


# In[ ]:


for key, group in grouped : 
    print('key :', key)
    print(group.head())


# In[ ]:


grouped_2 = grouped.get_group('Premium').head(5000)
grouped_2.set_index('carat', inplace = True)
grouped_2.sort_index(inplace = True)
grouped_2


# In[ ]:


plt.figure(figsize = (18, 5))
plt.plot(grouped_2)
plt.xlabel('carat', size = 12)
plt.ylabel('price', size = 12)
plt.title('다이아몬드 무게별 가격', size = 18)
plt.xticks(size = 15)
plt.yticks(size = 15)
plt.show()


# In[ ]:


fig, ax = plt.subplots()

ax.scatter(grouped_2.index, grouped_2['price'])
ax.set(xlim=(0, 2.5), ylim=(0, 10000))

plt.show()

