#User function Template for python3
class Solution:
    def getNthUglyNo(self,n):
        # code here
        arr=[1]
        ptr1=0
        ptr2=0
        ptr3=0
        for i in range(2,n+1):
            a=arr[ptr1]*2
            b=arr[ptr2]*3
            c=arr[ptr3]*5
            res=min(a,b,c)
            arr.append(res)
            if(res==a):
                ptr1+=1
            if(res==b):
                ptr2+=1
            if(res==c):
                ptr3+=1
        
        return arr[-1]
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        ob = Solution()
        ans = ob.getNthUglyNo(n);
        print(ans)
        tc -= 1

# } Driver Code Ends
