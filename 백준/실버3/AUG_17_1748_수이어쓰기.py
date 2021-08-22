"""
1748. 수 이어 쓰기 
"""

import math


def findLength(num):
    nums = str(num)
    count = 0

    if len(nums) == 1:
        return num

    # 1의 자리 부터 시작해서 원 수의 길이 - 1 만큼
    for i in range(len(nums)-1):
        # 각 자리에서 1의 자리는 1씩 증가, 10의 자리는 1이 증가할때 마다 자리수는 2씩 증가.
        count += 9 * 10**i * (i + 1)

    # 가장 큰 자리로 얻어지는 수의 길이 계산.
    # 원 수에서 앞의 for loop 에서 계산된 자리수 (ie. 1, 10) 만큼 빼주고 + 1
    # 에다 현 자리수에서 만들어지는 수의 갯수 더하기. (100 이면 수의 길이는 3개씩 증가)
    count += (num - 10**(len(nums)-1) + 1) * len(nums)
    print(count)


findLength(int(input()))
