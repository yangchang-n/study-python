#!/usr/bin/env python
# coding: utf-8

# In[ ]:


a_list = []
while True :
    input_data = input('수를 입력하세요. > ')
    if input_data == 'q' :
        print('종료합니다.')
        break
    if not input_data.isnumeric() :
        print('다시 입력하세요.')
        continue
    a_list.append(int(input_data))
    a = 0
    b = 1
    c = 0
    d = 0
    for i in range(len(a_list)) :
        a += a_list[i]
        b *= a_list[i]
        c += 1
        d = a / c
    print('입력된 수의 총합 : {}'.format(a))
    print('입력된 수의   곱 : {}'.format(b))
    print('입력된 수의 갯수 : {}'.format(c))
    print('입력된 수의 평균 : {:.2f}'.format(d))

