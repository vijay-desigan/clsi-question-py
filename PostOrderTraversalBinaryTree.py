# Given the root of a binary tree, return the postorder traversal of its nodes' values.

 

# Example 1:


# Input: root = [1,null,2,3]
# Output: [3,2,1]
# Example 2:

# Input: root = []
# Output: []
# Example 3:

# Input: root = [1]
# Output: [1]
  
  
import collections
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root is None:
            return []
        # d=collections.deque([root])
        # while(d):
        #     f=d.popleft()
        #     ans.append(f.val)
        #     if f.right is not None:
        #         d.append(f.right)
        #     if f.left is not None:
        #         d.append(f.left)
        # ans.reverse()
        # return ans
        
        s1=collections.deque([root])
        s2=collections.deque([])
        while(s1):
            f=s1.pop()
            s2.append(f)
            
            if f.left is not None:
                s1.append(f.left)
            if f.right is not None:
                s1.append(f.right)
            
        
        while(s2):
            x=s2.pop()
            ans.append(x.val)
        return ans
        
            
        
