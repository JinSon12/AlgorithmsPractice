"""
실버 1.
2447 별찍기 - 10

재귀


- zip(): 각 리스트에서 같은 위치에 있는 원소들끼리 묶어줌. 

"""


import sys


def concatenate(v1, v2):
    return ["".join(x) for x in zip(v1, v2, v1)]


def recurse(n):
    if n == 1:
        return ["*"]

    n //= 3

    valSoFar = recurse(n)

    top_bottom = concatenate(valSoFar, valSoFar)
    middle = concatenate(valSoFar, [" " * n] * n)

    return top_bottom + middle + top_bottom


print("\n".join(recurse(9)))

# method 2
sys.setrecursionlimit(10**6)


def recursively_add(n):
    if n == 1:
        return ["*"]

    valSoFar = recursively_add(n // 3)

    res = []

    for s in valSoFar:
        res.append(s * 3)

    for s in valSoFar:
        res.append(s * (n//3) + " " * (n // 3) + s * (n // 3))

    for s in valSoFar:
        res.append(s * 3)

    return res
