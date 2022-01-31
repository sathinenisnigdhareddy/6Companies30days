#User function Template for python3
import math
class Solution:
    def colName (self, n):
        # your code here
        ans=''
        b=int(math.log(n,26))
        
        temp=26**b
        a=[]
        
        while(temp>0):
            x=n//temp
            a.append(x)
            n=n%temp
            temp=temp//26
            

           
        if(n>0):
            a.append(n)
       
            
       
        for i in range(len(a)-1,0,-1):
            if(a[i]<=0):
                
                a[i-1]=a[i-1]-1
                a[i]=a[i]+26
        for i in a:
            if(i>0):
                ans=ans+chr(64+i)
        return ans

#{ 
#  Driver Code Starts
#Initial Template for Python 3

t = int (input ())
for tc in range (t):
    n = int (input ())
    ob = Solution()
    print (ob.colName (n))
    

# } Driver Code Ends
