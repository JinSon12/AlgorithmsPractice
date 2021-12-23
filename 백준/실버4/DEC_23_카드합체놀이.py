# https://www.acmicpc.net/problem/15903

import heapq

N, T = map(int, input().split())
nums = list(map(int, input().split()))


def calculateMinScore(nums, tries):
    heapq.heapify(nums)

    for _ in range(tries):
        num1 = heapq.heappop((nums))
        num2 = heapq.heappop((nums))

        add = num1 + num2

        heapq.heappush(nums, add)
        heapq.heappush(nums, add)

    print(sum(nums))


calculateMinScore(nums, T)
