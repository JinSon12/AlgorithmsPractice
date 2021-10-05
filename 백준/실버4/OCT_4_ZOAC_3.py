"""
ZOAC 3 

https://www.acmicpc.net/problem/20436

"""

import sys 
input = sys.stdin.readline

left, right = input().rstrip().split()
order = input().rstrip()
keys = [["q","w","e","r","t","y","u","i","o","p"], ["a","s","d","f","g","h","j","k","l"], ["z","x","c","v","b","n","m"]]
dkeys = {}

for r in range(len(keys)): 
  for c in range(len(keys[r])): 
    dkeys[keys[r][c]] = [r, c]

# print(dkeys)

def calculateTime(left, right): 
  left_cur_r, left_cur_c = dkeys[left]
  right_cur_r, right_cur_c = dkeys[right]
  res = 0 

  for key in order: 
    dest_r, dest_c = dkeys[key]
    split = 5 
    dist = 0 

    if dest_r == 2: 
      split = 4
    
    # move left 
    if dest_c < split: 
      dist = abs(left_cur_r - dest_r) + abs(left_cur_c - dest_c)
      left_cur_r = dest_r
      left_cur_c = dest_c
    
    else: 
      dist = abs(right_cur_r - dest_r) + abs(right_cur_c - dest_c)  
      right_cur_r = dest_r
      right_cur_c = dest_c

    res += dist + 1   # 1 = 키를 누르는데 걸린 시간 

  print(res)

calculateTime(left, right)


    


    

    


