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
I don't think this concept is much useful here, may be much effective
if we were to write fibonacci series with recursion, but I just wanted to
apply...

If you pay attention, I've used simple memoization concept here:
So, basically what I've done is caching each value of n-th factorial in the memory
and return it if it is already in cache, else calculate it with recursion to calculate
each value and save it in the dictionary so that we can use it whenever we need.
"""
if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
