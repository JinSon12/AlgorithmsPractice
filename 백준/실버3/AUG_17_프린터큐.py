"""
1966. 프린터 큐
"""

# takes string

import sys
from collections import deque


def findOrder(order, target):
    queue = order
    res = []

    for i in range(len(queue)):
        queue[i] = [queue[i], i]  # priority, initorder

    pointer = 0
    while pointer < len(queue):
        maxVal = max(queue, key=lambda x: x[0])

        if queue[pointer] < maxVal:
            queue.append(queue.popleft())
        else:
            res.append(queue.popleft())

    for i in range(len(res)):
        if res[i][1] == target:
            print(i + 1)


TC = int(input())

for _ in range(TC):
    N, target = list(map(int, input().split()))
    work = deque(map(int, input().split()))

    findOrder(work, target)


##

input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    queue = list(map(int, input().split()))

    cnt = 0
    target = queue[M]
    queue[M] = -1   # 다른 값들과 구분

    while max(queue) > target:
        cnt += 1
        pop = queue.index(max(queue))
        queue = queue[pop+1:] + queue[:pop]
    print(cnt + queue[:queue.index(-1)].count(target) + 1)


###

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    imp = list(map(int, input().split()))
    idx = list(range(len(imp)))
    idx[m] = 'target'

    order = 0

    while True:
        # imp의 첫번째 값 = 최댓값?
        if imp[0] == max(imp):
            order += 1
            # idx의 첫 번째 값 = "target"?
            if idx[0] == 'target':
                print(order)
                break
            else:
                imp.pop(0)
                idx.pop(0)
        else:
            imp.append(imp.pop(0))
            idx.append(idx.pop(0))
