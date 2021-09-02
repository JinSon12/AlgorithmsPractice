""""
안전지대 

https://www.acmicpc.net/problem/2468

Key Insight: 
- 2d 행렬이고, 저장해야 할 데이터가 많다면 (visited), set 보다는 visited array 를 사용하는 것이 더 빠르다. 

"""
from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
grid = [list(map(int, input().split())) for _ in range(N)]
minHeight = min(map(min, grid))
maxHeight = max(map(max, grid))


def findMaxSafeArea(grid, minHeight, maxHeight):

    def bfs(row, col, height):
        dirs = [[-1, 0], [1, 0], [0, 1], [0, -1]]
        q = deque([[row, col]])

        while q:
            r, c = q.popleft()

            for x, y in dirs:
                newr = r + y
                newc = c + x

                if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and grid[newr][newc] >= height:
                    if visited[newr][newc] == 0:
                        q.append([newr, newc])
                        visited[newr][newc] = 1

    maxSafeArea = 0
    for h in range(minHeight, maxHeight + 1):
        temp = 0
        visited = [[0] * N for _ in range(N)]
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] >= h and visited[i][j] == 0:
                    visited[i][j] = 1
                    temp += 1
                    bfs(i, j, h)

        maxSafeArea = max(temp, maxSafeArea)

    return maxSafeArea


print(findMaxSafeArea(grid, minHeight, maxHeight))


def faster():

    read = sys.stdin.readline

    N = int(read())
    P = [list(map(int, read().strip().split())) for _ in range(N)]
    # print(N, P)

    height_set = set()
    for r in range(N):
        for c in range(N):
            height_set.add(P[r][c])
    # print(height_set)

    visited = [[0]*N for _ in range(N)]
    # print(visited)

    def bfs(start_r, start_c, w_height):
        if not P[start_r][start_c] > w_height:
            return 0
        queue = deque()
        queue.append([start_r, start_c])
        visited[start_r][start_c] = 1
        count = 1

        while queue:
            rr, cc = queue.popleft()
            for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nr, nc = rr + dr, cc + dc
                if not (-1 < nr < N and -1 < nc < N):
                    # print("over boundary")
                    continue
                if P[nr][nc] > w_height and visited[nr][nc] == 0:
                    # print(nr, nc)
                    queue.append([nr, nc])
                    visited[nr][nc] = 1
                    count += 1

        # print(start_r, start_c, w_height, count, visited)
        return count

    def get_count(water_height):
        count = 0
        for rr in range(N):
            for cc in range(N):
                if visited[rr][cc] == 1:
                    continue
                if bfs(rr, cc, water_height) > 0:
                    count += 1
        return count

    max_count = -1
    # for height in height_set:
    for height in range(max(height_set)):
        max_count = max(get_count(height), max_count)
        # print(visited)
        visited = [[0]*N for _ in range(N)]
        # print(max_count)

    print(max_count)
