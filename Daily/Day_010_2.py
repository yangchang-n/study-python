#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np

arr = np.arange(15)
print(arr, arr.ndim, arr.shape)
print()
arr_2 = arr.reshape(3, 5)
print(arr_2, arr_2.ndim, arr_2.shape)
print()
print(arr_2.dtype.name, arr_2.dtype.itemsize, arr_2.size)


# In[ ]:


import numpy as np

a = np.arange(-5, 5, 0.5)
print(a.size)
arr_3 = a.reshape(int(a.size / 4), 4)
print(arr_3)


# In[ ]:


import numpy as np

b = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(b)

list_a = list(range(1, 100 + 1))
arr_4 = np.array(list_a).reshape(5, 4, 5)
print(arr_4)


# In[ ]:


import numpy as np

print(np.zeros(5))
print()
print(np.zeros((2, 3, 5)))
print()
print(np.zeros((5, 2), dtype = 'i'))
print()
print(np.zeros(5, dtype = 'U4'))
print()
print(np.zeros(5, dtype = 'i8'))
print()
print(np.zeros(5, dtype = 'f'))
print()
print(np.ones(5, dtype = 'f'))
print()
print(np.ones_like(np.zeros((5, 2), dtype = 'i'), dtype = 'f'))


# In[ ]:


import numpy as np

print(np.empty((4, 3)))


# In[ ]:


import numpy as np

x1 = np.array([1.0, 2.0, 3.0])
y1 = np.array([5.0, 10.0, 15.0])
x2 = np.array([[1.0, 2.0], [3.0, 4.0]]) 
y2 = np.array([[5.0, 10.0], [15.0, 20.0]]) 
z1 = np.array([-1.0, -2.0])
z2 = np.array([[5.0], [10.0], [15.0]])

print(x1 + y1)
print(x2 + y2)
print(x2 * y2)
print(x2 + z1)
print(x1 ** 5)
print(x1 >= 2)


# In[ ]:


import numpy as np

x1 = np.array([1.0, 2.0, 3.0])
y1 = np.array([5.0, 10.0, 15.0])
x2 = np.array([[1.0, 2.0], [3.0, 4.0]]) 
y2 = np.array([[5.0, 10.0], [15.0, 20.0]]) 
z1 = np.array([-1.0, -2.0])
z2 = np.array([[5.0], [10.0], [15.0]])

print(x2.ndim, x2)
print(x2.flatten())


# In[ ]:


import numpy as np

arr_5 = np.arange(10) ** 2

print(arr_5)
print(arr_5[2])
print(arr_5[3 : 7])
print(arr_5[0 : -1 : 2])
print(arr_5[ : : -1])

for data in arr_5 :
    print(data)


# In[ ]:


import numpy as np

arr_6 = np.arange(1, 20 + 1, 1).reshape(5, 4)

print(arr_6)
print()
print(arr_6[1, 1], arr_6[3, 2])
print()
print(arr_6[[1, 3], [1, 2]])
print()
print(arr_6[1 : 3, : ])
print()
print(arr_6[ : , -1])
print()
print(arr_6[[1, 3], : ][ : ,[1, 2]])


# In[ ]:


import numpy as np

arr_6 = np.arange(1, 20 + 1, 1).reshape(5, 4)

arr_6[1, : ] = -arr_6[1, : ]
print(arr_6)
print()
print(arr_6[ : : -1, : : -1])


# In[ ]:


import numpy as np

arr_6 = np.arange(1, 20 + 1, 1).reshape(5, 4)

print(np.sin(arr_6))
print()
print(np.log(np.arange(0.01, 1, 0.05)))


# In[ ]:


import numpy as np

a1 = np.array([1, 5, 3])
a2 = np.array([3, 4, 5])

print(np.maximum(a1, a2))
print(np.minimum(a1, a2))
print(np.sum(a1))
print(np.argmax(a1))
print(np.argmin(a2))


# In[ ]:


import numpy as np

print(np.random.choice(100, 5))
print(np.random.rand(2, 3))


# In[ ]:


import numpy as np

iq = float(np.random.randn(1) * 20 + 100)
print('당신의 IQ는 {:3.2f}입니다.'.format(iq))


# In[ ]:


import numpy as np

a = np.array([[0.1, 0.8, 0.2], [0.3, 0.2, 0.5], [0.9, 0.5, 0.3]])
print(np.argmax(a, axis = 0))


# In[ ]:


import numpy as np

x = np.array([18,   5,  10,  23,  19,  -8,  10,   0,   0,   5,   2,  15,   8,
              2,   5,   4,  15,  -1,   4,  -7, -24,   7,   9,  -6,  23, -13])
print(len(x), np.mean(x))
print(np.median(x), np.var(x), np.std(x), np.max(x), np.min(x))
print(np.percentile(x, 25), np.percentile(x, 50), np.percentile(x, 75), np.percentile(x, 100))


# In[ ]:


import numpy as np

print(np.random.choice(6, 10, p = [0.5, 0.1, 0.1, 0.1, 0.1, 0.1]))


# In[ ]:


import numpy as np

int_list = np.random.randint(1, 10 + 1, size = (2, 5))
print(int_list)


# In[ ]:


import numpy as np

x = np.arange(1, 20 + 1)
a = []
b = []
c = []
for i in x :
    if i % 3 == 0 :
        a.append(i)
    if i % 4 == 1 :
        b.append(i)
    if i % 3 == 0 and i % 4 == 1 :
        c.append(i)
        
print(a)
print(b)
print(c)


# In[ ]:


import numpy as np

x = np.arange(1, 20 + 1)
print(x[x % 3 == 0])
print(x[x % 4 == 1])
print(x[(x % 3 == 0) & (x % 4 == 1)])

