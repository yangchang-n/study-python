#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

sr = {'국어' : 100, '영어' : 90, '수학' : 80}
sr = pd.Series(sr)

print('Before : {}, After : {}'.format(sr, sr + 10))


# In[ ]:


import pandas as pd

sr1 = pd.Series({'국어' : None, '영어' : 90, '수학' : 80})
sr2 = pd.Series({'국어' : 100, '영어' : 90, '수학' : 80, '과학' : 100})

# print(sr1 + sr2)

sr_add = sr1.add(sr2, fill_value = 0)

print(sr_add)


# In[ ]:


import seaborn as sb

titanic = sb.load_dataset('titanic')
df = titanic.loc[:, ['sex', 'age', 'fare']]
print(df.head())
print(sb.get_dataset_names())


# In[ ]:


import pandas as pd

file_path = './dataset/read_csv_sample.csv'
df = pd.read_csv(file_path, header = None)
print(df)


# In[ ]:


import pandas as pd

file_path = './dataset/남북한발전전력량.xlsx'
df = pd.read_excel(file_path, index_col = 0)
print(df.head())
df.to_excel('./dataset/sample_excel.xlsx')


# In[ ]:


import pandas as pd

file_path = './dataset/read_json_sample.json'
df = pd.read_json(file_path)
print(df)


# In[ ]:


import pandas as pd

file_path = './dataset/sample.html'
df = pd.read_html(file_path)
print(df)
print()
print(df[1])
print()
df[1].set_index('name', inplace = True)
print(df[1])


# In[ ]:


import pandas as pd

data_1 = {
    'name' : ['Jerry', 'Tom', 'Changeun'],
    'aigol' : ['B+', 'A', 'A+'],
    'basic' : ['C+', 'C', 'B+'],
    'c++' : ['B+', 'A-', 'A']
}

data_2 = {
    'c0' : [1, 2, 3],
    'c1' : [1, 2, 3],
    'c2' : [1, 2, 3],
    'c3' : [1, 2, 3]
}

df_1 = pd.DataFrame(data_1)
df_2 = pd.DataFrame(data_2)

df_1.set_index('name', inplace = True)
df_2.set_index('c0', inplace = True)

file_path = './dataset/df_excel.xlsx'
wp = pd.ExcelWriter(file_path)
df_1.to_excel(wp, sheet_name = 'Sheet 1')
df_2.to_excel(wp, sheet_name = 'Sheet 2')
wp.save()

