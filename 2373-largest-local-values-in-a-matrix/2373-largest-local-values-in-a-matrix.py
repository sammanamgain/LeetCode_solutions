class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        
        result=[]
        n=len(grid)
        for i in range(2,n):
            temp=[]
            for j in range(2,n):
                Max=0
                for k in range(i-2,i+1):
                    for l in range(j-2,j+1):
                        Max=max(Max,grid[k][l])
                temp.append(Max)
            result.append(temp)
        return result
                



        