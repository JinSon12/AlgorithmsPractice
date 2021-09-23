"""
연구소 

https://www.acmicpc.net/problem/14502


"""
import sys, copy
from collections import deque

input = sys.stdin.readline

R, C = map(int, input().rstrip().split())
grid = [list(map(int, input().split())) for _ in range(R)] 
dirs = [[1,0], [-1,0], [0, -1], [0, 1]]
max_safe_area = 0 

def bfs(): 
  temp_grid = copy.deepcopy(grid)
  # cnt = 0 
  q = deque([])
  global max_safe_area
  # visited = [[0] * C for _ in range(R)]

  for i in range(R): 
    for j in range(C): 
      if temp_grid[i][j] == 2:    # if virus 
        q.append([i,j])
        # cnt += 1 

  # spread the virus 
  while q: 
    r, c = q.popleft() 

    for x, y in dirs: 
      newr = r + y 
      newc = c + x

      if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and temp_grid[newr][newc] == 0: 
        temp_grid[newr][newc] = 2 
        q.append([newr, newc])
        # cnt += 1 
        # visited[newr][newc] = 1 

  total = 0 
  for i in range(R): 
    for j in range(C): 
      if temp_grid[i][j] == 0: 
        total += 1 

  max_safe_area = max(max_safe_area, total)


# dfs 의 응용을 통해서 grid 의 수를 바꾸어 (0 -> 1) 벽을 세운 것으로 간주한다. 
def createWalls(cnt):
  if cnt == 3: 
    bfs() 
    return 
  
  for i in range(R):
    for j in range(C): 
      if grid[i][j] == 0: 
        grid[i][j] = 1
        createWalls(cnt + 1) 
        grid[i][j] = 0 

createWalls(0)
print(max_safe_area) 