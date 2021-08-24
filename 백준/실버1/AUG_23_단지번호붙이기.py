"""
2667. 단지 번호 붙이기

BFS/ DFS 로 해결 가능.
"""

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())

# DFS


def namePlaces_dfs(matrix):
    # 0 to keep track of the total number of 단지. next elements would be the count of houses in 단지.
    res = [0]

    def dfs(row, col):
        if row < 0 or row > N - 1 or col < 0 or col > N - 1 or matrix[row][col] == 0:
            return 0

        matrix[row][col] = 0

        no = dfs(row - 1, col)
        s = dfs(row + 1, col)
        e = dfs(row, col + 1)
        w = dfs(row, col - 1)

        return no + s + e + w + 1

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                res[0] += 1
                count = dfs(i, j)
                res.append(count)

    return res


"""
BFS 할때 Key Point, 
- 가야할 좌표를 저장하고 for loop 사용해서 access 한다 
- 0 < x < y 사용 가능. 
- q 에 추가할 때 방문처리를 한다 (popleft 한 다음에 방문처리하지 않는다 -- 이는 중복방문을 피하기 위해서다)

"""


def namePlaces_bfs(matrix):
    res = [0]

    def bfs(r, c):
        moves = [[-1, 0], [1, 0], [0, -1], [0, 1]]  # n, s, w, e
        numH = 1
        q = deque([[r, c]])
        matrix[r][c] = 0

        while q:
            r, c = q.popleft()

            for move in moves:
                newr = r + move[0]
                newc = c + move[1]

                if 0 <= newr <= N-1 and 0 <= newc <= N-1 and matrix[newr][newc] == 1:
                    numH += 1
                    # 추가할때 방문처리해줘야 중복된 자리를 방문하지 않는다. [1,2] 를 방문 할 것인데 다른 지점에서 [1,2] 방문하라고 추가됨.
                    matrix[newr][newc] = 0
                    q.append([newr, newc])

        return numH

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                res[0] += 1
                count = bfs(i, j)
                res.append(count)

    return res


matrix = []

for _ in range(N):
    matrix.append(list(map(int, list(input().rstrip()))))

res = namePlaces_bfs(matrix)
res = [res[0]] + sorted(res[1:])

for el in res:
    print(el)


""" 
다른 방식의 dfs 
- moves array 사용 
"""


def dfs_2():
    dir = [[0, 1], [0, -1], [1, 0], [-1, 0]]
    count_array = []
    count = 0

    def dfs(y, x):
        matrix[y][x] = 0    # 방문처리
        global count
        count += 1
        for dy, dx in dir:
            ny, nx = dy+y, dx+x
            if 0 <= ny < N and 0 <= nx < N and matrix[ny][nx] == 1:  # 조건 처리
                dfs(ny, nx)

    total = 0

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 1:
                count = 0
                dfs(i, j)
                total += 1
                count_array.append(count)

    count_array.sort()
    print(total)
    for i in count_array:
        print(i)
