"""
01 Matrix 
https://leetcode.com/problems/01-matrix/

- Single BFS (from points that are 0 -> other numbers)
- Multiple BFS (from points that are not 0 -> 0 and calculate the minimum distance)
- DP 

복습 
"""

from collections import deque
import math
from typing import List


class Solution:
    # multiple BFS (starting from points that are not 0 to 0)
    # very slow. (TLE )
    def updateMatrix_multipleBFS(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        # visited = [[0]* len(mat[0]) for _ in range(len(mat))]

        def bfs(r, c):
            min_dist = max(len(mat), len(mat[0])) + 1
            q = deque([])
            q.append((r, c, 1))
            visited = set({(r, c)})

            # print(visited, "visited")
            while q:
                nr, nc, dist = q.popleft()
                print(nr, nc)

                for x, y in dirs:
                    newx = nr + x
                    newy = nc + y
                    print(newx, newy, visited)
                    # print((newx, newy) not in visited)
                    if 0 <= newx < len(mat) and 0 <= newy < len(mat[0]) and (newx, newy) not in visited:
                        if mat[newx][newy] == 0:
                            print("dirs", dist)
                            min_dist = min(min_dist, dist)
                            mat[r][c] = min_dist
                            return
                        else:
                            q.append((newx, newy, dist + 1))
                            visited.add((newx, newy))

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] != 0:
                    print("enter")
                    bfs(i, j)

        return mat

    # Single BFS
    # Faster (49%), 710ms
    def updateMatrix_singleBFS(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        visited = [[0] * len(mat[0]) for _ in range(len(mat))]
        q = deque([])

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.append((i, j))
                    visited[i][j] = 1

        while q:
            nr, nc = q.popleft()

            for x, y in dirs:
                newx = nr + x
                newy = nc + y

                if 0 <= newx < len(mat) and 0 <= newy < len(mat[0]) and visited[newx][newy] == 0:
                    q.append((newx, newy))
                    visited[newx][newy] = 1
                    mat[newx][newy] = mat[nr][nc] + 1

        return mat

    # DP
    # https://leetcode.com/problems/01-matrix/discuss/1369741/C%2B%2BJavaPython-BFS-DP-solutions-with-Picture-Clean-and-Concise-O(1)-Space
    def updateMatrix_DP(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])

        for r in range(m):
            for c in range(n):
                if mat[r][c] > 0:
                    top = mat[r - 1][c] if r > 0 else math.inf
                    left = mat[r][c - 1] if c > 0 else math.inf
                    mat[r][c] = min(top, left) + 1

        for r in range(m - 1, -1, -1):
            for c in range(n - 1, -1, -1):
                if mat[r][c] > 0:
                    bottom = mat[r + 1][c] if r < m - 1 else math.inf
                    right = mat[r][c + 1] if c < n - 1 else math.inf
                    mat[r][c] = min(mat[r][c], bottom + 1, right + 1)

        return mat

    # fastest. - add 1 more to the dist (self), if NEWS of it is all >= distance.
    # single pass BFS 를 한번 더 꼬아서 생각 한 것. (1 의 입장에서.)
    def updateMatrix_fastest(self, mat: List[List[int]]) -> List[List[int]]:
        nrow, ncol = len(mat), len(mat[0])
        queue = []
        for r, row in enumerate(mat):
            for c, val in enumerate(row):
                if val != 0:
                    queue.append((r, c))

        distance = 1
        while queue:
            q = []
            for r, c in queue:
                if ((r == 0 or mat[r - 1][c] >= distance) and (c == 0 or mat[r][c - 1] >= distance) and (r == nrow - 1 or mat[r + 1][c] >= distance) and (c == ncol - 1 or mat[r][c + 1] >= distance)):
                    mat[r][c] = distance + 1
                    q.append((r, c))
            distance += 1
            queue = q

        return mat


stn = Solution()
stn.updateMatrix_fastest([[0, 0, 0], [0, 1, 0], [1, 1, 1]])
