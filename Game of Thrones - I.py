#!/bin/python3

import math
import os
import random
import re
import sys
Dothraki are planning an attack to usurp King Robert's throne. King Robert learns of this conspiracy from Raven and plans to lock the single door through which the enemy can enter his kingdom.

# door

# But, to lock the door he needs a key that is an anagram of a palindrome. He starts to go through his box of strings, checking to see if they can be rearranged into a palindrome.

# For example, given the string
# , one way it can be arranged into a palindrome is

# .

# Function Description

# Complete the gameOfThrones function below to determine whether a given string can be rearranged into a palindrome. If it is possible, return YES, otherwise return NO.

# gameOfThrones has the following parameter(s):

#     s: a string to analyze

# Input Format

# A single line which contains

# , the input string.

# Constraints

# |s| contains only lowercase letters in the range

# Output Format

# A single line which contains YES or NO.


# Complete the gameOfThrones function below.
def gameOfThrones(s):
    s2={}
    n=s
    j=1
    m=0
    c=[1]*len(s)
    for i in range(len(s)-1):
        j=0
        while j<len(s):
            if j==i:
                j=j+1
            if(n[i]==n[j]):
                c[i]=c[i]+1
                j=j+1
            else: 
                j=j+1
    
    for i in range(len(c)):
        if c[i]%2==0:
            m=m+1
        elif c[i]>2 and c[i]%2==1:
            m=m+1
    if m==len(c) or m==len(c)-1:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
