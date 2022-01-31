#User function Template for python3
import collections
class Solution:
    
    #Function to find maximum of each subarray of size k.
    def max_of_subarrays(self,arr,n,k):
        
        #code here
        ans=[]
        q=collections.deque([0])
        for i in range(1,k):
            if(len(q)>0 and arr[q[-1]]>arr[i]):
                q.append(i)
            elif(len(q)>0 and arr[q[-1]]<=arr[i]):
                while(len(q)>0 and arr[q[-1]]<=arr[i]):
                    q.pop()
                q.append(i)
        ans.append(arr[q[0]])
        for i in range(k,len(arr)):
            while(len(q)>0 and q[0]<i-k+1):
                q.popleft()
           
            if(len(q)>0 and arr[q[-1]]<=arr[i]):
                while(len(q)>0 and arr[q[-1]]<=arr[i]):
                    q.pop()
            q.append(i)
            ans.append(arr[q[0]])
        return ans
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n,k = map(int,input().strip().split())
        arr = list(map(int,input().strip().split()))
        ob=Solution()
        res = ob.max_of_subarrays(arr,n,k)
        for i in range (len (res)):
            print (res[i], end = " ")
        print()
# } Driver Code Ends
