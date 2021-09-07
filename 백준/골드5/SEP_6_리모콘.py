""" 
리모콘

"""
import sys
input = sys.stdin.readline

T = int(input())
num_broken_btns = input()
imposs = set(map(int, input().split()))
possibles = set({0, 1, 2, 3, 4, 5, 6, 7, 8, 9})

for el in imposs:
    if el in possibles:
        possibles.remove(el)

print(possibles, imposs)


def findCount(target):
    # 100 -> num 까지 +, - 버튼으로만 움직이기.
    count = abs(100 - target)

    # 0 ~ 1백만 까지 탐색하여서
    # 이동하는데 필요한 최소한의 클릭 횟수를 구한다.
    # 백만을 범위로 사용하는 이유는, 모든 경우를 고려하기 위해서이다.
    # 예) 1~8 까지의 버튼 고장. 사용할 수 있는 버튼 0,9 일때, 50만번으로 가고싶을때,
    # 결국 90만에서 - 버튼을 사용해서 내려가는 경우나, 100 에서 + 버튼을 사용해서 올라가는 경우 밖에 없다.
    # 즉, 50만을 범위로 고정하면, 5 보다 큰 수의 버튼이 고장났을 때, 그 경우를 탐색할 수 없다.
    for num in range(1000000):
        num = str(num)

        for i in range(len(num)):
            charNum = int(num[i])
            if charNum not in possibles:
                break

            # 어떤 수의 마지막 인덱스까지 (마지막 자릿수 까지) 탐색했고, 그 수의 모든 자릿수의 수가 버튼으로 눌려서 갈 수 있다면,
            elif i == len(num) - 1:
                steps = abs(target - int(num))
                count = min(count, steps + len(num))

    print(count)


findCount(T)


def findCount_v2():
    n = int(input())
    m = int(input())
    A = []
    if m != 0:
        A = list(input().split())

    min_temp = 123456789
    for i in range(1000001):
        TF = True
        for j in A:
            if j in str(i):
                TF = False
                break

        if not TF:
            continue

        if min_temp > abs(n - i):
            min_temp = abs(n-i)
            min_i = i

    if m == 10:
        print(abs(n-100))
    else:
        print(min(min_temp + len(str(min_i)), abs(100-n)))


def sol1107():
    n = int(input())
    m = int(input())
    c = list(str(i) for i in range(10))
    if m > 0:
        for i in input().split():
            c.remove(i)
    if len(c) == 0:
        return abs(n - 100)

    s = len(str(n))
    words = []
    for i in range(len(c)):
        words.append(c[i])
    if c[0] != "0" or len(c) > 1:
        words.append((c[0] if c[0] != "0" else c[1]) + c[0])
    if s > 1:
        words.append("")

    vals = []
    count = 1
    while count < s:
        vals.clear()
        for w in words:
            x = int(w + c[0] * (s - count))
            vals.append((abs(n - x) + len(str(x)), w))
        vals.sort()
        words.clear()
        if len(vals) == 1:
            for i in range(len(c)):
                words.append(vals[0][1] + c[i])
        else:
            for i in range(len(c)):
                words.append(vals[0][1] + c[i])
                words.append(vals[1][1] + c[i])
        count += 1
    vals.clear()
    for w in words:
        x = int(w)
        vals.append(abs(n - x) + len(str(x)))
    return min(abs(n - 100), min(vals))


print(sol1107())
