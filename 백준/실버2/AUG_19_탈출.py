"""
3184. 양

DFS solutions 
# https://velog.io/@gomster_96/백준-3184-양-DFS 
# https://ariz1623.tistory.com/134
"""

import sys
from collections import deque

N, M = map(int, input().split())
grid = []
visited = [[0 for _ in range(M)] for _ in range(N)]
dirs = [(-1, 0), (0, -1), (0, 1), (1, 0)]


for _ in range(N):
    grid.append(list(input().rstrip()))


def findStartPosition():
    wolves, sheep = 0, 0
    for i in range(N):
        for j in range(M):
            if grid[i][j] != "#" and visited[i][j] == 0:
                tw, ts = BFS(i, j)
                wolves += tw
                sheep += ts

    print(sheep, wolves)


def BFS(startx, starty):
    countW = 0
    countS = 0

    q = deque([[startx, starty]])
    visited[startx][starty] = 1

    while q:
        x, y = q.popleft()

        if grid[x][y] == "o":
            countS += 1

        elif grid[x][y] == "v":
            countW += 1

        for dir in dirs:
            newx = x + dir[0]
            newy = y + dir[1]

            if newx >= 0 and newy >= 0 and newx < len(grid) and newy < len(grid[0]):
                if visited[newx][newy] == 0 and grid[newx][newy] != "#":
                    q.append([newx, newy])
                    visited[newx][newy] = 1

    # print("countw", countW, "counts", countS)
    if countW < countS:
        countW = 0
    else:
        countS = 0
    # print("countw", countW, "counts", countS)

    return (countW, countS)


findStartPosition()

"""
# Recursive (DFS)

"""

# set recursion limit
sys.setrecursionlimit(int(10e6))

# solve function


def solve(x, y, R, C):
    #global variables
    global escaped, sheeps, wolves

    # mark as visited
    isVisited[x][y] = True

    # check for sheep or wolf
    if grid[x][y] == 'o':
        sheeps += 1
    elif grid[x][y] == 'v':
        wolves += 1

    # check for escape
    if y - 1 < 0 or x - 1 < 0 or y + 1 >= C or x + 1 >= R:
        escaped = True

    # serach neighbors
    if y - 1 >= 0 and not isVisited[x][y - 1] and grid[x][y - 1] != '#':
        solve(x, y - 1, R, C)
    if x - 1 >= 0 and not isVisited[x - 1][y] and grid[x - 1][y] != '#':
        solve(x - 1, y, R, C)
    if y + 1 < C and not isVisited[x][y + 1] and grid[x][y + 1] != '#':
        solve(x, y + 1, R, C)
    if x + 1 < R and not isVisited[x + 1][y] and grid[x + 1][y] != '#':
        solve(x + 1, y, R, C)


# main
if __name__ == "__main__":
    # get R, C
    R, C = map(int, sys.stdin.readline().rstrip().split())

    # get grid
    grid = [list(sys.stdin.readline().rstrip())
            for i in range(R)]

    # isVisited grid
    isVisited = [[False for i in range(C)]
                 for i in range(R)]

    # solve
    ans = [0, 0]
    for i in range(R):
        for j in range(C):
            if grid[i][j] == '#' or isVisited[i][j]:
                continue

            escaped, sheeps, wolves = False, 0, 0
            solve(i, j, R, C)

            if escaped:
                continue

            if sheeps > wolves:
                ans[0] += sheeps
            else:
                ans[1] += wolves

    # print answer
    print(ans[0], ans[1])
