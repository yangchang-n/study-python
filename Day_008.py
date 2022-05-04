#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import datetime as dt

print('현재시각 출력 :', dt.datetime.now())


# In[ ]:


from urllib import request

target = request.urlopen('https://google.com')
print(target.read())


# In[ ]:


from bs4 import BeautifulSoup

html_doc = """<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.title)
# print(soup.title.name)
# print(soup.title.parent)
# print(soup.title.string)
# print()
# print(soup.p)
# print(soup.p['class'])
# print()
# print(soup.find_all('p'))
# print()
# print(soup.find(id = 'link2'))
# print()
for link in soup.find_all('a') :
    print(link.get('href'))
    
tag = BeautifulSoup('<b id="boldest">bold</b>', 'html.parser').b
print(tag['id'])
print(tag.attrs)


# In[ ]:


from urllib import request
from bs4 import BeautifulSoup

url = 'https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220503'
target = request.urlopen(url)
soup = BeautifulSoup(target.read(), 'html.parser')

movie_title = []
movie_point = []

for line in soup.find_all('tr') :
    title = line.find('div', class_ = 'tit5')
    if title :
        movie_title.append(title.get_text().strip('\n'))
    point = line.find('td', class_ = 'point')
    if point :
        movie_point.append(point.get_text())
        
for i, (title, point) in enumerate(zip(movie_title, movie_point)) :
    print(i + 1, ' : ', title, point)


# In[ ]:


import requests

text = '''Uh, summa-lumma, dooma-lumma, you assumin' I'm a human
What I gotta do to get it through to you I'm superhuman?
Innovative and I'm made of rubber so that anything
You say is ricochetin' off of me, and it'll glue to you and
I'm devastating, more than ever demonstrating
How to give a motherfuckin' audience a feeling like it's levitating
Never fading, and I know the haters are forever waiting
For the day that they can say I fell off, they'll be celebrating'''

url = 'https://openapi.naver.com/v1/papago/n2mt'
headers = {'X-Naver-Client-Id' : '5rDbjvMAzcjRHypwwQIn',
          'X-Naver-Client-Secret' : 'cHxTHT7HGx'}
params = {'source' : 'en', 'target' : 'ko', 'text' : text}
response = requests.post(url, headers = headers, data = params)
result = response.json()
target = result['message']['result']['translatedText']
print(target)


# In[ ]:


class Student :
    def __init__(self, name, kor, math) :
        self.name = name
        self.kor = kor
        self.math = math
    def get_sum(self) :
        return self.kor + self.math

student_1 = Student('홍길동', 90, 80)
print(student_1.name)
print('{} : {}, {} / 총점 : {}'.format(student_1.name, student_1.kor, student_1.math, student_1.get_sum()))


# In[ ]:


# class를 활용한 교수님 코드

class Student :
    def __init__(self, name, kor, eng, math) :
        self.name = name
        self.kor = kor
        self.eng = eng
        self.math = math
    def get_sum(self) :
        return self.kor + self.eng + self.math
    def get_avr(self) :
        return self.get_sum() / 3

def input_data() :
    name = input('이름 입력 > ')
    while name != 'q' :
        score = input('국어, 영어, 수학 점수 입력 > ').split()
        students.append(Student(name, int(score[0]), int(score[1]), int(score[2])))
        name = input('이름 입력 > ')    
        
students = [] 
input_data()
    
score_tot = [[], [], []]
for student in students :
    print(student.name, student.kor, student.eng, student.math, student.get_sum(), student.get_avr())
    score_tot[0].append(student.kor)
    score_tot[1].append(student.eng)
    score_tot[2].append(student.math)

