"""
영화 감독 숌 

https://www.acmicpc.net/problem/1436


복습하기.

brute force 를 사용하지 않는 방법으로 구해보기 
"""


import sys


def findNumber(n):
    if n == 1:
        print(666)
        return

    if n > 1:
        count = 1
        start = 666
        while count != n:
            start += 1
            if '666' in str(start):
                count += 1

        print(start)


findNumber(int(input()))


def main():
    n = int(sys.stdin.readline())

    lst = list(range(10000))
    set_lst = set()
    for i in lst:
        x = str(i).zfill(4)
        for j in range(5):
            y = x[:j]+"666"+x[j:]
            set_lst.add(int(y))

    print(sorted(list(set_lst))[n-1])


if __name__ == "__main__":
    main()
