#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'palindromeIndex' function below.
#
# The function is expected to return an INTEGER.
# The function accepts STRING s as parameter.
#

def fwd_check(fwd_s):
    stk = []
    mistakes = 0
    
    for i, char in enumerate(fwd_s):
        stk.append(char)
    new_s = ""
    
    curr_mistake_idx = -1
    while stk:
        new_s += stk.pop()
        if new_s[-1] != fwd_s[len(new_s)-1]:
            new_s = new_s[:-1]
            mistakes += 1
            curr_mistake_idx=(len(fwd_s)-1-len(new_s)-1)
        
        if mistakes==2:
            return -1, False
        
    return curr_mistake_idx, True
    
def bwd_check(bwd_s):
    stk = []
    mistakes = 0
    
    for i, char in enumerate(bwd_s):
        stk.append(char)
    new_s = ""
    
    curr_mistake_idx = -1
    while stk:
        new_s += stk.pop()
        if new_s[-1] != bwd_s[len(new_s)-1]:
            new_s = new_s[:-1]
            mistakes += 1
            curr_mistake_idx=(len(new_s)-1)
        
        if mistakes==2:
            return -1, False
        
    return curr_mistake_idx, True

def palindromeIndex(s):
    fwd_idx, fwd_val = fwd_check(s)
    bwd_idx, bwd_val = bwd_check(s[::-1])
    
    if fwd_val and bwd_val:
        return fwd_idx
    elif fwd_val:
        return fwd_idx
    elif bwd_val:
        return bwd_idx
    else:
        return -1

if __name__ == "__main__":
    string = 'aaab'
    print(palindromeIndex(s=string))
