#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the miniMaxSum function below.
def miniMaxSum(arr):
    # find minimums
    copy = list()
    for i in arr:
        copy.append(i)
    fourMins = list()
    fourMaxs = list()
    for i in range(0, 4):
        mini = min(copy)
        fourMins.append(mini)
        copy.remove(mini)
    # find maximums
    copy = arr
    for i in range(0, 4):
        maxi = max(copy)
        fourMaxs.append(maxi)
        copy.remove(maxi)
    result1 = sum(fourMins)
    result2 = sum(fourMaxs)
    print(f"{result1} {result2}")

if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
