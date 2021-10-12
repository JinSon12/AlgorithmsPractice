"""
센티와 마법사 뿅망치 

https://www.acmicpc.net/problem/19638

주의 할 점 : 
모든 거인이 작을때, 최소 때린 횟수를 구해야 한다. 

"""
import sys, heapq, math
input = sys.stdin.readline

NG, HC, TRY = map(int, input().rstrip().split())


def printResultAfterHitWithMangchi(): 
  res = [] 

  for _ in range(NG): 
    height = int(input().rstrip())
    res.append(height * -1)

  heapq.heapify(res)

  cnt = 0 
  for i in range(1, TRY + 1): 
    tallest = heapq.heappop(res) * -1

    if tallest < HC: 
      heapq.heappush(res, tallest)
      break 

    newHeight = 0 
    if tallest == 1: 
      newHeight = 1 

    else: 
      newHeight = math.floor(tallest // 2)
      cnt += 1 

    heapq.heappush(res, newHeight * -1)

  maxVal = min(res) * -1
  if maxVal >= HC: 
    print("NO")
    print(maxVal)
  else: 
    print("YES")
    print(cnt)



printResultAfterHitWithMangchi()

def v2():
  N, H, T = map(int, input().split())
  height = sorted(map(lambda x: -int(x), sys.stdin))

  for t in range(T):
      if -height[0] < H:
          print(f"YES\n{t}")
          break

      h = -heapq.heappop(height)
      if h > 1:
          h //= 2
      heapq.heappush(height, -h)

  else:
      if -height[0] < H:
          print(f"YES\n{T}")
      else:
          print(f"NO\n{-height[0]}")