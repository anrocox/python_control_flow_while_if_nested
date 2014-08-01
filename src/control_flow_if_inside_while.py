#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 23, 2014

@author: anroco

In Python, How to define control structures if inside while loop?

En Python, ¿Cómo definir estructuras de control if dentro de un ciclo while?
'''

#create a integer
n = 0

#iterates whilst the value of n is less than 5
while n < 5:

    #checks if the remainder of the division by two is equal to 0
    if n % 2 == 0:
        print(str(n) + ' is an even number')
    else:
        print(str(n) + ' is an odd number')

    #adds 1 to value n
    n += 1
