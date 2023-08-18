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
#

import numpy as np
def candies(n, arr):
    start_of_decreasing_sequence = {0:0}
    current_val = 1
    min_sum = 0
    values = []

    for i, elem in enumerate(arr):
        if i == 0:
            continue

        prev_num = arr[i-1]
        if prev_num<elem:
            current_val += 1            

        elif prev_num>elem:
            if current_val == 1:
                min_sum += i-start_of_decreasing_sequence[i-1]
                start_of_decreasing_sequence = start_of_decreasing_sequence[i]
                
            else:
                if current_val == 2:
                    start_of_decreasing_sequence[i] = i 
                current_val = 1   
        values.append(current_val)         
        min_sum += current_val
        
    return min_sum
    # Write your code here

if __name__ == '__main__':
    arr = [1,2,3]
    n = len(arr)
    print(candies(n, arr))