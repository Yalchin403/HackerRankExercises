#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superReducedString function below.
def superReducedString(s):
    cache = list()
    for letter in s:
        if cache and letter == cache[-1]:
            cache.pop()
        else:
            cache.append(letter)
    new = ''.join(cache)
    if len(new) == 0:
        return "Empty String"
    return new

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = superReducedString(s)

    fptr.write(result + '\n')

    fptr.close()
