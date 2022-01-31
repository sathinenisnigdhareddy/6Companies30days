# your task is to complete this Function
# Function shouldn't return anything
def skip(ptr,M):
    while(ptr!=None and M>1):
        M-=1
        ptr=ptr.next
    return ptr
def drop(ptr2,N):

    while(ptr2!=None and N>=0):
        ptr2=ptr2.next
        N-=1
    return ptr2
'''
class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None
'''
class Solution:
    def skipMdeleteN(self, head, M, N):
        # Code here
        temp=head
        count=0
        while(temp!=None):
            count+=1
            temp=temp.next
        if(M>count):
            return head
        else:
            temp=head
            while(temp!=None):
                ptr1=skip(temp,M)
                ptr2=drop(ptr1,N)
                if(ptr1!=None):
                    ptr1.next=ptr2
                temp=ptr2
            return head

#{ 
#  Driver Code Starts
#main

class Node:
    # Constructor to initialize the node object
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    # Function to initialize head
    def __init__(self):
        self.head = None

    # Function to insert a new node at the beginning
    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    # Utility function to prit the linked LinkedList
    def printList(self):
        temp = self.head
        while (temp):
            print(temp.data, end=" ") 
            temp = temp.next
        print("")


if __name__=='__main__':
    t = int(input())
    while (t > 0):
        llist = LinkedList()
        n = int(input())
        m,p = list(map(int, input().strip().split()))
        values = input().strip().split()
        for i in reversed(values):
            llist.push(i)
        Solution().skipMdeleteN(llist.head, m, p)
        llist.printList()
        t -= 1
# Contributed by: Harshit Sidhwa
# } Driver Code Ends
