#!/usr/bin/env python
# coding: utf-8

# In[ ]:


while True:
    input_data = input('계산식을 입력하세요.(\'10 + 20\'의 형태로) > ').split()
    if input_data[0] == 'q' :
        print('종료합니다.')
        break
    else:
        if len(input_data) != 3 :
            print('다시 입력하세요.')
            continue
        num_1 = int(input_data[0])
        num_2 = int(input_data[2])
        code = input_data[1]
        if code in '+-*/':
            if code == '+':
                result = num_1 + num_2
            elif code == '-':
                result = num_1 - num_2
            elif code == '*':
                result = num_1 * num_2
            else:
                result = num_1 / num_2
            print('{} {} {} = {}'.format(num_1, code, num_2, result))
        else:
            print('다시 입력하세요.')
            continue


# In[ ]:


student = {}
fp = open('student.txt', 'w+')

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
            if len(score) != 3 :
                print('다시 입력하세요.')
                continue
            for i in score :
                if not i.isnumeric() :
                    print('다시 입력하세요.')
                    break
            else :
                break

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

    for i in range(100 + 1) :
        mode_numbers.append((i, int_number_list.count(i)))
        
    a = sorted(mode_numbers, key = lambda n : n[1], reverse = True)
    
    print('#{} {}'.format(keys, a[0][0]))
    fp_2.write('#{} {}\n'.format(keys, a[0][0]))

fp.close()
fp_2.close()

