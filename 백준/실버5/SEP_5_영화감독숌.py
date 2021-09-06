"""
영화 감독 숌 

https://www.acmicpc.net/problem/1436


복습하기.

brute force 를 사용하지 않는 방법으로 구해보기 
"""


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
                print(start)
                count += 1


findNumber(int(input()))
