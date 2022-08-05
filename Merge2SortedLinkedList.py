# You are given the heads of two sorted linked lists list1 and list2.

# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

# Return the head of the merged linked list.

 

# Example 1:


# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Example 2:

# Input: list1 = [], list2 = []
# Output: []
# Example 3:

# Input: list1 = [], list2 = [0]
# Output: [0]
  
  
  # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        temp1=list1
        temp2=list2
#         # n=min(list1.val,list2.val)
        head=ListNode(0)
        temp3=head
        
        while temp1 and temp2:
            print(temp1.val,temp2.val)
            if temp1.val>temp2.val:
                t=ListNode(temp2.val)
                temp3.next=t
                temp3=temp3.next
                temp2=temp2.next
            else:
                t=ListNode(temp1.val)
                temp3.next=t
                temp3=temp3.next
                temp1=temp1.next
        while temp1:
            t=ListNode(temp1.val)
            temp3.next=t
            temp3=temp3.next
            temp1=temp1.next
        while temp2:
            t=ListNode(temp2.val)
            temp3.next=t
            temp3=temp3.next
            temp2=temp2.next
        return head.next
            
#         while temp1.next is not None and temp2.next is not None:
#             if temp1.val <=temp2.val:
#                 t=ListNode(temp1.val)
#                 temp3.next=t
#                 temp3=temp3.next
#             if temp2.val <temp1.val:
#                 t=ListNode(temp2.val)
#                 temp3.next=t
#                 temp3=temp3.next
        
        
#         while temp1.next is None and temp2.next is not None:
#             t=ListNode(temp2.val)
#             temp3.next=t
#             temp3=temp3.next


    
            
            
                
            
        
