#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the anagram function below.
def anagram(s):
    d=0
    l=len(s)
    if l%2!=0:
        return -1
    else:
        d=sum((Counter(s[:l//2]) - Counter(s[l//2:])).values())
        return d
    #print(sum((Counter(s[:l//2]) - Counter(s[l//2:])).values()))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = anagram(s)

        fptr.write(str(result) + '\n')

    fptr.close()
