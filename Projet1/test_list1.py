#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:59:32 2021

@author: kimpapaulin
"""

def match_ends(words):
    count = 0 
    for i in words : 
        if len(i) >= 2 and i[0] == i[-1] : 
            count += 1 
    print(count)
    return

def front_x(words):
    L1 = []
    L2 = []
    for i in words : 
        if i [0] == 'x' : 
            L1.append(i)
        else : 
            L2.append(i)
    L1.sort()
    L2.sort()
    L3 = L1 + L2
    print(L3)
    return

b = ['mix', 'xyz', 'apple', 'xanadu', 'aardvark']

front_x(b)

tuples = [(1, 7), (1, 3), (3, 4, 1), (2, 2)]

def sort_last(tuples):
    for m in range (0, len(tuples)):
        for k in range (0, len(tuples)-m-1): 
            if (tuples[k][-1] > tuples[k+1][-1]):
                beta = tuples[k]
                tuples[k]=tuples[k+1]
                tuples[k+1]=beta
    print(tuples)
    return

sort_last(tuples)

c= [(1, 7), (1, 3), (3, 4, 1), (2, 2)]

c.sort(key = lambda y : y[1] )
print(c)
            
            
    
   


    
   
    
    
## hotel : Novetel aeroport charle de gaule 