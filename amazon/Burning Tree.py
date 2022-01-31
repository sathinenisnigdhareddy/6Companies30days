#User function Template for python3
import collections
G={}
def bfs(G,target):
    q=collections.deque([target])
    q.append('*')
    visited={}
    count=0
    while(len(q)>0):
        x=q.popleft()
        if(x=='*'):
            if(len(q)>0 and q[-1]!='*'):
                q.append('*')
                count+=1
        if(x!='*'):
            visited[x]='t'
            for i in G[x]:
                if(visited.get(i)==None):
                    q.append(i)
    return count
                    
    
def fun(root):
    global G
    if(root==None):
        return 
    else:
        if(root.left!=None and G.get(root.left)==None):
            G[root.left.data]=[root.data]
        elif(root.left!=None and G.get(root.left.data)!=None):
            G[root.left.data].append(root.data)
        if(root.right!=None and G.get(root.right.data)==None):
            G[root.right.data]=[root.data]
        elif(root.right!=None and G.get(root.right.data)!=None):
            G[root.right.data].append(root.data)
        if(root.left!=None and root.right!=None):
            if(G.get(root.data)==None):
                
                G[root.data]=[root.left.data,root.right.data]
            else:
                G[root.data].append(root.left.data)
                G[root.data].append(root.right.data)
                

                
            
        elif(root.left!=None and root.right==None):
            if(G.get(root.data)==None):
                G[root.data]=[root.left.data]
            else:
                G[root.data].append(root.left.data)
        elif(root.left==None and root.right!=None):
            if(G.get(root.data)==None):
                G[root.data]=[root.right.data]
            else:
                G[root.data].append(root.right.data)
            
            
            
            

    fun(root.left)
    fun(root.right)
    
class Solution:
    def minTime(self, root,target):
        # code here
        global G
        if(root.left==None and root.right==None):
            return 0
        fun(root)
     
        
        x=bfs(G,target)
        G={}
        return x
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

from collections import deque

# Tree Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None

# Function to Build Tree   
def buildTree(s):
    #Corner Case
    if(len(s)==0 or s[0]=="N"):           
        return None
        
    # Creating list of strings from input 
    # string after spliting by space
    ip=list(map(str,s.split()))
    
    # Create the root of the tree
    root=Node(int(ip[0]))                     
    size=0
    q=deque()
    
    # Push the root to the queue
    q.append(root)                            
    size=size+1 
    
    # Starting from the second element
    i=1                                       
    while(size>0 and i<len(ip)):
        # Get and remove the front of the queue
        currNode=q[0]
        q.popleft()
        size=size-1
        
        # Get the current node's value from the string
        currVal=ip[i]
        
        # If the left child is not null
        if(currVal!="N"):
            
            # Create the left child for the current node
            currNode.left=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.left)
            size=size+1
        # For the right child
        i=i+1
        if(i>=len(ip)):
            break
        currVal=ip[i]
        
        # If the right child is not null
        if(currVal!="N"):
            
            # Create the right child for the current node
            currNode.right=Node(int(currVal))
            
            # Push it to the queue
            q.append(currNode.right)
            size=size+1
        i=i+1
    return root

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        line=input()
        target=int(input())
        root=buildTree(line)
        print(Solution().minTime(root,target))

# } Driver Code Ends
