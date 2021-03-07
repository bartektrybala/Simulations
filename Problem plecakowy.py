#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Monte Carlo, problem plecakowy przybliżenie liczby rozwiązań
import random
import numpy as np

N = 30
B = 4
I = 100000

wi = [np.random.normal(0, 1) for i in range(N)]

for i in range(len(wi)):
    if wi[i] < 0:
        wi[i] = -wi[i]

A = []
for j in range(I):
    Sum = 0
    x = [random.choice([0, 1]) for i in range(N)]
    for i in range(N):
        Sum += wi[i] * x[i]
    if(Sum <= B):
        A.append(Sum)
        
prop = len(x)/I
print(prop)
prop*2**N

