""" 
lru_cache 를 사용하면, memoization 이 파이썬 내부에서 사용되어 속도가 빠르게 구현된다. 

"""


from functools import lru_cache


def numRollsToTarget(n, k, target):
    @lru_cache(maxsize=None)
    def dfs(diceNum, numLeft):
        # 마지막 주사위 일때,
        # numLeft 가 0 이면, 마지막 주사위를 던졌을때
        if diceNum == n:
            if numLeft == 0:
                return 1
            else:
                return 0

        # 굴릴수있는 주사위 갯수에서 한 번 추가한 주사위에서 더 굴리거나 (즉 3개가 최종이면, 4개를 굴려버리고, 이렇게 되면 음수가 나온다)
        # 혹은, 굴릴 수 있는 주사위 갯수에서 너무 큰 숫자가 나와서 총 수의 합이 찾아야 하는 수를 넘어버린 것.
        elif numLeft < 0:
            return 0

        count = 0
        for diceFaceNum in range(1, k + 1):
            toAddMore = dfs(diceNum + 1, numLeft - diceFaceNum)
            count = (count + toAddMore) % (10**9 + 7)

        return count
    return dfs(0, target)


print(numRollsToTarget(1, 6, 3))
