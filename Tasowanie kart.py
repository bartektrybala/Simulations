#!/usr/bin/env python
# coding: utf-8

# In[1]:


#TASOWANIE KART
import random

def tasowanie(talia):
    nowa_talia = []
    for i in range(len(talia)):
        x = random.choice(talia)
        nowa_talia.append(x)
        talia.remove(x)
    return nowa_talia

i = 0
rozw = False
A = [i for i in range(1, 11)] #uporządkowana talia kart, rozmiar talii
while(rozw == False):
    B = A.copy()
    nowa = tasowanie(B)
    if nowa == A:
        print('Ilość prób:', i)
        rozw = True
        print(nowa, A)
    i += 1

