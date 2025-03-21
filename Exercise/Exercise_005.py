#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# 문자열을 입력 받고 대문자로 변환한다.
input_data = input().upper()      

# 알파벳으로 이루어진 문자열과 26개의 0으로 이루어진 리스트를 만든다.
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
count = [0 for i in range(26)]

for j in input_data :           # 처음에 입력받은 문자열의 각 문자에 대해 순서대로
    index = alphabet.find(j)    # alphabet에서 몇 번째에 위치하는지를 찾아 index 변수에 저장하고
    count[index] += 1           # count 리스트의 index 자리에 1을 더한다. -> 계속 반복한다.

tuple_list = []                                  # 정렬을 위해 빈 리스트를 하나 만들고
for k in range(len(count)) :                     # count 리스트의 길이(알파벳 갯수인 26개)를 범위로 잡아서
    tuple_list.append((alphabet[k], count[k]))   # 만들었던 빈 리스트에 알파벳, 알파벳 갯수 쌍을 순서대로 튜플로 받는다.

# tuple_list를 정렬하는데, 갯수를 기준으로, 내림차순으로 정렬한다.
sorted_list = sorted(tuple_list, key = lambda l : l[1], reverse = True)

# sorted_list는 첫 요소가 가장 많이 쓰인 문자와 그 갯수가 튜플 형식으로 적혀 있으므로,
if sorted_list[0][1] == sorted_list[1][1] :      # 가장 많이 적힌 2개의 문자의 갯수가 같다면
    print('?')                                   # ?를 출력하고
else :                                           # 가장 많이 적힌 문자가 하나밖에 없다면
    print(sorted_list[0][0])                     # 그 문자를 출력한다.

