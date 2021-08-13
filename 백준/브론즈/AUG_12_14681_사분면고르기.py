"""
https://www.acmicpc.net/problem/14681

14681 사분면 고르기

"""

x = int(input())
y = int(input())


def quadrant(x, y):
    if x > 0 and y > 0:
        return 1
    elif x > 0 and y < 0:
        return 4
    elif x < 0 and y < 0:
        return 3
    else:
        return 2


print(quadrant(x, y))
