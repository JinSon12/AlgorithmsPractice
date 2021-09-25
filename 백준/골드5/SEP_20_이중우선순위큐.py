""" 
이중 우선순위 큐 

https://www.acmicpc.net/problem/7662

"""
from collections import defaultdict
from collections import deque



import heapq, sys 
input = sys.stdin.readline

N = int(input())

def doublePQ_using_nlargest(m):
  heap = [] 
  heapq.heapify(heap)

  for _ in range(m): 
    operation, val = input().split()
    val = int(val)

    if operation == "I": 
      heapq.heappush(heap, val)

    else: 
      if heap: 
        
        # getting the minval from heap 
        if val == -1:     
          heapq.heappop(heap)

        # getting the maxval from heap 
        else: 
          maxval = heapq.nlargest(1, heap)[0]
          heap.remove(maxval)
    
  if heap: 
      finalMin, finalMax = heapq.heappop(heap), heapq.nlargest(1, heap)[0]
      print(finalMax, finalMin)

  else: 
      print("EMPTY")

def doublePQ(m): 
  minheap, maxheap = [], [] 
  visited = [False] * 1000001
  
  for i in range(m): 
    operation, val = input().split()
    val = int(val)

    if operation == "I": 
      heapq.heappush(minheap, (val, i))       # save val, ind as tuple 
      heapq.heappush(maxheap, ((val * -1), i))
      visited[i] = True
    
    else: 
      if val == -1: 
        while minheap and not visited[minheap[0][1]]: 
          heapq.heappop(minheap)
        
        if minheap: 
          visited[minheap[0][1]] = False
          heapq.heappop(minheap)
      
      else: 
        while maxheap and not visited[maxheap[0][1]]: 
          heapq.heappop(maxheap)
        
        if maxheap: 
          visited[maxheap[0][1]] = False
          heapq.heappop(maxheap)
    
  while minheap and not visited[minheap[0][1]]: 
      heapq.heappop(minheap)
    
  while maxheap and not visited[maxheap[0][1]]: 
      heapq.heappop(maxheap)  
    
  if maxheap and minheap: 
      print(-maxheap[0][0], minheap[0][0])
  else: 
      print("EMPTY")


def usingdict(): 
  for _ in range(N):
      queue = deque()
      ndict = defaultdict(int)
      K = int(input())
      for _ in range(K):
          S, N = input().split()
          N = int(N)
          if S == "I":
              if ndict[N] == 0:
                  bisect.insort_left(queue, N)
              ndict[N] += 1
          elif N == 1:
              if queue:
                  ndict[queue[-1]] -= 1
                  if ndict[queue[-1]] == 0:
                      queue.pop()
          else:
              if queue:
                  ndict[queue[0]] -= 1
                  if ndict[queue[0]] == 0:
                      queue.popleft()

      if queue:
          print(queue[-1], queue[0])
      else:
          print("EMPTY")



for _ in range(N): 
  m = int(input())
  doublePQ(m)

