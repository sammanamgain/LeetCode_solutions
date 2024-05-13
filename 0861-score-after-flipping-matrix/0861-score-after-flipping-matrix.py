class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        m=len(grid[0])
        n=len(grid)
        for i in range(m):
            print(grid)
            for j in range(n):
                if i ==0:
                    if grid[j][i]==0:
                        for k in range(m):
                            if grid[j][k]==0:
                                grid[j][k]=1
                            else:
                                grid[j][k]=0
                else:
                    countOne=0
                    countZero=0
                    for k in range(n):
                        if grid[k][i]==0:
                            countZero+=1
                        else:
                            countOne+=1
                    if countZero>countOne:
                        for k in range(n):
                            if grid[k][i]==0:
                                grid[k][i]=1
                            else:
                                grid[k][i]=0
        print(grid)
        sum=0
        for i in range(n):
            temp=''
            for j in range(m):
                temp+=str(grid[i][j])
            decimal_num = int(temp, 2)
            sum+=decimal_num
        
        return sum
                






        