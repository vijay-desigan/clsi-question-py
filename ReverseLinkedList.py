# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        l=[]
        temp=head
        if head==None:
            return None
        while(temp.next is not None):
            l.append(temp.val)
            temp=temp.next
        l.append(temp.val)
        
        l.reverse()
        
        temp=head
        i=0
        while(temp.next is not None):
            temp.val=l[i]
            i+=1
            temp=temp.next
        temp.val=l[i]
        
        return head
        
        
