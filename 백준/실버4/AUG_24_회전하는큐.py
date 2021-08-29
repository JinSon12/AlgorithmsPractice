"""
1021 회전하는 큐.

복습 요 . 특히 이분검색법의 변형.
"""

import sys
from collections import deque


def findMinCount(nums):
    def removeLeftAndAppendRight(target):
        while q[0] != target:
            q.append(q.popleft())
        q.popleft()

    def removeRightAndAppendLeft(target):
        while q[0] != target:
            t = q.pop()
            q.appendleft(t)

        q.popleft()

    l = [x + 1 for x in range(N)]  # change later
    q = deque(l)
    # M = len(nums)
    nums_pos = 0   # change later
    count = 0

    # for i, v in enumerate(l):
    #     d[v] = [i, N - i - 1]  # dist from left and right

    while nums_pos < M:  # nums 의 마지막 원소이면 중단. 따라서 count <= 3 은 4 까지 될 수 있기때문에 사용하지 않는다.
        if q[0] == nums[nums_pos]:
            q.popleft()
            nums_pos += 1

            # adjusting the distance in dictionary (bug prone?)

        # while q[0] != nums[nums_pos]
        else:
            num = nums[nums_pos]
            dl = q.index(num)
            dr = len(q) - dl

            if dl < dr:
                count += dl
                removeLeftAndAppendRight(num)
                nums_pos += 1
            else:
                count += dr
                removeRightAndAppendLeft(num)
                nums_pos += 1

    return count


N, M = map(int, input().split())
nums = list(map(int, input().split()))
print(findMinCount(nums))


""" 이분탐색의 로직 응용하면 훨씬 더 빨리 풀 수 있다. 78ms """

input = sys.stdin.readline

N, M = map(int, input().split())
arr = list(map(int, input().split()))
queue = [i for i in range(1, N+1)]
answer = 0

for target in arr:
    index = queue.index(target)
    if len(queue)//2 >= index:
        answer += index
    else:
        answer += len(queue) - index
    queue = queue[index + 1:] + queue[:index]

print(answer)
