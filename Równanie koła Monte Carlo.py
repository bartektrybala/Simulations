#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Monte Carlo Pi za pomocą równania koła
import random
import numpy as np

N = 10000
r = 2
Pk = 0
for i in range(N):
    x = random.uniform(-r, r)
    y = random.uniform(-r, r)
    if x**2 + y**2 <= r**2:
        Pk += 1
        
print('π:', np.pi)
print('Monte Carlo pi:', Pk/N*4)

