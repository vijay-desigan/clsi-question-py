# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five
#  integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.
# Example
# arr=[1,3,5,7,9]
# The minimum sum is 1+3+5+7=16  and the maximum sum is 3+5+7+9=24
# The function prints
#     16 24

arr=[1,3,5,7,9]
arr.sort()
min=0
for i in range(4):
    min+=arr[i]
max=0
arr.sort(reverse=True)
for i in range(4):
    max+=+arr[i]
print(min,max)

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr.sort()
    min=0
    for i in range(4):
        min+=arr[i]
    max=0
    arr.sort(reverse=True)
    for i in range(4):
        max+=+arr[i]
    print(min,max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
