# Given two sorted linked lists consisting of N and M nodes respectively. The task is to merge both of the list (in-place) and return head of the merged list.

# Example 1:

# Input:
# N = 4, M = 3 
# valueN[] = {5,10,15,40}
# valueM[] = {2,3,20}
# Output: 2 3 5 10 15 20 40
# Explanation: After merging the two linked
# lists, we have merged list as 2, 3, 5,
# 10, 15, 20, 40.


#User function Template for python3
'''
    Function to merge two sorted lists in one
    using constant space.
    
    Function Arguments: head_a and head_b (head reference of both the sorted lists)
    Return Type: head of the obtained list after merger.

    {
        # Node Class
        class Node:
            def __init__(self, data):   # data -> value stored in node
                self.data = data
                self.next = None
    }

'''
#Function to merge two sorted linked list.
def sortedMerge(head1, head2):
    # code here
    lst=[]
    temp=head1
    n=1
    while(temp.next is not None):
        lst.append(temp.data)
        n+=1
        temp=temp.next
    temp.next=head2
    while(temp.next is not None):
        n+=1
        lst.append(temp.data)
        temp=temp.next
    lst.append(temp.data)
    # print(lst)
    temp2=head1
    lst.sort()
    i=0
    while(temp2.next is not None):
        temp2.data=lst[i]
        i+=1
        temp2=temp2.next
    temp2.data=lst[-1]
    return head1
        

        


#{ 
#  Driver Code Starts
#Initial Template for Python 3
# Node Class
class Node:
    def __init__(self, data):   # data -> value stored in node
        self.data = data
        self.next = None

# Linked List Class
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # creates a new node with given value and appends it at the end of the linked list
    def append(self, new_value):
        new_node = Node(new_value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node    
            return
        self.tail.next = new_node
        self.tail = new_node
        
# prints the elements of linked list
def printList(n):
    while n is not None:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m = map(int, input().strip().split())
        
        a = LinkedList() # create a new linked list 'a'.
        b = LinkedList() # create a new linked list 'b'.
        
        nodes_a = list(map(int, input().strip().split()))
        nodes_b = list(map(int, input().strip().split()))
        
        for x in nodes_a:
            a.append(x)
        
        for x in nodes_b:
            b.append(x)
        
        printList(sortedMerge(a.head,b.head))

# } Driver Code Ends
