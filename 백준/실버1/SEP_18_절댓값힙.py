"""
절대값 힙. 

https://www.acmicpc.net/problem/11286

절댓값 힙은 다음과 같은 연산을 지원하는 자료구조이다.

배열에 정수 x (x ≠ 0)를 넣는다.
배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 
절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

"""
import heapq
import sys
input = sys.stdin.readline

N = int(input())

heap = []
heapq.heapify(heap)

for _ in range(N):
    num = int(input())

    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
        else:
            print(0)

    else:
        heapq.heappush(heap, (abs(num), num))   # abs of num, original_num
