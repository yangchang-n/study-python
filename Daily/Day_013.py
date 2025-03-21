#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

df1 = pd.DataFrame({'a': ['a0', 'a1', 'a2', 'a3'],
                    'b': ['b0', 'b1', 'b2', 'b3'],
                    'c': ['c0', 'c1', 'c2', 'c3']},
                    index = [0, 1, 2, 3])
 
df2 = pd.DataFrame({'a': ['a2', 'a3', 'a4', 'a5'],
                    'b': ['b2', 'b3', 'b4', 'b5'],
                    'c': ['c2', 'c3', 'c4', 'c5'],
                    'd': ['d2', 'd3', 'd4', 'd5']},
                    index = [2, 3, 4, 5])

# print(pd.concat([df1, df2]))
# print(pd.concat([df1, df2], ignore_index = True))
# print(pd.concat([df1, df2], axis = 1))
# print(pd.concat([df1, df2], axis = 1, join = 'inner'))

sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name = 'e')
sr2 = pd.Series(['f0', 'f1', 'f2'], name = 'f', index = [3, 4, 5])
sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name = 'g')

# print(pd.concat([df1, sr1], axis = 1))
print(pd.concat([df2, sr2], axis = 1))
# print(pd.concat([sr1, sr2, sr3], axis = 1))


# In[ ]:


import pandas as pd

df1 = pd.read_excel('./dataset/stock_price.xlsx')
df2 = pd.read_excel('./dataset/stock_valuation.xlsx')

merge_inner = pd.merge(df1, df2, how = 'inner')
merge_outer = pd.merge(df1, df2, how = 'outer')
merge_inner_on = pd.merge(df1, df2, how = 'inner', on = 'id')
merge_dif_col = pd.merge(df1, df2, how = 'left', left_on = 'stock_name', right_on = 'name')
merge_dif_col


# In[ ]:


import pandas as pd

df1 = pd.read_excel('./dataset/stock_price.xlsx')
df2 = pd.read_excel('./dataset/stock_valuation.xlsx')

merge_inner = pd.merge(df1, df2, how = 'inner')
merge_outer = pd.merge(df1, df2, how = 'outer')

# # 교수님 방법
# # price 가 50000 미만인 자료의 id, name, value, price, eps, bps, per 를 추출
# # 1. df1 에서 price가 50000 미만인 자료의 id, value, price 만 추출
# price = df1.loc[df1['price']<50000,['id','value', 'price']]
# # 2. df1 과 df2 (name-eps-bps-per 만 가져와서) merge
# df_2 = df2.loc[:, ['id','name','eps','bps','per']]
# pd.merge(price, df_2, how='left')

mask = (lambda x : x.price < 50000)
merge_outer[mask][['id', 'stock_name', 'value', 'price', 'eps', 'bps', 'per']]


# In[ ]:


import pandas as pd

df1 = pd.read_excel('./dataset/stock_price.xlsx')
df2 = pd.read_excel('./dataset/stock_valuation.xlsx')
df3 = df1.set_index('id')
df4 = df2.set_index('id')

df5 = df3.join(df4)
df5


# In[ ]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['age', 'sex', 'class', 'fare', 'survived']]
grouped = df.groupby('class')
grouped_2 = df.groupby(['class', 'sex'])

# for key, group in grouped : 
#     print('key :', key)
#     print(group.head())

grouped.mean()
grouped.get_group('First')
grouped['age'].max()

# for key, group in grouped_2 :
#     print('key :', key)
#     print('number :', len(group))
#     print(group.mean())
    
grouped_2.mean()
grouped_2.get_group(('Third', 'male')).head()


# In[ ]:


import pandas as pd
import numpy as np

df = pd.read_csv('./dataset/auto-mpg.csv', header = None)
df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 
              'acceleration', 'model year', 'origin', 'name']
df['origin'].replace({1 : 'USA', 2 : 'EU', 3 : 'JPN'}, inplace = True)
grouped_country = df.groupby('origin')

print(grouped_country['mpg'].mean())
print(grouped_country.get_group('USA')['weight'].min())


# In[ ]:


import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['age', 'sex', 'class', 'fare', 'survived']]
grouped = df.groupby('class')

def min_max(x) :
    return x.max() - x.min()

grouped.agg(['max', 'min'])
grouped.agg({'age' : ['max', 'min'], 'fare' : 'mean'})
df.groupby('sex').agg(['min', 'max', 'sum', 'count'])


# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['age', 'class', 'fare', 'survived']]
grouped = df.groupby('class')

age_mean = grouped.age.mean()
age_std = grouped.age.std()

for key, group in grouped :
    group_score = (group['age'] - age_mean.loc[key]) / age_std.loc[key]
    print('key :', key)
    print(group_score)
    
def group_score(x) :
    return (x - x.mean()) / x.std()

age_score = grouped.age.transform(group_score)

print(age_score.loc[[1, 9, 0]])


# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['class', 'age', 'fare']]
df_fare = df.groupby('class').fare.transform(lambda x : x - x.mean())
df_fare[[1, 9, 0]]


# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['class', 'age', 'fare']]
df_gd = df.groupby('class')
df_rs = df_gd.filter(lambda x : len(x) >= 200)
df_rs['class'].unique()

df_rs_2 = df_gd.filter(lambda x : x.age.mean() < 30)
df_rs_2['class'].unique()

df_gd.apply(lambda x : x.describe())
df_gd.age.apply(lambda x : (x - x.mean()) / x.std())
age_filter = df_gd.apply(lambda x : x.age.mean() < 30)

for key in age_filter.index :
    if age_filter[key] == True :
        age_filter_df = df_gd.get_group(key)


# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['sex', 'age', 'class', 'fare', 'survived']]
df_gd = df.groupby(['class', 'sex'])
gdf = df_gd.mean()
gdf.loc[('First', 'female')]
gdf.xs('female', level = 'sex')


# In[ ]:


import pandas as pd
import numpy as np
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[ : , ['sex', 'age', 'class', 'fare', 'survived']]

pdf = pd.pivot_table(df, index = ['class', 'survived'], columns = 'sex',                     values = ['age', 'fare'], aggfunc = 'mean')

pdf.xs(('First', 1), level = ['class', 'survived'])

