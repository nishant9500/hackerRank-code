#!/bin/python3

import math
import os
import random
import re
import sys

def gameOfThrones(s):
    m=0
    for x in set(s):
        m=m+(s.count(x)%2)
    if m<2:
        return "YES"
    else:
        return "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = gameOfThrones(s)

    fptr.write(result + '\n')

    fptr.close()
