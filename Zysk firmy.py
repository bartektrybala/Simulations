#!/usr/bin/env python
# coding: utf-8

# In[1]:


#Przybliżanie zysku firmy za następny rok
import math
import random
import numpy as np

A = []
for i in range(10000):
    ni = [random.uniform(1000, 2000) for i in range(12)]
    k = random.uniform(2, 3)
    c = random.uniform(5, 10)
    Ks = 50000

    cni = [i*c for i in ni]
    kni = [i*k for i in ni]


    TR = sum(cni)
    TC = sum(kni) + Ks
    z = TR - TC
    A.append(z)

E = sum(A)/len(A)
E

