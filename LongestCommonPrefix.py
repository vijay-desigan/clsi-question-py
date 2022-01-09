# Write a function to find the longest common prefix string amongst an array of strings.
# 
# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"

# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        i=0
        prefix=''
        count=0
        run=True
        minlen=len((min(strs,key=len)))
        for i in range(minlen):
            count=0
            val=strs[0][i]
            for word in strs:
                if word[i]==val:
                    count+=1
                else:
                    run=False
                    break
            if count==len(strs):
                prefix=prefix+val
            if not run:
                break
        return prefix
