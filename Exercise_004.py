#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import test_package.module_a as a
import test_package.module_b as b

print(a.var_a, b.var_b)


# In[ ]:


from test_package import module_a, module_b

print(module_a.var_a)


# In[ ]:


from test_package import *

print(module_a.var_a)

