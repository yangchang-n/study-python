#!/usr/bin/env python
# coding: utf-8

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

