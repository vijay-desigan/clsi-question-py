# Finding middle element in a linked list 
# Given a singly linked list of N nodes.
# The task is to find the middle of the linked list. For example, if the linked list is
# 1-> 2->3->4->5, then the middle node of the list is 3.
# If there are two middle nodes(in case, when N is even), print the second middle element.
# For example, if the linked list given is 1->2->3->4->5->6, then the middle node of the list is 4.

# Example 1:

# Input:
# LinkedList: 1->2->3->4->5
# Output: 3 
# Explanation: 
# Middle of linked list is 3.
# Example 2: 

# Input:
# LinkedList: 2->4->6->7->5->1
# Output: 7 
# Explanation: 
# Middle of linked list is 7.

class Solution:
    #  Should return data of middle node. If linked list is empty, then  -1
    def findMid(self, head):
        # find number of total nodes
        temp=head
        count=1
        while(temp.next is not None):
            count+=1
            temp=temp.next
        
        # find the middle node accordingly
        if count%2==0:
            middle=int(count/2)+1
            pass
        else:
            middle=int((count+1)/2)
        
        # return the node
        temp=head
        for i in range(middle-1):
            temp=temp.next
        return temp.data
