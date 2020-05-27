#-*- coding: utf8 -*-
import random
import math

def echant():
    succes = 0
    for simu in range(400):
        if random.randint(1, 4)==1:
            succes = succes + 1
    return succes/400
cpt = 0
for series in range(100):
    if abs(0.25-echant())<1/math.sqrt(400):
        cpt = cpt + 1
freq = cpt/100
print(freq)
