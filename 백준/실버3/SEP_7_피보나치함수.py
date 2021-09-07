"""
피보나치 함수

recursive 한 방식으로 fibonacci 수를 구한다. 
이때, 1, 0 의 호출 횟수를 구하기. 

"""
import sys
input = sys.stdin.readline


N = int(input())


def fibonacci(n):
    dp = [[0, 0] for j in range(n + 1)]

    if n == 0:
        print(1, 0)
        return

    if n == 1:
        print(0, 1)
        return

    dp[0] = [1, 0]  # [count0, count1]
    dp[1] = [0, 1]

    for i in range(2, n+1):
        dp[i] = [0, 0]
        dp[i][0] = dp[i-1][0] + dp[i-2][0]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]

    print(dp[n][0], dp[n][1])


for _ in range(N):
    fibonacci(int(input()))


def fibo_v2():
    T = int(input())

    for i in range(T):
        n = int(sys.stdin.readline())

        L = [[1, 0], [0, 1]]

        for i in range(2, n+1):
            L.append([(L[i-2][0]+L[i-1][0]), (L[i-2][1]+L[i-1][1])])

        print(L[n][0], L[n][1])


# 검산
counter = [0, 0]


def fibonacci(n):
    if n == 0:
        counter[0] += 1
    elif n == 1:
        counter[1] += 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
