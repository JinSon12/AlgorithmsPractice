import timeit

# runtime 1.58 * e -5


def fib(n):
    dp = [j for j in range(n + 1)]

    # dp 배열의 초기값은 [0, 1, 2, 3, 4, 5 ... n] 으로 되어있다.
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


start = timeit.default_timer()
fib(50)
stop = timeit.default_timer()
print('Time: for dp', stop - start)
