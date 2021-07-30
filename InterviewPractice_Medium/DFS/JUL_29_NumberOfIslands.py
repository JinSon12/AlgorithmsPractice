# https://leetcode.com/problems/number-of-islands/

class Solution:
    """
    200. Number of Islands

    Key Insight: 
    - DFS or BFS 
    - Either recursive, or iterative possible. 
    """

    # recursive solution,
    # 138 ~ 144ms, 80% ~ 56% fast

    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1 or grid[row][col] != "1":
                return

            grid[row][col] = "0"

            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        if len(grid) == 1 and len(grid[0]) == 1:
            return str(grid[0][0])

        count = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    # dfs until we hit water
                    dfs(i, j)
                    count += 1

        return count
