"""
최대힙 

배열에 자연수 x를 넣는다.
배열에서 가장 큰 값을 출력하고, 그 값을 배열에서 제거한다.
프로그램은 처음에 비어있는 배열에서 시작하게 된다.

첫째 줄에 연산의 개수 N(1 ≤ N ≤ 100,000)이 주어진다. 
다음 N개의 줄에는 연산에 대한 정보를 나타내는 정수 x가 주어진다. 
만약 x가 자연수라면 배열에 x라는 값을 넣는(추가하는) 연산이고, 
x가 0이라면 배열에서 가장 큰 값을 출력하고 그 값을 배열에서 제거하는 경우이다. 
입력되는 자연수는 231보다 작다.

"""
import sys
import heapq
input = sys.stdin.readline

N = int(input())
heap = []
heapq.heapify(heap)

for _ in range(N):
    num = int(input())
    if num == 0:
        if heap:
            print(heapq.heappop(heap)[1])
            # 혹은
            # print(heapq.heappop(heap) * -1)
        else:
            print(0)

    else:
        heapq.heappush(heap, (-num, num))
        # 혹은
        # heapq.heappush(heap, -num)
