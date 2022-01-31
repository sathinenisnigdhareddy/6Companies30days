#User function Template for python3
import collections
from collections import deque
class Solution:
    def FirstNonRepeating(self, A):
        # Code here
        dict={}
        q=deque([A[0]])
        ans=A[0]
        dict[A[0]]=1
        for i in range(1,len(A)):
            if(dict.get(A[i])==None):
                dict[A[i]]=1
                q.append(A[i])
            else:
                dict[A[i]]+=1
                while(len(q)>0 and dict[q[0]]>1):
                    q.popleft()
            if(len(q)==0):
                ans=ans+'#'
            else:
                ans=ans+q[0]
        return ans
        

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T=int(input())
    for i in range(T):
        A = input()
        ob = Solution()
        ans = ob.FirstNonRepeating(A)
        print(ans)

# } Driver Code Ends
