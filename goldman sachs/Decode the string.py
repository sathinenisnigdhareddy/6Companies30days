#User function Template for python3

class Solution:
    def decodedString(self, s):
        # code here
        string=[]
        num=[]
        i=0
        res=''
        count=0
        while(i<len(s)):
            if(s[i].isdigit()):
                count=0
             
                
                while(i<len(s) and s[i].isdigit()):
                    count=count*10+int(s[i])
                    i+=1
              
                num.append(count)
              
           
            
            
            
            elif(s[i]=='['):
                string.append(res)
                res=''
                i+=1
                
                
                
            elif(s[i]==']'):
                x=string.pop()
                y=num.pop()
               
               
                for k in range(y):
                    x+=res
                i+=1
                
                res=x
                
            
            
            else:
                res+=s[i]
                i+=1
        return res
                

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        
        ob = Solution()
        print(ob.decodedString(s))
# } Driver Code Ends
