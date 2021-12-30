# Given a positive integer k, you need to find the length of the smallest positive integer n such that n is divisible by k, and n only contains the digit 1.

# Return the length of n. If there is no such n, return -1.

# Note: n may not fit in a 64-bit signed integer.

 

# Example 1:

# Input: k = 1
# Output: 1
# Explanation: The smallest answer is n = 1, which has length 1.
# Example 2:

# Input: k = 2
# Output: -1
# Explanation: There is no such positive integer n divisible by 2.

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        if k%2==0:
            return -1
        elif k%5==0:
            return -1
        val=1
        while True:
            if val%k!=0:
                val=val*10+1
            else:
                return len(str(val))
            
                
            
        
