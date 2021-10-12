"""
7562. 나이트의 이동. 

BFS 사용하여 구하기. 
- 기존의 BFS 는 동서남북으로 하였지만, 이번에는 custom 한 방향으로 움직인다. (이것이 유일한 차이점.)
"""
import timeit
import sys
from collections import deque
input = sys.stdin.readline

dirs = [[2, 1], [2, -1], [-2, 1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]


def BFS(startx, starty, endx, endy):
    if startx == endx and starty == endy:
        return 0

    q = deque([[startx, starty, 0]])  # row, col, moveCount
    visited[startx][starty] = True

    while q:
        x, y, moveCount = q.popleft()
        # print(x, y)
        if x == endx and y == endy:
            return moveCount

        for dir in dirs:
            newx = dir[0] + x
            newy = dir[1] + y

            if newx >= 0 and newy >= 0 and newx < len(visited) and newy < len(visited):
                if visited[newx][newy] == False:
                    visited[newx][newy] = True
                    q.append([newx, newy, moveCount + 1])
    return -1


# TC = int(input())

# for _ in range(TC):
#     N = int(input())
#     visited = [[False for _ in range(N)] for _ in range(N)]

#     startRow, startCol = map(int, input().split())
#     endRow, endCol = map(int, input().split())

#     start = timeit.default_timer()
#     print(BFS(startRow, startCol, endRow, endCol))
#     stop = timeit.default_timer()

#     print('Time: for dp', stop - start)

N = 10000
visited = [[False for _ in range(N)] for _ in range(N)]
start = timeit.default_timer()
print(BFS(0, 0, 70, 950))
stop = timeit.default_timer()
print('Time: for dp', stop - start)

"""
Instead of using the moveCount and passing it along in the deque, 
we can also keep a variable called answer separately. 
"""
input = sys.stdin.readline


def bfs(start):
    move = [(2, 1), (1, 2), (-2, -1), (-1, -2),
            (2, -1), (-2, 1), (1, -2), (-1, 2)]
    visit = [[0]*n for _ in range(n)]
    ans = 0

    q = deque()
    q.append(start)
    visit[start[0]][start[1]] = 1

    while q:
        for _ in range(len(q)):
            x, y = q.popleft()

            if x == dest[0] and y == dest[1]:
                return ans

            for mv in move:
                nx, ny = x+mv[0], y+mv[1]

                if 0 <= nx < n and 0 <= ny < n:
                    if visit[nx][ny] == 0:
                        visit[nx][ny] = 1
                        q.append((nx, ny))

        ans += 1    # after a level has been checked, we add one to answer.
    return -1


# t = int(input())
# for _ in range(t):
#   n = int(input())
#   start = tuple(map(int, input().split()))
#   dest = tuple(map(int, input().split()))
#   print(bfs(start))
