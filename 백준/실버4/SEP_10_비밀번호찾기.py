"""
비밀번호 찾기 

https://www.acmicpc.net/problem/17219

"""
import sys
input = sys.stdin.readline

web_pw = {}


def findPW(name):
    if name in web_pw:
        print(web_pw[name])


N, FIND_COUNT = map(int, input().rstrip().split())

for _ in range(N):
    web_page, pw = input().rstrip().split()
    web_pw[web_page] = pw

for _ in range(FIND_COUNT):
    inp = input().rstrip()
    findPW(inp)
