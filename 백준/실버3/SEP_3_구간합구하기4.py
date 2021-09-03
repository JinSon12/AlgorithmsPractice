"""
https://www.acmicpc.net/problem/11659

구간 합 구하기 4

map = iterable의 각 element 에 함수를 적용시킨다. 약간 for each.

Key Insight:
- 일종의 메모이제이션을 사용한다 (prefix sum array)

O(N+M)

"""

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
nums = list(map(int, input().split()))


# 기본적인 누적합 (prefix sum) 구하는 방법.
def findPrefixSum(nums):
    ps = []
    sumSoFar = 0

    for i in range(len(nums)):
        sumSoFar += nums[i]
        ps.append(sumSoFar)

    return ps


# 이 경우에는 처음부터 현재 숫자의 앞 (i.e. [0, 3)) 까지 구해서 저장한다.
# 또한 이 문제에서 사용하기에 적합하다. (문제에서 구하는 1번째 숫자 ~ 3번째숫자 = 0 ~ 2번 인덱스까지의 누적합.)
# 이유 : index 1 부터 첫번째 원소의 누적합을 구하기 때문이다~
def findPrefixSum_modified(nums):
    ps = [0]
    sumSoFar = 0

    for i in range(len(nums)):
        ps.append(sumSoFar + nums[i])  # 앞에 있는 것에 현재 것을 더해주고
        sumSoFar += nums[i]            # 누적합 값을 업데이트 한다.

    return ps


ps = findPrefixSum_modified(nums)

for i in range(M):
    start, end = map(int, input().split())
    print(ps[end] - ps[start-1])


def memoizationWay(nums):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    memo = [0]*(n+2)
    memo[1] = a[0]

    for i in range(2, n+1):
        memo[i] = memo[i-1]+a[i-1]

    for _ in range(m):
        i, j = map(int, input().split())
        print(memo[j]-memo[i-1])
