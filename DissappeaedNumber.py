# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of all the integers in the range [1, n] that do not appear in nums.

# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

# Example 2:

# Input: nums = [1,1]
# Output: [2]

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        maxval=len(nums)
        val=1
        op=[]
        while val<=maxval:
            if nums.count(val)==0:
                op.append(val)
            val+=1
        return op
    
        
