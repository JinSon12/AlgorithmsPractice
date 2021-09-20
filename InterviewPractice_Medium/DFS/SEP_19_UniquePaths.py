"""
Unique Paths 

https://leetcode.com/problems/unique-paths/


DFS (cache)
DP 

"""

from functools import cache

class Solution:
    # Time: O(2^(m*n))?
    def uniquePaths(self, m: int, n: int) -> int:
        count = 0
        visited = set()

        @cache
        def dfs(r, c):
            # termination condition
            if r == m-1 and c == n-1:
                return 1

            elif r > m or c > n:
                return 0

            top = right = 0
            if (r+1, c) not in visited:
                visited.add((r+1, c))
                top = dfs(r + 1, c)
                visited.remove((r+1, c))
                
            if (r, c + 1) not in visited:
                visited.add((r, c+1))
                right = dfs(r, c + 1)
                visited.remove((r, c+1))

            return top + right
        
        res = dfs(0, 0)
        return res