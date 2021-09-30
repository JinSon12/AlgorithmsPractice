""" 
봄버맨

https://www.acmicpc.net/problem/16918

"""
import sys 
input = sys.stdin.readline

R, C, S = map(int, input().rstrip().split())

grid = [list(input().rstrip()) for _ in range(R)]
bt = [[0 for _ in range(C)] for _ in range(R)] 
dirs = [[1, 0], [-1, 0], [0, -1], [0,1]]

def addbomb(s): 
  for i in range(R): 
    for j in range(C): 
      if grid[i][j] == ".": 
        grid[i][j] = "O"
        bt[i][j] = s + 3  # 3 초 뒤에 터진다.  

def detonate(s): 
  for i in range(len(bt)): 
    for j in range(len(bt[0])): 
      if bt[i][j] == s:
        grid[i][j] = "."
        bt[i][j] = 0 

        # 주변의 폭탄 터뜨리기. 
        for x, y in dirs: 
          newr = i + y 
          newc = j + x 

          # 마지막 조건이 중요하다. 
          # 마지막 조건이 없다면, 옆에 설치되어 잇는 폭탄까지 없애버리는데, 이때 없어진 폭탄의 주변 폭탄을 삭제할 수없게 되어버린다. 
          if 0 <= newr < len(grid) and 0 <= newc < len(grid[0]) and bt[newr][newc] != s: 
            grid[newr][newc] = "."
            bt[newr][newc] = 0  

def setInitialTimer(): 
  for i in range(R):
    for j in range(C): 
      if grid[i][j] == "O": 
        bt[i][j] = 3  # 첫번째 폭탄은 3 초에 터진다. 

def printBoard(): 
  for i in range(R): 
    for j in range(C):
      print(grid[i][j], end="")
    print()

for s in range(1, S+1): 
  if s == 1: 
    setInitialTimer() 

  elif s % 2 == 0: 
    addbomb(s) 

  elif s % 2 != 0: 
    detonate(s) 

printBoard()