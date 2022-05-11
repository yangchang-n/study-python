#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import seaborn as sns

def add_10(n) :
    return n + 10

def add_two_obj(a, b) :
    return a + b

titanic = sns.load_dataset('titanic')
mask = (titanic.age >= 20) & (titanic.age < 70)
df = titanic.loc[mask, ['age', 'fare']]

# df['age'].apply(add_10).head()
# df['age'].apply(add_two_obj, b = 20)
# df['age'].apply(lambda x : x + 10)
# df.applymap(add_10)
# df.apply(add_10, axis = 0)
# df.apply(lambda x : add_10(x), axis = 0)
# df.apply(lambda x : x.max() - x.min(), axis = 0)

df['m_age'] = df.apply(lambda x : df.age.max() - x.age, axis = 1)
df['m_fare'] = df.apply(lambda x : x.age + x.fare, axis = 1)
print(df.head())


# In[ ]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['age', 'fare']]

def missing_value(x) :
    return x.isnull()

def missing_count(x) :
    return missing_value(x).sum()

def total_number_missing(x) :
    return missing_count(x).sum()

df.pipe(missing_value)
df.pipe(missing_count)
df.pipe(total_number_missing)


# In[ ]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[0 : 4, 'survived' : 'age']
df_sort = df[sorted(df.columns.values)]
df_sort


# In[ ]:


import pandas as pd

df = pd.read_excel('./dataset/주가데이터.xlsx')
df['연월일'] = df['연월일'].astype('str')
dates = df['연월일'].str.split('-')
df['연'] = dates.str.get(0)
df['월'] = dates.str.get(1)
df['일'] = dates.str.get(2)
df.head()


# In[ ]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
mask = (titanic.age < 10) & (titanic.sex == 'female')
df = titanic.loc[mask, ['age', 'class', 'fare', 'sex']]
df.head()


# In[ ]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
mask = ((titanic.age < 10) | (titanic.age >= 60))
df = titanic.loc[mask, ['age', 'pclass', 'fare']]
# df_sib = titanic.loc[(titanic.sibsp == 3) | (titanic.sibsp == 4) | (titanic.sibsp == 5)]
df_sib = titanic.loc[titanic['sibsp'].isin([3, 4, 5]), : ]
df_sur = titanic.loc[titanic['survived'] == 1, : ]
print(len(df_sur))
print(len(titanic))


# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./dataset/남북한발전전력량.xlsx')
df.replace('-', np.nan, inplace = True)
df_1 = df.dropna(axis = 0, thresh = int(round((len(df.columns) / 3 * 2), 0)))
years = list(map(str, range(2010, 2016 + 1)))
df_2 = df_1.loc[[0, 5]]
df_2 = df_2.drop(columns = '발전 전력별')
df_2 = df_2.set_index('전력량 (억㎾h)')
df_2 = df_2.loc[ : , years]
df_2 = df_2.T
plt.figure(figsize = (18, 5))
plt.plot(df_2)
plt.xlabel('연도(년)', size = 12)
plt.ylabel('전력량(억kWh)', size = 12)
plt.title('남북한간 발전 전력량 합계 추이(2010 ~ 2016)', size = 18)
plt.xticks(size = 15)
plt.yticks(size = 15)
plt.legend(labels = ['남한', '북한'], loc = 'best', fontsize = 12)
plt.ylim(0, 8000)
plt.show()

