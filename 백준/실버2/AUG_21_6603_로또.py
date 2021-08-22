"""
6603. 로또 

Combinations 문제
조합 문제 

"""
import sys


# 80ms
def findCombination(nums):
    res = []

    def dfs(pathSoFar, start):
        if len(pathSoFar) == 6:   # 종료 조건, recursion depth
            print(*pathSoFar)
            return

        for i in range(start, len(nums)):
            dfs(pathSoFar + [nums[i]], i+1)

    dfs([], 0)

    print(len(res))
    return res


res = []
while True:
    nums = list(map(int, input().split()))

    if nums[0] == 0:
        break

    nums.pop(0)
    findCombination(nums)


"""
res1 = []


def dfs(start, depth):
    # print("level", depth)
    if depth == 6:
        # print("combi", combi)
        res1.append(combi[:6])
        return

    for i in range(start, len(nums)):
        combi[depth] = nums[i]
        dfs(i + 1, depth + 1)


combi = [0 for i in range(13)]

dfs(0, 0)
print("abs", nums)
print(res1)

if res1 == res:
    print("true")
else:
    print("false")
"""
