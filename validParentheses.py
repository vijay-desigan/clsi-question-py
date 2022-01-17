# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

# An input string is valid if:

# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
 

# Example 1:

# Input: s = "()"
# Output: true

# Example 2:

# Input: s = "()[]{}"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        br=0
        sqbr=0
        par=0
        for i in s:
            if i=='(':
                br+=1
            elif i==')':
                br-=1
            elif i=='[':
                sqbr+=1
            elif i==']':
                sqbr-=1
            elif i=='{':
                par+=1
            elif i=='}':
                par-=1
        if br==0 and sqbr==0 and par==0:
            return 'true'
        else:
            return 'false'
        
