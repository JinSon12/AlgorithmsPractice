"""
11047. 동전 0

https://www.acmicpc.net/problem/11047

준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.

동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다. 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.

10 4200
1
5
10
50
100
500
1000
5000
10000
50000

=> 6

KEY Insight: 
- Greedy Algorithm; b/c each coin is a multiple of the previous coin. 

그리디를 사용할 수 없는 경우: 
target = 800 
동전 종류 : 
500
400
100 

"""

import sys
input = sys.stdin.readline

N, target = map(int, input().strip().split())

coins = [int(input()) for _ in range(N)]


def numberOfChange(coins, target):
    number = 0

    for i in range(len(coins)-1, -1, -1):
        coin = coins[i]

        # while 은 시간 초과
        # while target - coin >= 0:
        #     number += 1
        #     target -= coin
        #     break

        count, rem = divmod(target, coin)
        number += count
        target = rem

    return number


print(numberOfChange(coins, target))
