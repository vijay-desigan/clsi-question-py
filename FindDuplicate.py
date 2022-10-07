# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

# There is only one repeated number in nums, return this repeated number.

# You must solve the problem without modifying the array nums and uses only constant extra space.

 

# Example 1:

# Input: nums = [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: nums = [3,1,3,4,2]
# Output: 3

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # m={}
        # for i in nums:
        #     if i not in m:
        #         m[i]=0
        #     m[i]+=1
        # print(m)
        # for i in m:
        #     if m[i]>1:
        #         return i 
        
        slow=nums[0]
        fast=nums[0]
        
        slow=nums[slow]
        fast=nums[nums[fast]]

        
        
        while fast!=slow:
            # print(slow,fast)
            slow=nums[slow]
            fast=nums[nums[fast]]
            
        start=nums[0]
        # start2=fast
        while start!=fast:
            # print(slow,fast)
            start=nums[start]
            fast=nums[fast]
        return start
            
        
        
        
        
        
        
        
        
        
        
        
