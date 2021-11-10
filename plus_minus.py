# Given an array of integers, calculate the ratios of its elements that are positive, negative, and zero. Print the decimal value of
# each fraction on a new line with 6 places after the decimal.
# Note: This challenge introduces precision problems. The test cases are scaled to six decimal places, though answers with
# absolute error of up to 10^-4  are acceptable.
# Example
# arr=[1,1,0,-1,-1]
# There are n=5 elements, two positive, two negative and one zero. Their ratios are 2/5 ,2/5 and 1/5.Results are printed as:
# 0.400000
# 0.400000
# 0.200000


#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

#actual logic 
# |||||||
# VVVVVVV
def plusMinus(arr):
    # Write your code here
    zero=0
    posetive=0
    negative=0
    total=len(arr)
    for i in arr:
        if i==0:
            zero+=1
        elif i<0:
            negative+=1
        elif i>0:
            posetive+=1
    print(round(posetive/total,6))
    print(round(negative/total,6))
    print(round(zero/total,6))
    
    
if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
