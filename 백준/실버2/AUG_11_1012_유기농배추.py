"""
1012. 유기농 배추

DFS 문제. 

"""

import sys
input = sys.stdin.readline
numTC = int(input())  # count # of test cases


# ====
# 탐색.


def dfs(row, col):
    # 종료 조건.
    if row < 0 or row > len(graph) - 1 or col < 0 or col > len(graph[0]) - 1 or graph[row][col] != 1:
        return

    # 한 번 봤던 자리는 0 으로 바꾸어 다시 방문 하지 않도록 한다.
    graph[row][col] = 0

    dfs(row - 1, col)  # north
    dfs(row + 1, col)  # south
    dfs(row, col + 1)  # east
    dfs(row, col - 1)  # west

    return


def findBaeChoo():
    count = 0
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j] == 1:
                count += 1
                dfs(i, j)

    return count

# ===


for _ in range(numTC):
    N, M, K = map(int, input().split())  # w, h, # 배추
    graph = [[0] * N for _ in range(M)]

    result = 0  # 지렁이 수

    # 그래프 생성
    for _ in range(K):  # 배추수 만큼 추가
        a, b = map(int, input().split())
        graph[b][a] = 1  # 배추 위치 표기

    print(findBaeChoo())
