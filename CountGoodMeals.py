# A good meal is a meal that contains exactly two different food items with a sum of deliciousness equal to a power of two.

# You can pick any two different foods to make a good meal.

# Given an array of integers deliciousness where deliciousness[i] is the deliciousness of the i th item of food, return the number of different good meals you can make from this list modulo 109 + 7.
#
# Note that items with different indices are considered different even if they have the same deliciousness value
# Input: deliciousness = [1,3,5,7,9]
# Output: 4
# Explanation: The good meals are (1,3), (1,7), (3,5) and, (7,9).
# Their respective sums are 4, 8, 8, and 16, all of which are powers of 2.

import math
def log(value):
    val=1
    if value==1:
        return True
    while val<=value:
        power=2**val
        if power==value:
            return True 
        if power>value:
            break
        if power<value:
            val+=1
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        goodMeal=0
        for i in range(len(deliciousness)):
            for j in range(i+1,len(deliciousness)):
                sum=deliciousness[i]+deliciousness[j]
                if log(sum):
                    goodMeal+=1
        return goodMeal
                    
        

