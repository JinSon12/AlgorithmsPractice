"""
https://www.acmicpc.net/problem/1620

나는야 포켓몬 마스터 이다솜 

목표: 
이름이나 값으로 원하는 포켓몬 찾기. 

사용가능한 자료구조 :
list [pokename] 범위: 0~n+1 
  - 문제: pokename 으로 찾으려고 할때 시간이 많이 걸릴 것. 

두개의 dictionary 사용해서 이름으로도 찾을수 있도록 하기. 
dictionary (pokename, num)


"""
import sys
input = sys.stdin.readline


def findPoke(poke):
    if poke.isalpha():
        print(pokes_name[poke], "ans")
    else:
        poke = int(poke)
        print(pokes[poke], "ans")


N_POKE, Q = map(int, input().split())
pokes = [""]
pokes_name = {}

for i in range(N_POKE):
    mon = input().rstrip()
    pokes.append(mon)
    pokes_name[mon] = i + 1

for _ in range(Q):
    q = input().rstrip()
    findPoke(q)
