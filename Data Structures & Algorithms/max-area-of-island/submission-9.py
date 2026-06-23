class Solution:
    def findConnectedPoints(self, grid, i, j):
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

    def findConnectedIsland(self, grid, i, j) -> int:
        if grid[i][j] == 0:
            return 0
        
        grid[i][j]=0
        
        ans=1
        for connect in self.findConnectedPoints(grid, i,j):
            ans+=self.findConnectedIsland(grid, connect[0], connect[1])

        return ans

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        out=0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    out=max(out, self.findConnectedIsland(grid, i, j))

        return out