# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

# Return true if there is a cycle in the linked list. Otherwise, return false.

 

# Example 1:


# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).
# Example 2:


# Input: head = [1,2], pos = 0
# Output: true
# Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.
# Example 3:


# Input: head = [1], pos = -1
# Output: false
# Explanation: There is no cycle in the linked list.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        turtle=head
        hare=head
        
        while turtle and hare and hare.next:
            hare=hare.next.next
            turtle=turtle.next
            if turtle==hare:
                return True
        return False
#         l=[]
#         temp=head
#         if temp is None or temp.next is None:
#             return False
        
#         while temp:
#             if temp.val=="done":
#                 return True
#             else:
#                 temp.val="done"
#             temp=temp.next
            
#         return False
        
        
        
        
