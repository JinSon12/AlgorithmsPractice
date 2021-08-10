# https://www.acmicpc.net/problem/18870

length = int(input())
nums = list(map(int, input().split()))


# nums = [2, 4, -10, 4, -9]
snums = sorted(set(nums))
# print(snums)

d = {}


for i, v in enumerate(snums):
    if v not in d:
        d[v] = i

for i in nums:
    print(d[i], end=" ")
