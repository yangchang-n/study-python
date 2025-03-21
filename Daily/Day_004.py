#!/usr/bin/env python
# coding: utf-8

# In[ ]:


print("test")


# In[ ]:


import keyword
print(keyword.kwlist)


# In[ ]:


print(10, 20, 30, 'print test')


# In[ ]:


a = 10 + 20


# # python code
# python

# In[ ]:


a = 10 + 20
a

b = 10 + 10
b


# In[ ]:


a = 10 + 20
print(a)


# # test
# test

# In[ ]:


a = 10 + 20
print('a =', a)


# # asdf

# In[ ]:


# 하나만 출력합니다.
print("# 하나만 출력합니다.")
print("Hello Python Programming...!")
print()

# 여러 개를 출력합니다.
print("# 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "양창은입니다!")
print()

# 아무것도 입력하지 않으면 단순하게 줄바꿈합니다.
print("# 아무것도 출력하지 않습니다.")
print("--- 확인 전용선 ---")
print()
print()
print("--- 확인 전용선 ---")


# In[ ]:


print(type('test'), type(12), type(True), type(35.0), sep='\t', end='\n\n')
print(type('test'), type(12), type(True), type(35.0), sep=', ')
print("\"Hello\"")


# In[ ]:


print("이름\t나이\t지역")
print("양창은\t25\t노원구")


# In[ ]:


print('''동해물과 백두산이 마르고 닳도록
하느님이 보우하사 우리나라 만세
무궁화 삼천리 화려강산
대한사람 대한으로 길이 보전하세''')


# In[ ]:


print('test ' * 3)


# In[ ]:


a = '안녕하세요'
print(a[0])
print(a[-3])


# In[ ]:


a = '안녕하세요'
print(a[0:2])
print(a[2:])
print(a[:3])
print(a[:-1])
print(len(a))
print(a[2:len(a)-1])
print(type(a))


# In[ ]:


print(5 / 2)
print(5 // 2)
print(5 % 2)
print(5 ** 2)
a = 10; b = 3
print(a // b)


# In[ ]:


a = 10
b = 3
a = 11
a + b


# In[ ]:


a = 10
a += 10
a


# In[ ]:


input_data = input("Press any button and press enter > ")
print('input_data =', input_data)


# In[ ]:


print('Adding 100 program')
print('It adds 100 when you input any integer and press enter button.')
input_data_2 = input('Input any number > ')
input_data_2 = int(input_data_2)
input_data_2 + 100


# In[ ]:


print('Adding program')
print('This program adds two numbers you input.')
inputdata1 = input('Input your first number > ')
inputdata2 = input('Input your second number > ')
inputdata1 = int(inputdata1)
inputdata2 = int(inputdata2)
inputdata1 + inputdata2


# In[ ]:


print('Adding program')
print('This program adds two numbers you input.')
inputdata1 = input('Input your first number > ')
inputdata2 = input('Input your second number > ')
inputdata1 = int(inputdata1)
inputdata2 = int(inputdata2)
print("{} + {} = {}".format(inputdata1, inputdata2, inputdata1 + inputdata2))


# In[ ]:


output_a = '{:d}'.format(52)
output_b = '{:5d}'.format(52)
output_c = '{:10d}'.format(52)
output_d = '{:05d}'.format(52)
output_e = '{:010d}'.format(-52)
print(output_a)
print(output_b)
print(output_c)
print(output_d)
print(output_e)


# In[ ]:


a = 'abced'
print(a.upper())
input_str = input('영문자 입력 > ')
print('소문자 출력 : {}'.format(input_str.lower()))
print('대문자 출력 : {}'.format(input_str.upper()))

