#!/bin/python3
import math
import os
import random
import re
import sys

#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr

import numpy as np
def candies(n, arr):
    values = [1 for _ in range(n)]
    for i, elem in enumerate(arr):
        if i>0 and i<len(arr)-1:
            if arr[i-1] > elem:
                values[i] = max(values[i-1]+1, values[i])
    
    for i in range(n-2,-1,-1):
        if arr[i] > arr[i+1]:
                values[i] = max(values[i+1]+1, values[i])

    return sum(values)
if __name__ == '__main__':
    arr = [4,6,4,5,6,2]
    n = len(arr)
    print(candies(n, arr))