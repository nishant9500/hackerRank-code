#!/bin/python3

import math
import os
import random
import re
import sys

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
