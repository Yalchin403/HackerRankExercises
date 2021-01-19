#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumNumber function below.
def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
  count_l = 0
  if n < 6:
    count_l = 6 - n
  req =  {"digit":0, "lowerCase": 0, "upperCase": 0, "special": 0}
  for item in password:
    if item.islower():
      req["lowerCase"] += 1
    elif item.isupper():
      req["upperCase"] += 1
    elif item.isnumeric():
      req["digit"] += 1
    else:
      req["special"] += 1
  count_req = 0
  for item in req:
    if req[item] == 0:
      count_req += 1
  if count_req > count_l:
    return count_req
  return count_l
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    password = input()

    answer = minimumNumber(n, password)

    fptr.write(str(answer) + '\n')

    fptr.close()
