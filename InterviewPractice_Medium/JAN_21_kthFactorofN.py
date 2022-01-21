"""
Kth Factor of N 


"""


def findFactor(N):
    factors = []
    for i in range(1, N + 1):
        if N % i == 0:
            factors.append(i)

    return factors


def findKthFactor(N, k):
    res = findFactor(N)
    print(res)
    return res[k-1] if k-1 < len(res) else -1


print(findKthFactor(10, 3))
print(findKthFactor(12, 3))
print(findKthFactor(7, 2))
