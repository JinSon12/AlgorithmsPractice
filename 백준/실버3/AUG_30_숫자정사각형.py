"""
https://www.acmicpc.net/problem/1051

숫자 정사각형. 

"""


import generateRandom

import sys
input = sys.stdin.readline

R, C = map(int, input().split())
nums = []

for _ in range(R):
    nums.append([int(x) for x in input().rstrip()])

print(nums)


def findLargestSquare(nums):
    smallerLength = min(R, C)
    size = 0

    for i in range(len(nums)-1):
        for j in range(len(nums[0])-1):
            num = nums[i][j]
            for k in range(1, smallerLength):
                if i + k < len(nums) and j + k < len(nums[0]):
                    # print(i, j, i + k, j + k, "com")
                    if num == nums[i+k][j] and num == nums[i][j+k] and num == nums[i+k][j+k]:
                        # print(i, j, i+k, j+k)
                        size = max(size, k)
                        # print(size)

    return (size+1) * (size+1)


# randGrid = generateRandom.generate2D(5, 5, 5)
# print(randGrid, "grid")
print(findLargestSquare((nums)))


def fasterSearch(nums):
    def search(s):
        for i in range(n-s+1):
            for j in range(m-s+1):
                if nums[i][j] == nums[i][j+s-1] == nums[i+s-1][j] == nums[i+s-1][j+s-1]:
                    return True

        return False

    if n > m:
        size = m
    else:
        size = n

    for k in range(size, 0, -1):
        if search(k):
            print(k**2)
            break
