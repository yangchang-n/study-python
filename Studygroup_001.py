#!/usr/bin/env python
# coding: utf-8

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


students_score = {}
line_list = []
keys_list = []
values_list = []
line_dict = {}
fp = open('input.txt', 'r+')
fp_2 = open('output.txt', 'w+')

fp.seek(0)

for line in fp.readlines() :
    line_list.append(line.strip('\n'))
    
del line_list[0]

for i in range(len(line_list)) :
    if i % 2 == 0 :
        keys_list.append(line_list[i])
    else :
        values_list.append(line_list[i])
        
for i in range(len(keys_list)) :
    line_dict[keys_list[i]] = values_list[i]

for keys, values in line_dict.items() :
    
    number_list = values.strip('\n').split()
    int_number_list = [int(number_list[i]) for i in range(len(number_list))]
    int_number_list.sort()
    mode_numbers = []

    for i in int_number_list :
        mode_numbers.append((i, int_number_list.count(i)))
        
    a = sorted(dict(mode_numbers).items(), key = lambda n : n[1], reverse = True)
    
    print('#{} {}'.format(keys, list(dict(a).keys())[0]))
    fp_2.write('#{} {}\n'.format(keys, list(dict(a).keys())[0]))
    
fp.close()
fp_2.close()

