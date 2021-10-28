# https://www.acmicpc.net/problem/2751

import sys 
input = sys.stdin.readline

N = int(input())
nums = [] 

for i in range(N): 
  nums.append(int(input()))


def orderNumber(nums): 
  nums.sort() 
  for i in range(len(nums)): 
    print(nums[i])

orderNumber(nums)