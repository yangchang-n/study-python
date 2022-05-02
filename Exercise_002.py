#!/usr/bin/env python
# coding: utf-8

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

