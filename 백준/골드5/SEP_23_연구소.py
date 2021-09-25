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
  # DEEP COPY takes long time!!!!!!!!
  temp_grid = [[] * C for _ in range(R)]
  for i in range(R): 
    temp_grid[i] = grid[i][:]

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
  # if cnt == 3: 
  #   bfs() 
  #   return 
  
  for i in range(R):
    for j in range(C-2): 
      if grid[i][j] == 0: 
        grid[i][j] = 1
        grid[i][j+1] = 1
        grid[i][j+2] = 1
        bfs() 
        grid[i][j] = 0 
        grid[i][j+1] = 0
        grid[i][j+2] = 0

createWalls(0)
print(max_safe_area) 



"""
version 2. 
Faster 
"""

from itertools import combinations
import copy
from collections import deque

def v2(): 
  dx = [0,0,-1,1]
  dy = [1,-1,0,0]
  n, m = map(int, input().split(" "))
  board = [list(map(int, input().split(" "))) for _ in range(n)]

  candidate = []
  queue = deque()

  ret = 0
  for i in range(n):
      for j in range(m):
          if board[i][j] == 0:
              candidate.append((i,j))
          if board[i][j] == 2:
              queue.append((i,j))

  for can in list(combinations(candidate, 3)):
      nboard = copy.deepcopy(board)
      nqueue = copy.deepcopy(queue)
      for ele in can:
          nboard[ele[0]][ele[1]] = 1

      while nqueue:
          y, x = nqueue.popleft()

          for i in range(4):
              ny, nx = y + dy[i], x + dx[i]
              if ny < 0 or nx < 0 or ny >= n or nx >= m:
                  continue

              if nboard[ny][nx] == 0:
                  nboard[ny][nx] = 2
                  nqueue.append((ny,nx))

      count = 0
      for i in range(n):
          for j in range(m):
              if nboard[i][j] == 0:
                  count += 1

      ret = max(ret, count)


  print(ret)