"""
최소 힙

https://www.acmicpc.net/problem/1927

널리 잘 알려진 자료구조 중 최소 힙이 있다. 최소 힙을 이용하여 다음과 같은 연산을 지원하는 프로그램을 작성하시오.

배열에 자연수 x를 넣는다.
배열에서 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

입력에서 0이 주어진 횟수만큼 답을 출력한다.
만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

ex1)
input =
9
0
12345678
1
2
0
0
0
0
32

output =
0
1
2
12345678
0


"""
import sys
import heapq
input = sys.stdin.readline


def findAndOrderDescending():
    arr = []
    pq = []
    N = int(input().rstrip())

    heapq.heapify(pq)

    for _ in range(N):
        inp = int(input().rstrip())

        if inp == 0:
          # 이부분은 이렇게 표현 가능. (el = heapq.heappop(q) if pq else '0')
            if not pq:
                print(0)
            else:
                popEl = heapq.heappop(pq)
                print(popEl)
        else:
            heapq.heappush(pq, inp)


findAndOrderDescending()
