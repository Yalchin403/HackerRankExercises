#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    hr = int(s[0]) * 10 + int(s[1])
    length = len(s)
    if s[8:length + 1] == "PM" and s[0:2] == "12":
        return "12" + s[2:8]
    elif s[8:length + 1] == "PM":
        hr = hr + 12
        return str(hr) + s[2:8]
    
    elif s[8:length + 1] == "AM" and s[0:2] == "12":
        return "00" + s[2:8]
    else:
        return s[0:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
