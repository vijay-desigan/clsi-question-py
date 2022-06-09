# Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if(len(nums))==1:
            if nums[0]==target:
                return [0,0]
            else:
                return [-1,-1]
        left=0
        ans=[-1,-1]
        right=len(nums)-1
        while(left<=right):
            mid=int((left+right)/2)
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                if mid-1>=0 and nums[mid-1]!=target or mid==0:
                    ans[0]=mid
                    break
                right=mid-1
        left=0
        right=len(nums)-1
        while(left<=right):
            mid=int((left+right)/2)
            if nums[mid]<target:
                left=mid+1
            elif nums[mid]>target:
                right=mid-1
            else:
                if  mid==len(nums)-1 or mid+1<=len(nums) and nums[mid+1]!=target:
                    ans[1]=mid
                    break
                left=mid+1
        return ans
                    
