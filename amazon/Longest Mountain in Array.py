def left(arr,a):
    index=a
    for i in range(a,0,-1):
        if(arr[i]>arr[i-1]):
            index=i-1
        else:
            break
    return index
def right(arr,a):
    index=a
    for i in range(a,len(arr)-1):
        if(arr[i]>arr[i+1]):
            index=i+1
        else:
            break
    return index   
class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        m=0
        for i in range(1,len(arr)-1):
            if(arr[i]>arr[i-1] and arr[i]>arr[i+1]):
               

                a=left(arr,i)
                b=right(arr,i)


                m=max(m,b-a+1)
        return m
        
