#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the staircase function below.
def staircase(n):
    material = ' ' * n
    for i in range(1, n+1):
        tempVar = material[0:n-i] + "#"*i
        print(tempVar)
if __name__ == '__main__':
    n = int(input())

    staircase(n)
