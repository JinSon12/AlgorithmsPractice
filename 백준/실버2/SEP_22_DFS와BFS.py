""" 
DFS 와 BFS 

https://www.acmicpc.net/problem/1260
"""
import sys
from collections import deque
input = sys.stdin.readline

V, E, SV = map(int, input().rstrip().split())
graph = [[] for _ in range(V+1)] 

for _ in range(E): 
  a, b = map(int, input().rstrip().split())

  graph[a].append(b)
  graph[b].append(a)

graph.sort()
print(graph)

def printDFSResult(): 
  visited = set({SV})
  res = [] 

  def dfs(node):
    res.append(node)
    for neigh in graph[node]: 
      if neigh not in visited: 
        visited.add(neigh)
        dfs(neigh)
        # visited.remove(neigh)
  

  dfs(SV) 
  print(visited)
  return res


def printBFSResult(): 
  res = []
  visited = set({SV})
  q = deque([SV])

  while q: 
    node = q.popleft() 
    
    res.append(node)

    for neigh in graph[node]: 
      if neigh not in visited: 
        q.append(neigh)
        visited.add(neigh)
  
  return res
  

print(*printDFSResult())
  

