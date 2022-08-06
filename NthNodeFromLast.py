# Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

# Example 1:


# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Example 2:

# Input: head = [1], n = 1
# Output: []
# Example 3:

# Input: head = [1,2], n = 1
# Output: [1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        l=0
        temp=head
        
        if temp is None :
            return head
            
        while temp:
            l+=1
            temp=temp.next
            
        t=l-n
        temp=head
        
        if n==l:
            return head.next
        
        for i in range(t):
            if i==t-1:
                p=temp
            temp=temp.next
            
        if p.next.next:
            p.next=p.next.next
        else:
            p.next=None
        return head
        
