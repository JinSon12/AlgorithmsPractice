"""
11724. 연결 요소의 갯수. 

"""

from collections import deque
import sys
input = sys.stdin.readline

NV, NE = map(int, input().split())  # num of vertices, num of edges

graph = [[] for _ in range(NV+1)]

graph[0] = [0, 0]

# creating the graph
for _ in range(NE):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# print(graph)

visited = [False] * (NV + 1)


def bfs(node):
    queue = deque([node])
    visited[node] = True

    while queue:
        n = queue.popleft()

        for neigh in graph[n]:
            if not visited[neigh]:
                queue.append(neigh)
                visited[neigh] = True


counter = 0  # to be returned.

for i in range(1, len(graph)):
    if not visited[i]:
        bfs(i)
        counter += 1

print(counter)


# dfs 추후 수정 요  복습 요 
sys.setrecursionlimit(1000000)


def dfs(v):
    visited[v] = True           # 방문 표시

    for u in graph[v]:          # 정점 v와 인접한 정점들을 하나씩 살펴보면서
        if visited[u] == False:  # 만약 방문하지 않았다면 dfs로 방문
            dfs(u)


n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[] for _ in range(n+1)]
visited = [False] * (n+1)
count = 0

for i in range(m):      # 해당 정점과  인접한 정점들을 저장
    u, v = map(int, sys.stdin.readline().rstrip().split())
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, n+1):
    if visited[i] == False:
        dfs(i)
        count += 1

print(count)
