#User function Template for python3

class Solution:
    def findPosition(self, N , M , K):
        # code here
        if(M>N):
            M=M%N
        if(K+M-1<=N):
            return K+M-1
        else:
            return (K+M-1)%N
        


#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,M,K=map(int,input().split())
        
        ob = Solution()
        print(ob.findPosition(N,M,K))
# } Driver Code Ends
