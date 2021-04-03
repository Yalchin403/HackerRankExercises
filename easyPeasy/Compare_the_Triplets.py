#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the compareTriplets function below.
def compareTriplets(a, b):
    aliceScore = 0
    BobScore = 0
    for i in range(len(a)):
        if a[i] > b[i]:
            aliceScore += 1
        elif a[i] < b[i]:
            BobScore += 1
        else:
            continue
    returnArray = [aliceScore, BobScore]
    return returnArray

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
