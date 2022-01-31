#User function Template for python3
def check(mat,row,col):
  
    for i in range(row,row+3):
        for j in range(col,col+3):
            if(mat[i][j]!=0):
               
                r=0
                for m in range(row,row+3):
                    for n in range(col,col+3):
                        if(mat[m][n]==mat[i][j]):
                            r+=1
                if(r>1):
                    return 0
                

    return 1
class Solution:
    def isValid(self, mat):
        # code here
        
        for i in range(0,9):
            for j in range(0,9):
                if(mat[i][j]!=0):
                    r=0
                    c=0
                    for k in range(0,9):
                        if(mat[i][k]==mat[i][j]):
                            r+=1
                            
                        if(mat[k][j]==mat[i][j]):
                            c+=1
                    
                    a=check(mat,(i//3)*3,(j//3)*3)
                    if(r>1 or c>1 or a==0):
                        return 0
                    
                        
        return 1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        arr = input().split()
        mat = [[0]*9 for x in range(9)]
        for i in range(81):
            mat[i//9][i%9] = int(arr[i])
        
        ob = Solution()
        print(ob.isValid(mat))
# } Driver Code Ends
