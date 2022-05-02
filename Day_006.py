#!/usr/bin/env python
# coding: utf-8

# In[ ]:


dict_a = {
    'name' : '7D 건조 망고',
    'type' : '당절임',
    'ingredient' : ['망고', '설탕', '메타중아황산나트륨', '치자황색소'],
    'origin' : '필리핀'
}
print(dict_a)
print(dict_a['name'])
print(dict_a['ingredient'][2])
print()
print(dict_a.keys())
print(dict_a.values())
print(dict_a['name'], dict_a['type'], sep = ', ')
print()
dict_a['price'] = 5000
print(dict_a)
del dict_a['price']
print(dict_a)
print()
print('type' in dict_a)
print(dict_a.get('type'))
print()
for key in dict_a :
    print('dict_a[\'{}\'] : {}'.format(key, dict_a[key]))
print()
for key, value in dict_a.items() :
    print('dict_a[\'{}\'] : {}'.format(key, value))


# In[ ]:


# example 1
student = {}
number = 0
total = 0
average = 0
while True :
    input_data = input('이름과 점수를 띄어쓰기로 구분해 입력하세요. > ').split()
    if input_data[0] == 'q' or input_data[0] == 'ㅂ' :
        print('종료합니다.')
        break
    student[input_data[0]] = int(input_data[1])
    for key, value in student.items() :
        print('이름 : {}\t점수 : {}'.format(key, value))
    number += 1
    total += int(input_data[1])
    average = total / number
    print('총 학생 수 : {}\t평균 : {:3.2f}'.format(number, average))  


# In[ ]:


# example 2
student = {}
while True :
    name = input('이름을 입력하세요. > ')
    if name == 'q' or name == 'ㅂ' :
        print('종료합니다.')
        break
    input_score = input('국어, 영어, 수학 점수를 띄어쓰기로 구분하여 입력하세요. > ').split()
    if input_score[0] == 'q' or input_score[0] == 'ㅂ' :
        print('종료합니다.')
        break
    if len(input_score) != 3 :
        print('다시 입력하세요. > ')
        continue
    print('이름\t국어\t영어\t수학\t총점\t평균')
    score = []
    for value in input_score :
        score.append(int(value))
    student[name] = score
    for name in student :
        print('{}\t{}\t{}\t{}\t{}\t{:3.2f}'.format(name, student[name][0], student[name][1], student[name][2],                                                   sum(student[name]), sum(student[name]) / 3))


# In[ ]:


# example 3
numbers = [1, 2, 3, 4, 2, 3, 1, 4, 5, 2, 3, 1, 2, 3]
counter = {}
for number in numbers :
    if number in counter.keys() :
        counter[number] += 1
    else :
        counter[number] = 1
for key in counter :
    print('{}은 {}개'.format(key, counter[key]))


# In[ ]:


list_a = [3, 2, 4, 5, 6, 7]
for item in list_a :
    print(item, end=' ')
print()
for i in range(len(list_a)) :
    print(list_a[i], end=' ')
print()
for i in reversed(range(len(list_a))) :
    print(list_a[i], end=' ')
print()
list_a.sort()
print(list_a)
list_a.sort(reverse = True)
print(list_a)
list_a.reverse()
print(list_a)


# In[ ]:


import time
count = 0
target_time = time.time() + 3
while time.time() < target_time :
    count += 1
print('3초동안 {}번 실행함'.format(count))


# In[ ]:


two_numbers = input('두 수를 입력하세요. > ').split()
a = 0
b = 0
for i in range(int(two_numbers[0]), int(two_numbers[1]) + 1) :
    if i % 3 == 0 :
        a += i
    if i % 5 == 0 :
        b += i
print(a, b)


# In[ ]:


list_b = [4, 5, 6, 7, 8, 9]
for num in list_b :
    print(num, end = ' ')
print()
for num in range(len(list_b)) :
    print(num, list_b[num], end = ' / ')
print()
for num, value in enumerate(list_b) :
    print(num, value, end = ' / ')


# In[ ]:


list_c = []
for num in range(2, 20 + 1, 2) :
    list_c.append(num * num)
print(list_c)

list_d = [num * num for num in range(2, 20 + 1, 2)]
print(list_d)


# In[ ]:


print(sum([i for i in range(1, 100 + 1) if i % 3 == 0]))

list_e = []
for i in range(1, 100 + 1) :
    if i % 3 == 0 :
        list_e.append(i)
print(sum(list_e))


# In[ ]:


list_d = [str(num * num) for num in range(2, 20 + 1, 2)]
print(list_d)
str_a = ' '.join(list_d)
print(str_a)
list_f = str_a.split(' ')
print(list_f)


# In[ ]:


def print_n_times(text, n_times) :
    for i in range(n_times) :
        print(text)
    
print_n_times('Hello', 2)


# In[ ]:


def print_val_times(n, *values) :
    for i in range(n) :
        for value in values :
            print(value, end = ' ')
        print()
        
print_val_times(2, 'Hello', 'World')


# In[ ]:


def compute_func(num1, num2 = 100) :
    return num1 + num2

print(compute_func(10, 30))
print(compute_func(20))


# In[ ]:


def input_func() :
    while True :
        input_data = input('계산식을 입력하세요.(\'10 + 20\'의 형태로) > ').split()
        if input_data[0]== 'q' :
            return ([input_data[0]], None)
        num_list = [int(data) for data in input_data if data.isdigit()]  # 10 + 20
        if input_data[1] in '+-*/' :
            return (num_list, input_data[1])

def plus_func(a, b) :
    return a + b
def minus_func(a, b) :
    return a - b
def mul_func(a, b) :
    return a * b
def div_func(a, b) :
    return a / b

while True :
    num_list, code = input_func()
    if num_list[0] == 'q' or num_list[0] == 'ㅂ' :
        print('종료합니다.')
        break
    num1 = num_list[0]
    num2 = num_list[1]
    if code == '+' :
        result = plus_func(num1, num2)
    elif code == '-' :
        result = minus_func(num1, num2)
    elif code == '*' :
        result = mul_func(num1, num2)
    else :
        result = div_func(num1, num2)

    print('{} {} {} = {}'.format(num1, code, num2, result))

