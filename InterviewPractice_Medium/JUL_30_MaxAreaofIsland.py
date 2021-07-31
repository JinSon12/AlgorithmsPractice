class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        def dfs(row, col, area):
            if row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0]) - 1 or grid[row][col] != 1:
                return 0
            area += 1
            grid[row][col] = 0

            north = dfs(row + 1, col, area)
            south = dfs(row - 1, col, area)
            east = dfs(row, col + 1, area)
            west = dfs(row, col - 1, area)

            return north + south + east + west + 1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    area = dfs(i, j, 0)
                    maxArea = max(maxArea, area)

        return maxArea
