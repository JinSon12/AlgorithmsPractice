"""
https://leetcode.com/problems/rotting-oranges/

BFS (돌면서 숫자 붙이기? (time을 증가시키면서 붙이기?))
- 저번 단계에서 있었던 숫자를 증가시키면서 탐색하기. (최소한의 단계의 시간, 거리, 등등이 걸리는지 알아보는 문제.)

유사한 문제 
https://www.acmicpc.net/problem/7576 백준 토마토 

복습
"""
from collections import deque
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set({})
        q = deque([])

        def BFS():
            while q:
                r, c, dist = q.popleft()

                for x, y in dirs:
                    newr = r + x
                    newc = c + y

                    if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and (newr, newc) not in visited:
                        if grid[newr][newc] != 0:
                            q.append((newr, newc, dist+1))
                            # 썩은 시간에 + 1 해서 저장.
                            grid[newr][newc] = grid[r][c] + 1
                            visited.add((newr, newc))

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = 0  # 어차피 grid 변형해도 문제 없음. (반환 x)
                    q.append((i, j, 0))
                    visited.add((i, j))

        BFS()

        time = -sys.maxsize

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1 and (i, j) not in visited:
                    return -1
                else:
                    time = max(time, grid[i][j])

        return time

    # time, oranges variable 사용하여 v1 에서 했던 이중 포문을 사용해서
    # 최대 결과 값을 찾아내는 것이 아니라
    # orange 변수에 총 오렌지 갯수를 저장해서 오렌지가 남아있으면 -1 (BFS 에서 도달하지 못했다 )
    # 아니면 time 을 반환한다.
    # time 은 각 단계마다 (한 층마다) 추가된다.
    def orangesRotting(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set({})
        q = deque([])
        oranges = 0

        def BFS(oranges):
            time = 0  # 시간을 써서 밑에 추가적으로 for loop 사용을 하지 않아도 되도록 한다.
            while q and oranges > 0:
                for _ in range(len(q)):  # 현 시점에 저장되어 있는 원소들만 탐색 하고 시간 업데이트.
                    r, c, dist = q.popleft()

                    for x, y in dirs:
                        newr = r + x
                        newc = c + y

                        if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and (newr, newc) not in visited:
                            if grid[newr][newc] != 0:
                                q.append((newr, newc, dist+1))
                                oranges -= 1
                                # 썩은 시간에 + 1 해서 저장.
                                grid[newr][newc] = grid[r][c] + 1
                                visited.add((newr, newc))

                time += 1

            return (time, oranges)

        # 그리드를 돌면서 오렌지, 썩은 오랜지를 각각 oranges, 큐에 추가한다.
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = 0  # 어차피 grid 변형해도 문제 없음. (반환 x)
                    q.append((i, j, 0))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    oranges += 1

        time, oranges = BFS(oranges)

        return time if oranges == 0 else -1

    def orangesRotting_faster(self, grid: List[List[int]]) -> int:
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set({})
        q = deque([])
        oranges = 0

        def BFS(oranges):
            time = 0  # 시간을 써서 밑에 추가적으로 for loop 사용을 하지 않아도 되도록 한다.
            while q and oranges > 0:
                for _ in range(len(q)):  # 현 시점에 저장되어 있는 원소들만 탐색 하고 시간 업데이트.
                    r, c, dist = q.popleft()

                    for x, y in dirs:
                        newr = r + x
                        newc = c + y

                        if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and (newr, newc) not in visited:
                            if grid[newr][newc] != 0:
                                q.append((newr, newc, dist+1))
                                oranges -= 1
                                # 썩은 시간에 + 1 해서 저장.
                                grid[newr][newc] = grid[r][c] + 1
                                visited.add((newr, newc))

                time += 1

            return (time, oranges)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 2:
                    grid[i][j] = 0  # 어차피 grid 변형해도 문제 없음. (반환 x)
                    q.append((i, j, 0))
                    visited.add((i, j))
                elif grid[i][j] == 1:
                    oranges += 1

        time, oranges = BFS(oranges)

        return time if oranges == 0 else -1

    def orangesRotting_fastest(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[False for _ in range(n)] for _ in range(m)]

        minutes = -1

        queue = deque()
        live = 0

        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 2):
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    live += 1

        queue.append(None)
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while(len(queue) != 0):

            rotten = queue.popleft()

            if(rotten == None):
                minutes += 1

                if(len(queue) != 0):
                    queue.append(None)

            else:

                for neighbor in neighbors:
                    new_dead_row = rotten[0] + neighbor[0]
                    new_dead_col = rotten[1] + neighbor[1]

                    if(0 <= new_dead_row < m and 0 <= new_dead_col < n):
                        if(grid[new_dead_row][new_dead_col] == 1):
                            grid[new_dead_row][new_dead_col] = 2
                            live -= 1
                            queue.append((new_dead_row, new_dead_col))

        if(live != 0):
            return -1

        return minutes
