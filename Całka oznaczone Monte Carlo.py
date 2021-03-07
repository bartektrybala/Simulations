#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Monte Carlo obliczanie całki oznaczonej na przedziale (a,b)
import math
import numpy as np
import random

#wzór całki
def f(x):
    return math.exp(-(x**2) * 0.5)

a = 0
b = 1
N = 1000


xrand = [random.uniform(a, b) for i in range(N)]
y = [f(x) for x in xrand]
d = max(y)
yrand = [random.uniform(a, d) for i in range(N)]
p_integral = 0

for i in range(N):
    if yrand[i] <= y[i]:
        p_integral += 1

integral = (p_integral/N) * (b-a) * d
print(integral)

