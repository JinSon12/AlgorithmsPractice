"""
15565. 귀여운 라이언 

꿀귀 라이언 인형과, 마찬가지로 꿀귀인 어피치 인형이 N개 일렬로 놓여 있다. 라이언 인형은 1, 어피치 인형은 2로 표현하자. 
라이언 인형이 K개 이상 있는 가장 작은 연속된 인형들의 집합의 크기를 구하여라.
K개 이상의 라이언 인형을 포함하는 가장 작은 연속된 인형들의 집합의 크기를 출력한다. 그런 집합이 없다면 -1을 출력한다.

첫 줄에 N과 K가 주어진다. (1 ≤ K ≤ N ≤ 10^6)

둘째 줄에 N개의 인형의 정보가 주어진다. (1 또는 2)

10 3
1 2 2 2 1 2 1 2 2 1
답 : 6 
"""
from collections import deque
import sys

input = sys.stdin.readline

# using deque
# N, k = map(int, input().split())
# nums = list(map(int, input().split()))

nums = [1, 2, 2, 2, 1, 2]
k = 5


def findMinimumCount_deque(nums, k):
    d = deque([])
    minLen = len(nums) + 1
    count1 = 0

    for i in range(len(nums)):
        d.append(nums[i])

        if nums[i] == 1:
            count1 += 1

        if count1 >= k:     # if we have desired # of count of 1
            # update the maxLen of the total count of stuffed animals.
            # print(minLen, len(d), print(d))
            minLen = min(minLen, len(d))

            d.popleft()

            while d and d[0] != 1:  # popleft from deque until we see 1.
                d.popleft()

            count1 -= 1

    if minLen != N + 1:
        print(minLen)
        return minLen
    else:
        print(-1)
        return -1


def findMinimumCount_tp(nums, k):
    inds = []
    minLen = len(nums) + 1
    p = 0

    for i, v in enumerate(nums):
        if v == 1:
            inds.append(i)

    while p + k - 1 < len(inds):
        first = inds[p]
        last = inds[p + k - 1]

        count = last - first + 1
        minLen = min(minLen, count)

        p += 1

    if minLen != len(nums) + 1:
        print(minLen)
    else:
        print(-1)


def fastandConcise(nums, k):
    if nums.count('1') < k:
        print(-1)
    else:
        lion = [i for i, x in enumerate(nums) if x == '1']

        print(min(
            lion[k - 1 + j] - lion[j] + 1 for j in range(len(lion)-k+1))
        )


findMinimumCount_tp(nums, k)
