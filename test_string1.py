#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 18:14:42 2021

@author: kimpapaulin
"""



def donuts(count):
    if count < 10 : 
        print("the number of donuts is : " , count)
    else : 
        print("The number of donuts is : many")
    return

M= "je viens "
print(M[:2] + M[-3:])

def both_ends(s):
    b = len(s)
    if b > 2 : 
        print(s[:2] + s[-2:])
    else : 
        print(" ")
    return

s="spring"
both_ends(s)

def fix_start(s):
    if len(s) < 1 : 
        print("il faut que votre caractere soit superieur à 1")
    else : 
        a = s[1:]
        b = a.replace(s[0],"*")
        c=s[0]
        ##b[0] = a[0] 
        print(c+b)
    return

fix_start("babble")


def mix_up(a, b):
    if len (a) < 2 and len(b) < 2 : 
        print("la longeur des caractères ne corresponds pas")
    else : 
         n = a[:2] # recuperation des deux premiere caratere de a
         p = b[:2] # recuperation des deux premiere caractee de b
         ap = a[2:] ## Ici on range le reste des caracteres de a
         bp = b[2:] ## Ici on range le reste des caractères de b 
         an = p + ap ## on met colle les deux premier de a avec le reste de b
         bn = n + bp ## les deux premier de b aveec le reste de a 
         print(an + " " + bn)
    return

mix_up("mix", "pod")
mix_up("dog", "dinner")







