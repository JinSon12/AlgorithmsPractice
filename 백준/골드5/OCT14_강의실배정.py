"""
강의실 배정 


"""
import heapq, sys 
input = sys.stdin.readline

N = int(input())
classes = [] 

for i in range(N): 
  start, end = map(int, input().rstrip().split())
  classes.append([start, end])

classes.sort(key=lambda x: x[0])

# 512ms
def assignRooms(): 
  roomPQ = [] 
  heapq.heappush(roomPQ, classes[0][1]) # 종료 시간을 사용한다. 

  for i in range(1, N): 
    curClassEndTime = roomPQ[0]
    nextClassStartTime = classes[i][0]

    # 현재 수업이 다음 수업의 시작시간보다 늦게 끝난다면, 
    # 수업중인 강의실 1 추가 후 강의가 끝나는 순서대로 우선순위큐를 사용해서 정렬
    if curClassEndTime > nextClassStartTime: 
      heapq.heappush(roomPQ, classes[i][1])
    
    # 현재 강의실 바로 다음에 추가로 강의 가능한 경우 
    # 현재 강의실의 끝나는 시간을 변경하기 위해서 
    # 현재 강의 종료 시간을 pop 후 새로운 강의 종료 시간을 push 한 후 (우선순위큐로 다시 정렬)
    else: 
      heapq.heappop(roomPQ)
      heapq.heappush(roomPQ, classes[i][1])
  
  print(len(roomPQ))

assignRooms()

# 380
def assignRooms2(): 
  schedules = [tuple(map(int, input().split())) for _ in range(N)]
  heap = [0]

  for s, t in sorted(schedules):
      if heap[0] <= s:
          heapq.heappop(heap)
      heapq.heappush(heap, t)

  print(len(heap))