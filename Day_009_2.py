#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd

dict_a = {'a' : 1, 'b' : 2, 'c' : 3}
sr = pd.Series(dict_a)

print(type(dict_a), type(sr))
print(dict_a)
print(sr)
print(sr.index)
print(sr.values)
print(sr[0 : 2])
print(sr['a' : 'c'])


# In[ ]:


import pandas as pd

tup_data = ('영인', '2010-05-06', '여', True)
sr1 = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])

# print(sr1[0], sr1['성별'])
# print(sr1[['이름', '생년월일']])
print(sr1[['이름', '학생여부']], '\n', sr1[[1, 2]])


# In[ ]:


import pandas as pd

dict_data = {'c0' : [1, 2, 3], 'c1' : [4, 5, 6], 'c2' : [7, 8, 9], 'c3' : [10, 11, 12], 'c4' : [13, 14, 15]}
df = pd.DataFrame(dict_data)
print(df)
print(df.index)
print(df.values)


# In[ ]:


import pandas as pd

df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']], index = ['준서', '예은'], columns = ['나이', '성별', '학교'])
print(df)
print()
df.index = ['학생1', '학생2']
print(df)
print()
df.rename(columns = {'나이' : '연령'}, inplace = True)
print(df)
print()
df.drop(['연령', '학교'], axis = 1, inplace = True)
print(df)


# In[ ]:


import pandas as pd

exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
print(df)
print()
df_copy = df.copy()
print(df_copy)
print()
df_copy.drop('우현', axis = 0, inplace = True)
df_copy.drop(['수학', '영어'], axis = 1, inplace = True)
print(df_copy)
print()
print(df[['수학', '영어']])


# In[ ]:


import pandas as pd

exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])

print(df.loc['서준', ['수학', '음악']])
df.loc['서준', '수학'] = 100
print(df)


# In[ ]:


import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'], '수학' : [90, 80, 70], '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data)
df.set_index('이름', inplace = True)
print(df)


# In[ ]:


import pandas as pd

exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95],
             '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

df = pd.DataFrame(exam_data, index=['서준', '우현', '인아'])
df['국어'] = [90, 80, 90]
print(df)
print()
print(df.loc[['서준', '인아'], '국어'])
print()
df.loc['동규'] = [40, 80, 90, 100, 90]
print(df)
print()
df.reset_index(inplace = True)
print(df)
print()


# In[ ]:


import pandas as pd

students = {
    '이름' : [],
    '국어' : [],
    '영어' : [],
    '수학' : []
}

while True :
    name = input('이름을 입력하세요. > ')
    if name == 'q' or name =='ㅂ' :
        print('종료합니다.')
        break
    score = input('국어, 영어, 수학 점수를 띄어쓰기로 구분해 입력하세요. > ').split()
    if len(score) != 3 :
        print('다시 입력하세요.')
        continue
    int_score = [int(score[i]) for i in range(len(score))]
    students['이름'].append(name)
    students['국어'].append(int_score[0])
    students['영어'].append(int_score[1])
    students['수학'].append(int_score[2])

df = pd.DataFrame(students)
df.set_index('이름', inplace = True)
print(df)

