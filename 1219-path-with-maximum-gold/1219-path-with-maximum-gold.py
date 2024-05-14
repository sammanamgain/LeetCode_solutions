class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        dx=(-1,0,0,1)
        dy=(0,-1,1,0)
        n=len(grid)
        m=len(grid[0])
        def dfs(i,j,grid):
            if i<0 or i>=n or j<0 or j>=m or grid[i][j]==0:
                return 0
            maxSum=0
            curVal=grid[i][j]
            for d in range(4):
                ni=i+dx[d]
                nj=j+dy[d]
                grid[i][j]=0
                maxSum=max(maxSum,curVal+dfs(ni,nj,grid))
                grid[i][j]=curVal
            return maxSum


        ans=0
        for i in range(n):
            for j in range(m):
                if grid[i][j]!=0:
                    ans=max(ans,dfs(i,j,grid))
        return ans