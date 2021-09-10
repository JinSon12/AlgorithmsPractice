"""
듣보잡 

https://www.acmicpc.net/problem/1764


"""
import sys
input = sys.stdin.readline

D, B = map(int, (input().rstrip().split()))

d = set()
b = set()


def findDBJ():
    res = []
    for i in d:
        if i in b:
            res.append(i)

    res.sort()

    print(len(res))
    for el in res:
        print(el)


for _ in range(D):
    d.add(input().rstrip())

for _ in range(B):
    b.add(input().rstrip())

findDBJ()


def faster():
    hear = set()
    see = set()
    for i in range(D):
        s = sys.stdin.readline().strip()
        hear.add(s)
    for i in range(B):
        s = sys.stdin.readline().strip()
        see.add(s)

    result = sorted(list(hear & see))

    print(len(result))
    for r in result:
        print(r)
