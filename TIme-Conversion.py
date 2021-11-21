# Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
# Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
# - 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
# Example
# s='12:01:00PM'
#   Return '12:01:00'.
# s='12:01:00AM'
#   Return '00:01:00'
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    in_12=s
    if in_12[8]=='P':
        hr=int(in_12[0])*10+int(in_12[1])
        if hr==12:
            hr=12
        else:
            hr=hr+12
        s2=str(hr)
    elif in_12[8]=='A':
        hr=int(in_12[0])*10+int(in_12[1])
        if 0<=hr<=9:
                hr='0'+str(hr)
        if hr==12:
            hr='00'
        s2=str(hr)
    for i in range(2,8):
        s2=s2+in_12[i]
    return s2

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
int(s2)


