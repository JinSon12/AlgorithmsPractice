"""
Island Perimeter. 

https://leetcode.com/problems/island-perimeter/

Key Point: 
- if border => return 1 
- if water => return 1 
- visit only the land. if you see the above condition, return 1 

"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        C = len(grid[0])
        L = len(grid)
        visited = [[0] * C for _ in range(L)]

        
        def dfs(row, col): 
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]): 
                return 1
            
            if grid[row][col] == 0: 
                return 1
              
            if grid[row][col] == 2: 
                return 0 
            
            grid[row][col] = 2 
            
            n = dfs(row + 1, col)
            
            s = dfs(row - 1, col)
                              
            w = dfs(row, col + 1)
                          
            e = dfs(row, col - 1)                  

            
            return n + s + w + e
        
        numsq = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])): 
                if grid[i][j] == 1: 
                    numsq += dfs(i, j)
       
        
        return numsq

    # faster.
    def islandPerimeter_v2(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for row_idx, row in enumerate(grid):
            for col_idx, land in enumerate(row):
                if not land:
                    continue
                perimeter +=4
                
                if col_idx and row[col_idx-1]: #check for land in the prev cell of the same row (horizontally behind)
                    perimeter -=2
                
                if row_idx and grid[row_idx-1][col_idx]: #check for land just above
                    perimeter -=2
        return perimeter