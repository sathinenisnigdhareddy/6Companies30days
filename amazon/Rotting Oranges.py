import collections
def fun(stack,count):
    global grid1
  
    while(len(stack)>0):
        m=stack.popleft()
        if(m!='*'):
            x=m[0]
            y=m[1]
            if(x-1>=0 ):
                if(grid1[x-1][y]==1):
                    grid1[x-1][y]=2
                    stack.append([x-1,y])
            if(y-1>=0):
                if(grid1[x][y-1]==1):
                    grid1[x][y-1]=2
                    stack.append([x,y-1])
            if(x+1<len(grid1)):
                if(grid1[x+1][y]==1):
                    grid1[x+1][y]=2
                    stack.append([x+1,y])
            if(y+1<len(grid1[0])):
                if(grid1[x][y+1]==1):
                    grid1[x][y+1]=2
                    stack.append([x,y+1])
        else:
            if(len(stack)>0 and stack[-1]!='*'):
                count+=1
                stack.append('*')
    return count
grid1=[]

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        stack=collections.deque()
        global grid1
      
        grid1=grid
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==2):
                    stack.append([i,j])
        
        stack.append('*')
        a=fun(stack,0)
        for i in range(0,len(grid)):
            for j in range(0,len(grid[0])):
                if(grid[i][j]==1):
                    return -1
        return a
        
           
       
        
