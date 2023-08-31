#!/bin/python3

import math
import os
import random
import re
import sys


def fwd_check(fwd_s):
    mistakes = 0    
    curr_mistake_idx = -1
    i, j = 0, len(fwd_s)-1
    while i<j:
        if i==j and mistakes<2:
            return curr_mistake_idx, True
        elif fwd_s[i]==fwd_s[j]:
            i+=1
            j-=1
        elif fwd_s[i]!=fwd_s[j] and mistakes<2:
            curr_mistake_idx = i
            mistakes+=1
            i+=1
        else:
            return -1, False

    return curr_mistake_idx, True
    
def bwd_check(fwd_s):
    mistakes = 0    
    curr_mistake_idx = -1
    i, j = 0, len(fwd_s)-1
    while i<j:
        if i==j and mistakes<2:
            return curr_mistake_idx, True
        elif fwd_s[i]==fwd_s[j]:
            i+=1
            j-=1
        elif fwd_s[i]!=fwd_s[j] and mistakes<2:
            curr_mistake_idx = j
            mistakes+=1
            j-=1
        else:
            return -1, False

    return curr_mistake_idx, True

def palindromeIndex(s):
    if s == s[::-1]:
        return -1

    fwd_idx, fwd_val = fwd_check(s)
    print(s)
    bwd_idx, bwd_val = bwd_check(s)
    print(s)
    
    print(fwd_idx, fwd_val)
    print(bwd_idx, bwd_val)
    if fwd_val and bwd_val:
        return fwd_idx
    elif fwd_val:
        return fwd_idx
    elif bwd_val:
        return bwd_idx
    else:
        return -1

if __name__ == "__main__":
    string = 'hjfiwwiwfjh'
    print(palindromeIndex(s=string))
