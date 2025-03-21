#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

df = pd.read_excel('./dataset/남북한발전전력량.xlsx')
df.replace('-', np.nan, inplace = True)
df.head()


# In[ ]:


import pandas as pd
import numpy as np

df = pd.DataFrame({'c1':['a', 'a', 'b', 'a', 'b'],
                  'c2':[1, 1, 1, 2, 2],
                  'c3':[1, 1, 2, 2, 2]})
df.duplicated()
df.drop_duplicates(subset = ['c2', 'c3'], inplace = True)
df


# In[ ]:


import pandas as pd
import numpy as np

df = pd.read_csv('./dataset/auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df['kpl'] = (df['mpg'] * 0.425).round(2)

df['horsepower'].replace('?', np.nan, inplace = True)
df['horsepower'] = df['horsepower'].astype('float')
# df['horsepower'].dropna(inplace = True)
df.dropna(subset = ['horsepower'], axis = 0, inplace = True)

df.origin.replace({1 : 'USA', 2 : 'EU', 3 : 'JPN'}, inplace = True)
df.origin = df.origin.astype('category')

df['model year'] = df['model year'].astype('category')
df['model year'].sample(10)


# In[ ]:


import pandas as pd
import numpy as np
from sklearn import preprocessing as pre

df = pd.read_csv('./dataset/auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df.horsepower.replace('?', np.nan, inplace = True)
df.horsepower = df.horsepower.astype('float')
df.dropna(subset = ['horsepower'], axis = 0, inplace = True)

count, bin_label = np.histogram(df.horsepower, bins = 3)
bin_names = ['저출력', '보통출력', '고출력']
df['hp_bin'] = pd.cut(x = df['horsepower'],
                     bins = bin_label,
                     labels = bin_names,
                     include_lowest = True)

label_encoder = pre.LabelEncoder()
one_hot_encoder = pre.OneHotEncoder()
one_hot_labeled = label_encoder.fit_transform(df['hp_bin'])
# print(one_hot_labeled)

one_hot_reshaped = one_hot_labeled.reshape(len(one_hot_labeled), 1)
one_hot_fitted = one_hot_encoder.fit_transform(one_hot_reshaped)
print(one_hot_fitted)


# In[ ]:


import pandas as pd
import numpy as np
from sklearn import preprocessing as pre

df = pd.read_csv('./dataset/auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']

df.horsepower.replace('?', np.nan, inplace = True)
df.horsepower = df.horsepower.astype('float')
df.dropna(subset = ['horsepower'], axis = 0, inplace = True)

count, bin_label = np.histogram(df.horsepower, bins = 3)
bin_names = ['저출력', '보통출력', '고출력']
df['hp_bin'] = pd.cut(x = df['horsepower'],
                     bins = bin_label,
                     labels = bin_names,
                     include_lowest = True)

df_2 = df.copy()
df_2.horsepower = df_2.horsepower / abs(df_2.horsepower.max())
df_2.horsepower.head()

df_3 = df.copy()
df_3.horsepower = (df_3.horsepower - df_3.horsepower.min()) / (df_3.horsepower.max() - df_3.horsepower.min())
df_3.horsepower.head()


# In[ ]:


import pandas as pd

df = pd.read_csv('./dataset/stock-data.csv')
df['New_Date'] = pd.to_datetime(df['Date'])
df.drop(columns = ['Date'], inplace = True)
df.rename(columns = {'New_Date' : 'Date'}, inplace = True)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day
df.set_index('Date', inplace = True)
df.head()

