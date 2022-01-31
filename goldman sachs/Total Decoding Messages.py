#User function Template for python3

class Solution:
    def CountWays(self, str):
        # Code here
        m=1000000007
        arr=[0 for i in range(len(str)+1)]
        arr[0]=1
        if(str[0]=='0'):
            return 0
        arr[1]=1
    
        for i in range(1,len(str)):
           
            if(int(str[i-1]+str[i])>0 and int(str[i-1]+str[i])<=26):
                if(str[i]!='0' and str[i-1]!='0'):
                    arr[i+1]=(arr[i]%m +arr[i-1]%m)%m
                elif(str[i]=='0' and str[i-1]!='0'):
                    arr[i+1]=arr[i-1]%m
                elif(str[i]!='0' and str[i-1]=='0'):
                    arr[i+1]=arr[i]%m
            elif(int(str[i-1]+str[i])>26):
                if(str[i]!='0'):
                
                    arr[i+1]=arr[i]%m
                else:
                    return 0
            else:
                return 0
        return arr[-1]

          

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import sys
sys.setrecursionlimit(10**6)
if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        str = input()
        ob = Solution()
        ans = ob.CountWays(str)
        print(ans)

# } Driver Code Ends
