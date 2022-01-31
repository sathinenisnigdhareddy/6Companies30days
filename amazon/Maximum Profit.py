#User function Template for python3

class Solution:
    def maxProfit(self, K, N, A):
        # code here
        mat=[[0 for i in range(len(A)+1)] for j in range(K+1)]
     
        for i in range(1,K+1):
            m=-float('inf')
            
            for j in range(1,len(A)+1):
                if(j==1):
                    mat[i][j]=mat[i][j-1]
                else:
                    m=max(mat[i-1][j-1]-A[j-2],m)
                    mat[i][j]=max(m+A[j-1],mat[i][j-1])
                
              
                    
        return mat[-1][-1]

                    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        K = int(input())
        N = int(input())
        A = input().split()
        for i in range(N):
            A[i] = int(A[i])
        
        ob = Solution()
        print(ob.maxProfit(K, N, A))
# } Driver Code Ends
