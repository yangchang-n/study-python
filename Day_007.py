#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def fact(n) :
    output = 1
    for i in range(1, n + 1) :
        output *= i
    return output

print(fact(6))


# In[ ]:


def fact_rec(n) :
    if n == 0 :
        return 1
    else :
        return n * fact_rec(n - 1)

print(fact_rec(6))


# In[ ]:


def fibo(n) :
    if n == 1 :
        return 1
    if n == 2 :
        return 1
    return fibo(n - 1) + fibo(n - 2)

print(fibo(20))


# In[ ]:


dictionary = {
    1 : 1,
    2 : 1
}

def fibo_2(n) :
    if n in dictionary :
        return dictionary[n]
    else :
        output = fibo_2(n - 1) + fibo_2(n - 2)
        dictionary[n] = output
        return output

print(fibo_2(50))


# In[ ]:


def power(item) :
    return item * item

def under_3(item) :
    return item < 3

power_1 = lambda n : n * n
under_3_1 = lambda n : n < 3

list_a = [1, 2, 3, 4, 5]

output_a = map(power, list_a)
print(list(output_a))

output_b = filter(under_3, list_a)
print(list(output_b))


# In[ ]:


fp = open('./basic.txt', 'w')
fp.write('Hello, World!')
fp.close()


# In[ ]:


with open('basic.txt', 'a') as fp :
    fp.write('TEST test')


# In[ ]:


with open('basic.txt', 'r') as fp :
    content = fp.read()
    print(content)


# In[ ]:


with open('basic.txt', 'r') as fp :
    fp.seek(0)
    for line in fp.readlines() :
        print(content)


# In[ ]:


file = open('basic.txt', 'r')
text = file.read()
print(text)


# In[ ]:


student = {}

while True :
    input_data = input('이름과 국어, 영어, 수학 점수를 띄어쓰기로 구분하여 입력하세요. > ')
    fp = open('student.txt', 'w')
    fp.write('{}\n'.format(input_data))
    fp.close()

    fp = open('student.txt', 'r')
    text = fp.read().split()

    name = text[0]
    score = text[1:4]

    if text[0] == 'q' or text[0] == 'ㅂ' :
        print('종료합니다.')
        break

    print('이름\t국어\t영어\t수학\t총점\t평균')
    input_score = []
    for value in score :
        input_score.append(int(value))
    student[name] = input_score
    for name in student :
        print('{}\t{}\t{}\t{}\t{}\t{:3.2f}'.format(name, student[name][0], student[name][1], student[name][2],                                                   sum(student[name]), sum(student[name]) / 3))


# In[ ]:


student = {}
fp = open('student.txt', 'w+')

while True :
    name = input('이름을 입력하세요. > ')
    
    if name == 'q' or name == 'ㅂ' :
        print('종료합니다.')
        break
        
    while True :
        score = input('국어, 영어, 수학 점수를 입력하세요. > ').split()
        if len(score) == 3 :
            break
        else :
            print('다시 입력하세요.')
            continue
            
    output = name + ' ' + ' '.join(score) + '\n'
    fp.write(output)
    
    fp.seek(0)
    for line in fp.readlines() :
        line_list = line.strip('\n').split()
        student[line_list[0]] = [int(line_list[i]) for i in range(1, 4)]

    print('이름\t국어\t영어\t수학\t총점\t평균')
    for name in student :
        print('{}\t{}\t{}\t{}\t{}\t{:3.2f}'.format(name, student[name][0], student[name][1], student[name][2],                                                   sum(student[name]), sum(student[name]) / 3))
fp.close()


# In[ ]:


def test() :
    print('test func')
    yield 'test'

print('first')
test()

print('second')
next(test())

print(test())


# In[ ]:


def test() :
    print('A 지점 통과')
    yield 1
    print('B 지점 통과')
    yield 2
    print('C 지점 통과')
    yield 3

func = test()
print('D 지점 통과')
print(next(func))
print('E 지점 통과')
print(next(func))
print(next(func))


# In[ ]:


try :
    input_num = int(input('정수 입력 > '))
    print(input_num * 2)
except :
    print('정수를 입력하세요.')


# In[ ]:


def test() :
    print('func start')
    try :
        print('try 구문 실행')
        return
    except :
        print('except 구문 실행')
    finally :
        print('finally 구문 실행')
    print('func end')

test()


# In[ ]:


student = {}
fp = open('student_2.txt', 'w+')

try :
    print('파일 실행 중...')
    while True :
        name = input('이름을 입력하세요. > ')
        if not name.isalpha() :
            print('다시 입력하세요.')
            continue
        if name == 'q' or name == 'ㅂ' :
            print('종료합니다.')
            break

        while True :
            score = input('국어, 영어, 수학 점수를 입력하세요. > ').split()
            if len(score) == 3 :
                if not score[0].isdigit() or not score[1].isdigit() or not score[2].isdigit() :
                    print('다시 입력하세요.')
                    continue
                break
            else :
                print('다시 입력하세요.')
                continue

        output = name + ' ' + ' '.join(score) + '\n'
        fp.write(output)

        fp.seek(0)
        for line in fp.readlines() :
            line_list = line.strip('\n').split()
            student[line_list[0]] = [int(line_list[i]) for i in range(1, 4)]

        print('이름\t국어\t영어\t수학\t총점\t평균')
        for name in student :
            print('{}\t{}\t{}\t{}\t{}\t{:3.2f}'.format(name, student[name][0], student[name][1], student[name][2],                                                       sum(student[name]), sum(student[name]) / 3))
except :
    print('오류가 발생하였습니다.')
        
fp.close()


# In[ ]:


import math as mt

print(mt.sin(mt.pi / 2))
print(mt.cos(0))
print(mt.floor(4.5))
print(mt.ceil(4.5))


# In[ ]:


from math import sin, cos, floor, pi

print(sin(pi / 2))
