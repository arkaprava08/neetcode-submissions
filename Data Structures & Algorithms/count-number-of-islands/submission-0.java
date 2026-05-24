class Solution {
    public char[][] resetIsland(char[][] grid, int i, int j) {
        if(!(i >= 0 && i < grid.length) || !(j >= 0 && j < grid[0].length))
            return grid;
        if(grid[i][j] == '0')
            return grid;
        
        grid[i][j] = '0';

        grid = resetIsland(grid, i-1, j);
        grid = resetIsland(grid, i, j-1);
        grid = resetIsland(grid, i+1, j);
        grid = resetIsland(grid, i, j+1);

        return grid;
    }

    public int numIslands(char[][] grid) {
        int islandBoy=0;

        for(int i=0; i<grid.length; i++) {
            for(int j=0; j<grid[0].length; j++) {
                if(grid[i][j] == '1') {
                    ++islandBoy;
                    grid = resetIsland(grid, i, j);
                }
            }
        }

        return islandBoy;
    }
}
