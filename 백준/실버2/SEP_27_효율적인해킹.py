"""
효율적인 해킹 

https://www.acmicpc.net/problem/1325

방향성 있는 그래프에서의 DFS/BFS

"""
import sys
from collections import deque
input = sys.stdin.readline


V, E = map(int, input().rstrip().split())
graph = [[] for _ in range(V+1)]
visited = []

for _ in range(E): 
  v1, v2 = map(int, input().rstrip().split())

  graph[v2].append(v1)

def bfs(v): 
  visited = [0 for _ in range(V + 1)] 
  cnt = 1
  q = deque([v])
  visited[v] = 1 

  while q:   
    node = q.popleft() 

    for neigh in graph[node]: 
      if visited[neigh] == 0: 
        q.append(neigh)
        visited[neigh] = 1 
        cnt += 1 
  
  return cnt 

max_cnt = 0 
res = [] 
for v in range(1, len(graph)): 
  cnt = bfs(v)
  max_cnt = max(max_cnt, cnt)
  res.append([v, cnt])

final = []
for i in range(len(res)): 
  if res[i][1] == max_cnt: 
    final.append(res[i][0])

print(*final)
