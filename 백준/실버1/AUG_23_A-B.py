"""
16953 A -> B 

숫자 A 에서 B 만드는 최소한의 연산 값을 구하기.

가능한 연산은 2가지
1) 2곱하기
2) 1 을 수의 가장 오른쪽에 추가하기.

BFS 
time complexity O(2^n)
"""
from collections import deque


def findMinNum(num, target):
    q = deque([num])
    steps = 0

    while q:
        steps += 1

        for _ in range(len(q)):
            n = q.popleft()
            if n == target:
                return steps

            # print(n)

            multiply = n * 2
            addOne = n * 10 + 1

            if multiply <= target:
                q.append(multiply)

            if addOne <= target:
                q.append(addOne)

    return -1


num, target = map(int, input().split())

print(findMinNum(num, target))


def findMinNum_recursion():
    A, B = map(int, input().split())
    INF = 1e9 + 7

    def func(x, c):
        if x == B:
            return c
        elif x > B:
            return INF
        else:
            return min(func(x*2, c + 1), func((x*10)+1, c + 1))

    ans = func(A, 0)
    print(ans == INF and -1 or ans + 1)


def findMin_simple():
    a, b = map(int, input().split())

    cnt = 0
    while b > a:
        if str(b)[-1] == '1':
            b = int(str(b)[:-1])
        else:
            if b % 2 != 0:
                break
            b //= 2
        cnt += 1

    if a == b:
        print(cnt+1)
    else:
        print(-1)
