#Your task is to complete this function
#Function should return complete string
def encode(arr):
    # Code here
    ans=[]
    ans.append(arr[0])
    ans.append(1)
    index=0
    s=""
    for i in range(1,len(arr)):
        if(arr[i]==ans[index]):
            ans[index+1]=ans[index+1]+1
        else:
            ans.append(arr[i])
            ans.append(1)
            index+=2
    
    for i in ans:
        s=s+str(i)
    return s
        

#{ 
#  Driver Code Starts
#Your code will prepended here
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        arr=input().strip()
        print (encode(arr))
# } Driver Code Ends
