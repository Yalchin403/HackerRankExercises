#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the superDigit function below.
def superDigit(n, k):
    sum = 0
    if len(n) == 1:
      sum = int(n)
      return sum
    else:
        for i in n:
            sum = sum + int(i)

        n = sum * int(k)
        sum = 0
        while(True):
            sum = sum + n % 10  # 17
            n = n // 10 # 0

            if n == 0:
                if len(str(sum)) != 1:
                    n = sum
                    sum = 0
                else:
                    return sum
  
  
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = nk[0]

    k = int(nk[1])

    result = superDigit(n, k)

    fptr.write(str(result) + '\n')

    fptr.close()
