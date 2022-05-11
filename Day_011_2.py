#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname = './dataset/malgun.ttf').get_name()
rc('font', family = font_name)

df = pd.read_excel('./dataset/시도별 전출입 인구수.xlsx')

df = df.fillna(method = 'ffill')
mask_seoul = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask_seoul]
df_seoul = df_seoul.drop(['전출지별'], axis = 1)
df_seoul.rename({'전입지별' : '전입지'}, axis = 1, inplace = True)
df_seoul.set_index('전입지', inplace = True)
sr_one = df_seoul.loc['경기도']

plt.figure(figsize = (14, 5))
plt.plot(sr_one.index, sr_one.values, color = 'red', marker = 'o', markerfacecolor = 'violet')
plt.xlabel('연도(년)', size = 12)
plt.ylabel('인구수(명)', size = 12)
plt.title('서울 -> 경기도 인구 이동', size = 15)
plt.xticks(rotation = 65)
plt.yticks(size = 12)
plt.legend(labels = ['인구 이동량 추이'], loc = 'best', fontsize = 12)
plt.ylim(0, 800000)
plt.annotate('',
             xy=(20, 620000),       #화살표의 머리 부분(끝점)
             xytext=(2, 290000),    #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='skyblue', lw=5), #화살표 서식
             )

plt.annotate('',
             xy=(47, 450000),       #화살표의 머리 부분(끝점)
             xytext=(30, 630000),   #화살표의 꼬리 부분(시작점)
             xycoords='data',       #좌표체계
             arrowprops=dict(arrowstyle='->', color='olive', lw=5),  #화살표 서식
             )

# 주석 표시 - 텍스트
plt.annotate('인구이동 증가(1970-1995)',  #텍스트 입력
             xy=(10, 420000),            #텍스트 위치 기준점
             rotation=22,                #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )

plt.annotate('인구이동 감소(1995-2017)',  #텍스트 입력
             xy=(38, 560000),            #텍스트 위치 기준점
             rotation=-12,               #텍스트 회전각도
             va='baseline',              #텍스트 상하 정렬
             ha='center',                #텍스트 좌우 정렬
             fontsize=15,                #텍스트 크기
             )
plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname = './dataset/malgun.ttf').get_name()
rc('font', family = font_name)

df = pd.read_excel('./dataset/시도별 전출입 인구수.xlsx')

df = df.fillna(method = 'ffill')
mask_seoul = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask_seoul]
df_seoul = df_seoul.drop(['전출지별'], axis = 1)
df_seoul.rename({'전입지별' : '전입지'}, axis = 1, inplace = True)
df_seoul.set_index('전입지', inplace = True)
sr_one = df_seoul.loc['경기도']

fig = plt.figure(figsize = (14, 10))
ax1 = fig.add_subplot(2, 1, 1)
ax2 = fig.add_subplot(2, 1, 2)

ax1.plot(sr_one, marker = 'o')
ax2.plot(sr_one, marker = '*', label = '서울 -> 경기')
ax2.legend(loc = 'best')
ax1.set_ylim(0, 800000)
ax2.set_ylim(0, 800000)
ax1.set_xticks(sr_one.index)
ax2.set_xticks(sr_one.index)
ax1.set_title('1번')
ax2.set_title('2번')

plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname = './dataset/malgun.ttf').get_name()
rc('font', family = font_name)

df = pd.read_excel('./dataset/시도별 전출입 인구수.xlsx')

df = df.fillna(method = 'ffill')
mask_seoul = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask_seoul]
df_seoul = df_seoul.drop(['전출지별'], axis = 1)
df_seoul.rename({'전입지별' : '전입지'}, axis = 1, inplace = True)
df_seoul.set_index('전입지', inplace = True)

col_years = list(map(str, range(1970, 2000 + 1)))
df_seoul_2 = df_seoul.loc[['충청남도', '경상북도', '강원도'], col_years]

fig_2 = plt.figure(figsize = (18, 5))

ax = fig_2.add_subplot(1, 1, 1)
ax.plot(col_years, df_seoul_2.loc['충청남도', : ], label = '서울 -> 충남')
ax.plot(col_years, df_seoul_2.loc['경상북도', : ], label = '서울 -> 경북')
ax.plot(col_years, df_seoul_2.loc['강원도', : ], label = '서울 -> 강원')
ax.legend(loc = 'best')

