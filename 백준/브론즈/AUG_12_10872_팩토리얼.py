def factorial(num):
    if num == 0:
        return 1

    res = 1

    for i in range(num, 1, -1):
        res *= i

    return res


def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1

    res = factorial_recursive(num - 1) * num
    return res


num = int(input())
print(factorial_recursive(num))

# print(factorial_recursive(5))
