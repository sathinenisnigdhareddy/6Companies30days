def check(ans,str1):
    a=ans
    while(len(ans)<=len(str1)):
        if(ans==str1):
            return True
        else:
            ans=ans+a
    return False
    
        
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        a=min(len(str1),len(str2))
        ans=''
        final=""
        for i in range(0,a):
            if(str1[i]==str2[i]):
                ans=ans+str1[i]
                if(check(ans,str1) and check(ans,str2)):
                    final=ans
        return final
            
