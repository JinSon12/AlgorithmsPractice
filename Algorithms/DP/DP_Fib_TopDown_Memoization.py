from functools import lru_cache
import timeit

dp = [0, 1]


def fib(n):
    # memoization 되어 있는 것(저장되어있는 것)을 꺼낸다.
    # n이 실제 저장되어있는 인덱스의 위치와 같거나 그보다 더 작다면,
    # 저장되어 있는 n 값을 꺼낸다. 즉 fib 3의 값을 저장해놓고, 그 값을 꺼내는 것.
    if n <= len(dp)-1:
        return dp[n]

    else:
        temp = fib(n-1) + fib(n-2)
        dp.append(temp)

        return temp


"""
LRU Cache 를 사용한 Memoization 구현. 
따로 배열이 필요하지 않고, 
@lru_cache 데코레이터를 사용해서 연산된 값을 저장한다. 
이를 통해 재귀 함수 구현의 단점인 성능을 대폭 향상할 수 있다. 
"""

# fib_lruCache(50) => 5.41 * e-05


@lru_cache(maxsize=None)
def fib_lruCache(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


start = timeit.default_timer()
fib_lruCache(900)
stop = timeit.default_timer()
print('Time: for lruCache', stop - start)
