#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
lotto_number_list = []
num = random.randrange(1, 46)
for i in range(7) :
    while num in lotto_number_list :
        num = random.randrange(1, 46)
    lotto_number_list.append(num)
print('Lotto number : {}, {}, {}, {}, {}, {}\nBonus number : {}'.      format(lotto_number_list[0], lotto_number_list[1], lotto_number_list[2],             lotto_number_list[3], lotto_number_list[4], lotto_number_list[5], lotto_number_list[6]))

