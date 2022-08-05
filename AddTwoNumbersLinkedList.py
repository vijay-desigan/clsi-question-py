# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

# Example 1:


# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Example 2:

# Input: l1 = [0], l2 = [0]
# Output: [0]
# Example 3:

# Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
# Output: [8,9,9,9,0,0,0,1]

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:    
        carry=0
        temp1=l1
        temp2=l2
        ans=[]
        head=ListNode(0)
        temp3=head
        
        while temp1 and temp2:
            s=0
            s=temp1.val+temp2.val+carry
            if s>=10:
                carry=1
                s=s%10
            else:
                carry=0
            t=ListNode(s)
            temp3.next=t
            temp3=temp3.next
            ans.append(s)
            temp1=temp1.next
            temp2=temp2.next
        while temp1:
            # ans.append(temp1.val+carry)
            s=temp1.val+carry
            if s>=10:
                carry=1
                s=s%10
            else:
                carry=0
            ans.append(s)
            t=ListNode(s)
            temp3.next=t
            temp3=temp3.next
            temp1=temp1.next
        while temp2:
            # ans.append(temp2.val)
            s=temp2.val+carry
            if s>=10:
                carry=1
                s=s%10
            else:
                carry=0
            ans.append(s)
            t=ListNode(s)
            temp3.next=t
            temp3=temp3.next
            temp2=temp2.next
        if carry:
            t=ListNode(carry)
            temp3.next=t
            temp3=temp3.next
            
        return head.next
        
#         if temp1.next is not None and temp2.next is not None:
#             while temp1.next is not None and temp2.next is not None:
#                 s+=temp1.val
#                 s+=temp2.val
#                 s=s*10
#             s+=temp1.val
#             s+=temp2.val
#             s=s*10
            
#         elif temp1.next is None and temp2.next is not None:
#             while temp1.next is not None:
#                 s+=temp1.val
#                 s=s*10
#             s+=temp1.val
#             s=s*10
#         elif temp1.next is not None and temp2.next is None:
#             while temp2.next is not None:
#                 s+=temp2.val
#                 s=s*10
#             s+=temp2.val
#             s=s*10
#         return s


        
  
