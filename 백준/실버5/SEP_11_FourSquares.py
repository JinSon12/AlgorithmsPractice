"""
Four Squares

https://www.acmicpc.net/problem/17626

"""
import sys


N = int(input())
dp = [0] * (N + 1)
dp[1] = 1

for i in range(2, n+1):
    min_val = n + 2

    j = 1
    while j * j <= i:
        min_val = min(min_val, dp[i - j * j])
        j += 1

    dp[i] = min_val + 1

print(dp[N])


def solve(n):
    if int(n ** 0.5) ** 2 == n:
        return 1
    ar = []
    for i in range(1, int((n // 2) ** 0.5) + 1):
        for j in range(1, int((n - i ** 2) ** 0.5) + 1):
            if i ** 2 + j ** 2 == n:
                return 2
            elif (n - i ** 2 - j ** 2) ** 0.5 % 1 == 0:
                ar.append(3)
            else:
                ar.append(4)
    return min(ar)


print(solve(int(input())))


def solution_3():
    import sys
    import math

    s = sys.stdin.readline()
    N = int(s)

    min_cnt = 4

    def find_result(N, cnt):
        global min_cnt
        if N == 0:
            if cnt < min_cnt:
                min_cnt = cnt
            return
        if cnt >= min_cnt:
            return

        snum = int(math.sqrt(N))
        enum = int(math.sqrt(N/2))
        for i in range(snum, enum-1, -1):
            find_result(N - i*i, cnt+1)

    find_result(N, 0)

    print(min_cnt)


def solution_4():
    n = int(input())
    min_sum = 4  # 최대는 4라고 증명되어있다, 아래 3중 for문에서 걸리지 않는다면 답은 4
    for a in range(int(n**0.5), int((n//4)**0.5), -1):  # 가능한 최소한의 범위로 축소해준다
        if a*a == n:
            min_sum = 1  # 최소의 숫자일 경우
            break
        else:
            temp = n - a*a
            for b in range(int(temp**0.5), int((temp//3)**0.5), -1):  # 남은 숫자는 3이니까 3으로 나누어줌
                if a*a + b*b == n:
                    min_sum = min(min_sum, 2)
                    continue
                else:
                    temp = n - a*a - b*b
                    for c in range(int(temp**0.5), int((temp//2)**0.5), -1):
                        if n == a*a + b*b + c*c:
                            min_sum = min(min_sum, 3)

    print(min_sum)
