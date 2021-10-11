""" 
크리스마스 선물 

https://www.acmicpc.net/problem/14235
"""
import sys, heapq
N = int(input())

def returnValueOfPresent(): 
  pq = [] 

  for _ in range(N): 
    inp = input()

    if inp == "0": 
      if pq: 
        print(-heapq.heappop(pq))
      else: 
        print(-1)
    
    # 선물 충전소일때 
    else: 
      presents = list(map(int, inp.split()))
      # print(presents)

      for i in range(1, len(presents)): 
        heapq.heappush(pq, -presents[i])

returnValueOfPresent()