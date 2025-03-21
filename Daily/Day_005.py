#!/usr/bin/env python
# coding: utf-8

# In[ ]:


input_data1 = input('문자 입력 > ')
print('입력받은 문자 : {}\n소문자로 변경 : {}\n대문자로 변경 : {}'.      format(input_data1, input_data1.lower(), input_data1.upper()))


# In[ ]:


a_str = '       test ASDF asdf    '
print("strip\t: /{}/\nrstrip\t: /{}/\nlstrip\t: /{}/".format(a_str.strip(), a_str.rstrip(), a_str.lstrip()))


# In[ ]:


b_str = 'test1234asdf'
print(b_str.isalnum())
print(b_str[:4].isalpha())


# In[ ]:


c_str = '양창은의 창은 길고 날카롭다.'
print(c_str.find('창은'))
print(c_str.rfind('창은'))
print(c_str[c_str.find('창은') - 1 : c_str.rfind('창은') + 1])
print('창은' in c_str)
print('창진' in c_str)


# In[ ]:


d_str = '10 20 30 40 50'
print('{}\n{}'.format(d_str, d_str.split()))


# In[ ]:


e_str = '10 test 30 40 50'
e_list = e_str.split()
print('test' in e_list)
print(e_str.split()[1])


# In[ ]:


import random
lotto_number_list = []
num = random.randrange(1, 46)
for i in range(7) :
    while num in lotto_number_list :
        num = random.randrange(1, 46)
    lotto_number_list.append(num)
print('Lotto number : {}, {}, {}, {}, {}, {}\nBonus number : {}'.      format(lotto_number_list[0], lotto_number_list[1], lotto_number_list[2],             lotto_number_list[3], lotto_number_list[4], lotto_number_list[5], lotto_number_list[6]))


# In[ ]:


f_str = input('Input any integer > ')
f_int = int(f_str)
if f_int < 100 :
    print('100보다 작음')
else :
    print('100보다 같거나 큼')


# In[ ]:


import datetime
now = datetime.datetime.now()

print('{}년 {}월 {}일 {}시 {}분 {}초'.format(now.year, now.month, now.day, now.hour, now.minute, now.second))

if 3 <= now.month and 5 >= now.month :
    print('이번 달은 {}월로 봄입니다.'.format(now.month))
elif 6 <= now.month and 8 >= now.month :
    print('이번 달은 {}월로 여름입니다.'.format(now.month))
elif 9 <= now.month and 11 >= now.month :
    print('이번 달은 {}월로 가을입니다.'.format(now.month))
else :
    print('이번 달은 {}월로 겨울입니다.'.format(now.month))

if now.hour < 12 :
    print('현재 시각은 {}시로 오전입니다.'.format(now.hour))
else :
    print('현재 시각은 {}시로 오후입니다.'.format(now.hour))


# In[ ]:


g_int = int(input('Input any integer > '))
if g_int % 2 == 0 :
    print('입력된 숫자 {}는 짝수'.format(g_int))
else :
    print('입력된 숫자 {}는 홀수'.format(g_int))


# In[ ]:


h_str = input('Input any word or number > ')
if not h_str.isalpha() :
    h_float = float(h_str)
    if h_float % 3 == 0:
        print('입력한 숫자 {}는 3의 배수입니다.'.format(h_float))
    else :
        print('입력한 숫자 {}는 3의 배수가 아닙니다.'.format(h_float))
else :
    if 't' in h_str :
        print('입력한 단어에 t가 포함되어 있습니다.'.format(h_str))
    else :
        print('입력한 단어에 t가 포함되어 있지 않습니다.'.format(h_str))


# In[ ]:


num_1 = float(input('First number > '))
i_str = input('Arithmetic code > ')
num_2 = float(input('Second number > '))

if i_str in '+-*/' :
    if i_str == '+' :
        result = num_1 + num_2
        print('Result : {}'.format(result))
    elif i_str == '-' :
        result = num_1 - num_2
        print('Result : {}'.format(result))
    elif i_str == '*' :
        result = num_1 * num_2
        print('Result : {}'.format(result))
    else :
        result = num_1 / num_2
        print('Result : {}'.format(result))
else :
    print('Error')


# In[ ]:


j_list = [23, 'test', 'abcd', True, 45]
print(j_list)
print(j_list[1])
print(j_list[2][:2])
j_list[0] = 35
print(j_list)
j_list.append('list')
print(j_list)


# In[ ]:


k_list = [15, [22, 35, 46], 57, 162]
print(k_list[1])
print(k_list[1][1])


# In[ ]:


# 계산기
# q 입력하면 종료

while True :
    
    l_data = input('계산식 입력 (10 + 20 의 형식, 띄어쓰기를 포함할 것) > ').split()
    
    if l_data[0] == 'q' :
        break
    if len(l_data) != 3 :
        continue
    if not l_data[0].isnumeric() or not l_data[2].isnumeric() :
        continue

    num_1 = float(l_data[0])
    i_str = l_data[1]
    num_2 = float(l_data[2])

    if i_str in '+-*/' :
        if i_str == '+' :
            result = num_1 + num_2
            print('Result : {}'.format(result))
        elif i_str == '-' :
            result = num_1 - num_2
            print('Result : {}'.format(result))
        elif i_str == '*' :
            result = num_1 * num_2
            print('Result : {}'.format(result))
        else :
            result = num_1 / num_2
            print('Result : {}'.format(result))
    else :
        print('Error')
        
print('Done')


# In[ ]:


# 구구단
num_1 = 1
while num_1 < 10 :
    num_2 = 2
    while num_2 < 10 :
        print('{:1d} * {:1d} = {:2d}'.format(num_2, num_1, num_1 * num_2), end = '\t')
        num_2 += 1
    print()
    num_1 += 1


# In[ ]:


while True :
    m_data = input('등차수열의 합 계산기, 초항과 끝항을 입력하세요. > ').split()
    if m_data[0] == 'q' :
        break
    if len(m_data) != 2 or not m_data[0].isnumeric() or not m_data[1].isnumeric() or m_data[0] == m_data[1] :
        print('띄어쓰기를 포함한 다른 두 수를 입력하세요.')
        continue
    num_1 = int(m_data[0])
    num_2 = int(m_data[1])
    if num_1 > num_2 :
        num_k = num_1
        num_1 = num_2
        num_2 = num_k
    a = num_1 + num_2
    b = num_2 - num_1
    c = a * (b + 1) / 2
    print('초항이 {}이고 끝항이 {}인 등차수열의 합은 {}입니다.'.format(num_1, num_2, c))
    continue


# In[ ]:


n_list = [1, 2, 3]
n_list.append(4)
print(n_list)
n_list.insert(1, 'test')
print(n_list)
n_list.append([4, 5, 6])
print(n_list)
n_list.extend([4, 5, 6])
print(n_list)
del n_list[1]
print(n_list)
n_list.pop(0)
print(n_list)
n_list.remove(4)
print(n_list)
n_list.clear()
print(n_list)


# In[ ]:


o_list = [1, 2, 3, 4]
print(5 in o_list)


# In[ ]:


for i in range(5) :
    print('apple', i)


# In[ ]:


p_list = [1, 2, 3, 7, 8, 9]
for i in p_list :
    print(i)
for char in 'Hello, World!!' :
    print(char, end = '~')


# In[ ]:


q_list = [100, 239, 574, 12, 49]
for i in range(len(q_list)) :
    print(q_list[i], end = ' ')

