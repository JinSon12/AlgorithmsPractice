"""
1475 방 번호 
"""

import math


def findNumSet(num):
    count = [0] * 10
    num = str(num)

    for n in num:
        count[int(n)] += 1

    count69 = math.ceil((count[6] + count[9]) / 2)
    count[6], count[9] = count69, count69

    print(max(count))


findNumSet(input())
