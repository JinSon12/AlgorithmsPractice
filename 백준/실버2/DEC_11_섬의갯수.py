import sys
from collections import deque

grid = []
visited = set()
dirs = [[-1, 0], [1, 0], [0, -1], [0, 1], [1, 1], [-1, -1], [1, -1], [-1, 1]]


def findIslands():
    def BFS(r, c):
        q = deque([[r, c]])
        while q:
            x, y = q.popleft()

            for dir in dirs:
                newx = x + dir[0]
                newy = y + dir[1]

                if 0 <= newx < len(grid) and 0 <= newy < len(grid[0]) and (newx, newy) not in visited:
                    if grid[newx][newy] == 1:
                        # if newx not visited
                        visited.add((newx, newy))
                        q.append([newx, newy])

    count = 0

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (i, j) not in visited and grid[i][j] == 1:
                visited.add((i, j))
                BFS(i, j)
                count += 1

    print(count, "answer")


while True:
    W, H = map(int, input().split())
    if W == 0 and H == 0:
        break

    # initialization 하는 것을 잊지 말기.
    grid = []
    visited = set()
    for i in range(H):
        grid.append(list(map(int, input().split())))

    # print(grid)
    findIslands()


def countWallsV2():
    dx = [0, 0, -1, 1, -1, -1, 1, 1]
    dy = [-1, 1, 0, 0, -1, 1, 1, -1]

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))

        while queue:
            a, b = queue.popleft()
            # ! visited 배열을 따로 사용하지 않고, 원 배열을 직접 modify 하여 방문 확인.
            graph[a][b] == 0

            # 상하좌우, 대각선 좌상,좌하,우상,우하 4개 포함 총 8개
            # 이동
            for i in range(8):
                nx = a + dx[i]
                ny = b + dy[i]
                if nx < 0 or nx > h-1 or ny < 0 or ny > w-1:
                    continue
                if graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    queue.append((nx, ny))
        return

    read = sys.stdin.readline
    while 1:

        w, h = map(int, read().split())
        if w == 0 and h == 0:
            break

        graph = [list(map(int, read().split())) for _ in range(h)]

        count = 0
        for i in range(h):
            for j in range(w):
                if graph[i][j] == 1:
                    bfs(i, j)
                    count += 1
        print(count)
