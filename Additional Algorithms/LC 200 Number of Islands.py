class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Approach 1 - Using DFS approach for Graphs.
        num_rows = len(grid)
        if num_rows == 0 :
            return 0
        num_cols = len(grid[0])
        num_islands = 0
        for i in range (num_rows):
            for j in range(num_cols):
                if grid[i][j] == '1':
                    num_islands = num_islands + 1
                    self.DFS(grid, i, j)
                    
        return num_islands
        
        
    def DFS(self, grid,r,c):
        num_rows = len(grid)
        num_cols = len(grid[0])
        grid[r][c] = '0'
        if r+1 < num_rows and grid[r+1][c] == '1' :
            self.DFS (grid, r+1,c)
        if c+1 < num_cols and grid[r][c+1] == '1':
            self.DFS (grid,r,c+1)
        if r-1 >=0 and grid[r-1][c] == '1'  :
            self.DFS (grid,r-1,c)
        if c-1 >=0 and grid[r][c-1] == '1'  :
            self.DFS (grid,r,c-1)
        
        
    
        