"""
ATM 

greedy 

"""
import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))


def findMinSum(nums):
    nums.sort()

    total = []
    soFar = 0

    for num in nums:
        soFar += num
        total.append(soFar)

    return sum(total)


print(findMinSum(nums))