ax.set_title('서울 -> 충남, 경북, 강원 인구 이동', size = 15)
ax.set_xlabel('연도(년)', size = 12)
ax.set_ylabel('인구수(명)', size = 12)
ax.set_xticks(col_years)
ax.set_ylim(0, 70000)
ax.tick_params(axis = 'x', rotation = 45)

plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname = './dataset/malgun.ttf').get_name()
rc('font', family = font_name)

df = pd.read_excel('./dataset/시도별 전출입 인구수.xlsx')

df = df.fillna(method = 'ffill')
mask_seoul = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask_seoul]
df_seoul = df_seoul.drop(['전출지별'], axis = 1)
df_seoul.rename({'전입지별' : '전입지'}, axis = 1, inplace = True)
df_seoul.set_index('전입지', inplace = True)

col_years = list(map(str, range(1970, 2000 + 1)))
df_seoul_2 = df_seoul.loc[['충청남도', '경상북도', '강원도'], col_years]
df_seoul_3 = df_seoul_2.T
df_seoul_3.index = df_seoul_3.index.map(int)
df_seoul_3.plot(kind = 'area', figsize = (18, 5), stacked = False, alpha = 0.1)

plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import font_manager, rc

font_name = font_manager.FontProperties(fname = './dataset/malgun.ttf').get_name()
plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

df = pd.read_excel('./dataset/남북한발전전력량.xlsx')
df_ns = df.loc[5 : , : ]
df_ns.columns[0]
df_ns = df_ns.drop('전력량 (억㎾h)', axis = 1)
df_ns.set_index(df_ns.columns[0], inplace = True)
df_ns = df_ns.T
df_ns.rename(columns = {'합계' : '총발전량'}, inplace = True)
df_ns['이전년도 총발전량'] = df_ns['총발전량'].shift(1)
df_ns['전년대비 총발전량 증감율'] = ((df_ns['총발전량'] / df_ns['이전년도 총발전량']) - 1) * 100
df_ns_2 = df_ns[['수력', '화력']]

ax1 = df_ns_2.plot(kind = 'bar', figsize = (18, 5), stacked = True)
ax2 = ax1.twinx()
ax2.plot(df_ns.index, df_ns['전년대비 총발전량 증감율'], ls = '--', marker = 'o', markersize = 8,         color = 'red', label = '전년대비 총발전량 증감율(%)')
ax1.set_ylim(0, 350)
ax2.set_ylim(-40, 40)
ax1.set_xlabel('연도(년)', size = 12)
ax1.set_ylabel('발전량(억kWh)', size = 12)
ax2.set_ylabel('증감율(%)', size = 12)
plt.title('북한 전력 발전량 (1990 ~ 2016)', size = 20)
ax1.legend(loc = 'best')

plt.show()


# In[ ]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.family'] = 'Malgun Gothic'
plt.rcParams['axes.unicode_minus'] = False

titanic = sns.load_dataset('titanic')
fig = plt.figure(figsize = (15, 5))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)
ax1.set_title('reg line - True')
ax2.set_title('reg line - False')

sns.regplot(x = 'age', y = 'fare', data = titanic, ax = ax1, color = 'violet')
sns.regplot(x = 'age', y = 'fare', data = titanic, ax = ax2, fit_reg = False)

plt.show()


# In[ ]:


import folium

seoul_map = folium.Map(location = [37.55, 126.98], zoom_start = 12)

seoul_map.save('./dataset/seoul.html')


# In[ ]:


import pandas as pd
import folium

df = pd.read_excel('./dataset/서울지역 대학교 위치.xlsx', engine = 'openpyxl')

df.set_index(df.columns[0], inplace = True)

seoul_map = folium.Map(location = [37.55, 126.98], tiles = 'Stamen Terrain', 
                        zoom_start = 12)

for name, lat, lng in zip(df.index, df.위도, df.경도):
    folium.Marker([lat, lng], popup = name).add_to(seoul_map)

seoul_map.save('./dataset/seoul_colleges.html')

