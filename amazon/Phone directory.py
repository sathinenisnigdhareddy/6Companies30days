#User function Template for python3
temp=[]
class TreeNode:
    def __init__(self):
        self.arr=[None for i in range(26)]
        self.isend=False
def insert(Root,string):
    if(Root==None):
        Root=TreeNode()
    x=Root
    for i in range(0,len(string)):
        if(Root.arr[ord(string[i])-ord('a')]==None):
            Root.arr[ord(string[i])-ord('a')]=TreeNode()
        
        
        Root=Root.arr[ord(string[i])-ord('a')]
    Root.isend=True
    return x
def ContactUtil(str,Root):
    m=str
    global temp
    
    if(Root.isend==True):
        if(m not in temp):
            temp.append(m)
    
    for i in range(0,26):
        if(Root.arr[i]!=None):
           ContactUtil(str+chr(97+i),Root.arr[i])
    
    
  
def contact_fun(str,Root):
    global temp
    x=Root
    m=''
    for i in range(0,len(str)):
        if(Root.arr[ord(str[i])-ord('a')]!=None):
            Root=Root.arr[ord(str[i])-ord('a')]
           
        else:
            return temp
    ContactUtil(str,Root)
    
    
    
    

class Solution:
    def displayContacts(self, n, contact, s):
        # code here
        global temp
        Root=None
        for i in range(0,n):
            Root=insert(Root,contact[i])
        m=''
        list=[]
        for i in range(0,len(s)):
            m+=s[i]
            contact_fun(m,Root)
            if(len(temp)==0):
                list.append([0])
            else:
                list.append(temp)
            temp=[]
        
        temp=[]
        return list
        
            

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        contact = input().split()
        s = input()
        
        ob = Solution()
        ans = ob.displayContacts(n, contact, s)
        for i in range(len(s)):
            for val in ans[i]:
                print(val, end = " ")
            print()
# } Driver Code Ends
