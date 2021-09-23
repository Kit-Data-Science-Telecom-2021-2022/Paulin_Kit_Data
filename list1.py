#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 19:53:27 2021

@author: kimpapaulin
"""

#!/usr/bin/python -tt
# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# Basic list exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# It's ok if you do not complete all the functions, and there
# are some additional functions to try in list2.py.

# A. match_ends
# Given a list of strings, return the count of the number of
# strings where the string length is 2 or more and the first
# and last chars of the string are the same.
# Note: python does not have a ++ operator, but += works.

def match_ends(words):
    count = 0 
    for i in words : 
        if len(i) >= 2 and i[0] == i[-1] : 
            count += 1 
    print(count)
    return


# B. front_x
# Given a list of strings, return a list with the strings
# in sorted order, except group all the strings that begin with 'x' first.
# e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
# ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
# Hint: this can be done by making 2 lists and sorting each of them
# before combining them.
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



# C. sort_last
# Given a list of non-empty tuples, return a list sorted in increasing
# order by the last element in each tuple.
# e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
# [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
# Hint: use a custom key= function to extract the last element form each tuple.
def sort_last(tuples):
    for m in range (0, len(tuples)):
        for k in range (0, len(tuples)-m-1): 
            if (tuples[k][-1] > tuples[k+1][-1]):
                beta = tuples[k]
                tuples[k]=tuples[k+1]
                tuples[k+1]=beta
    print(tuples)
    return
## si on veut changer l'ordre : on peut utiliser reverse avec true en parametre : 
## Supposnons que l'on veut crier sur le premier element : alors 

def sort_last3(neta):
    for o in range (0, len(neta)):
        for p in range (0, len(neta)-o-1): 
            if (neta[0][p] > neta[0][p+1]):
                z = neta[p]
                neta[p]=neta[p+1]
                neta[p+1]=z
    print(tuples)
    return
## En utilisant la foinction lambda : 

def sort_last2 (gama):
   gama.sort(key = lambda y : y[-1] )
   print(gama)
   return
## si on veut trier avec le premier element .... 
def sort_last2 (teta):
   teta.sort(key = lambda f : f[0] )
   print(teta)
   return

# Simple provided test() function used in main() to print
# what each function returns vs. what it's supposed to return.
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected))


# Calls the above functions with interesting inputs.
def main():
  print 'match_ends'
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print
  print 'front_x'
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print
  print 'sort_last'
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
