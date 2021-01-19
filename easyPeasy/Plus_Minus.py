#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the plusMinus function below.
def plusMinus(arr):
    n = len(arr)
    negatives = positives = zeros = 0
    for num in arr:
        if num < 0:
            negatives += 1
        elif num > 0:
            positives += 1
        else:
            zeros += 1
            
    results = (round(positives/n,6), round(negatives/n, 6), round(zeros/n, 6))
    for result in results:
        print(result)
        
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
