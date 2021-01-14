#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the extraLongFactorials function below.
def extraLongFactorials(n):
    print(main(n))


factorial_cache = {}
def main(n):
  if n in factorial_cache:
    return factorial_cache[n]
  
  if n == 1:
    value = 1
  else:
    value = n * main(n-1)
  
  factorial_cache[n] = value
  return value


"""
If you pay attention, I've used simple memoization concept here:
So, basically what I've done is caching each value of n-th factorial in the memory
and return it if it is already in cache, else calculate it with recursion to calculate
each value and save it in the dictionary so that we can use it whenever we need.
"""
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
