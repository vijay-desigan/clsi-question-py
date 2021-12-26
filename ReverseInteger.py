# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
# Example 1:
# Input: x = 123
# Output: 321
# Example 2:
# Input: x = -123
# Output: -321
# Example 3:
# Input: x = 120
# Output: 21

class Solution:
    def reverse(self, x: int) -> int:
        reversednum=0
        temp=x
        negative=False
        if x<0:
            temp=-1*x
            negative=True
        while temp>0:
            reversednum=reversednum*10+temp%10
            temp=int(temp/10)
        if negative:
            reversednum=-1*reversednum
        if reversednum<(-1*pow(2,31)) or reversednum>(pow(2,31)-1) :
            return 0
        else :
            return reversednum
