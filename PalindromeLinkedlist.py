# Given the head of a singly linked list, return true if it is a palindrome.
# Input: head = [1,2,2,1]
# Output: true

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        temp=head
        l=[]
        while(temp.next is not None):
            l.append(temp.val)
            temp=temp.next
        l.append(temp.val)
        
        if l==l[::-1]:
            return True 
        else:
            return False
    
