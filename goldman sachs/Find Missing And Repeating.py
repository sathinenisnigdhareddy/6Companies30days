#User function Template for python3

class Solution:
    def findTwoElement( self,arr, n): 
        # code here
        m=(n*(n+1))//2
        s=sum(arr)
        temp=m-s
        for i in range(0,len(arr)):
       
            x=abs(arr[i])
            if(x<=len(arr)):
                if(arr[x-1]>0):
                    arr[x-1]=-arr[x-1]
        
        for i in range(0,len(arr)):
            if(arr[i]>0):
                return ((i+1-temp),i+1)
      
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 

    tc=int(input())
    while tc > 0:
        n=int(input())
        arr=list(map(int, input().strip().split()))
        ob = Solution()
        ans=ob.findTwoElement(arr, n)
        print(str(ans[0])+" "+str(ans[1]))
        tc=tc-1
# } Driver Code Ends
