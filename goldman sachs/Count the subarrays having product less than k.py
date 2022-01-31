#User function Template for python3

class Solution:
    def countSubArrayProductLessThanK(self, a, n, k):
        #Code here
        ans=[0 for i in range(n)]
        ptr1=0
        ptr2=0
        b=0
        product=1
        for i in range(0,n):
            if(ans[i]<k):
                ptr1=i
                ptr2=i
                b=i
                break
        for i in range(b,len(a)):
            ptr2=i
          
          
            
            if(a[i]>=k):
                ans[i]=0
                product=1
                ptr1=i+1
              
            elif(a[i]*product <k):
                if(i!=0):
                    if(a[i]*a[i-1]>=k):
                        ans[i]=1
                        product=a[i]
                    else:
              
                        product=a[i]*product
                        ans[i]=ans[i-1]+1
                        ptr2=i
                else:
                    product=a[i]*product
                    ans[i]=1
                    ptr2=i
                    
            else:
                tep=i
                
                product=product*a[i]
                
                
                while(ptr1<ptr2 and product>=k):

                    product=product/a[ptr1]
                
                    ptr1+=1
                    if(product <k):
                        break
               
                ans[tep]=ptr2-ptr1+1
       
        
        return (sum(ans))
                
    
    
    
    

#{ 
#  Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n, k = [int(x) for x in input().strip().split()]
        arr = [int(x) for x in input().strip().split()]
        
        print(Solution().countSubArrayProductLessThanK(arr, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends
