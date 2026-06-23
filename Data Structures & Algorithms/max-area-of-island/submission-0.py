class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        def findConnectedPoints(grid, i, j):
            connect=[]
            if i-1>=0:
                connect.append([i-1, j])
            if j-1>=0:
                connect.append([i, j-1])
            if i+1<len(grid):
                connect.append([i+1, j])
            if j+1<len(grid[0]):
                connect.append([i, j+1])
            
            return connect

        def findConnectedIsland(grid, i, j) -> int:
            if grid[i][j] == 0:
                return 0
            
            grid[i][j]=0
            
            ans=1
            for connect in findConnectedPoints(grid, i,j):
                ans+=findConnectedIsland(grid, connect[0], connect[1])

            return ans

        out=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                out=max(out, findConnectedIsland(grid, i, j))

        return out