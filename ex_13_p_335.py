#-*- coding: utf8 -*-
import random

nb_series = 150
nb_lancers = 30
for series in range(nb_series):
    succes = 0
    for lancer in range(nb_lancers):
        if random.randint(1, 2) == 1:
            succes = succes + 1
    print(succes)
