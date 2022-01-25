# # Given an array of integers arr, return true if and only if it is a valid mountain array.

# # Recall that arr is a mountain array if and only if:

# # arr.length >= 3
# # There exists some i with 0 < i < arr.length - 1 such that:
# # arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
# # arr[i] > arr[i + 1] > ... > arr[arr.length - 1

# Example 1:

# Input: arr = [2,1]
# Output: false
  
# Example 2:

# Input: arr = [3,5,5]
# Output: false
  
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true

class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        peak=arr.index(max(arr))
        mountup=False
        mountdown=False
        for i in range(1,len(arr)):
            if i<=peak and arr[i]>arr[i-1]:
                mountup=True
            elif i>peak and arr[i]<arr[i-1]:
                mountdown=True
            else:
                return False
                break 
        if mountup and mountdown:
            return True
        else:
            return False
        
