"""
10773. 제로

"""

n = int(input())

stack = []


def calculate():
    for _ in range(n):
        num = int(input())
        if num == 0:
            stack.pop()

        else:
            stack.append(num)

    return sum(stack)


print(calculate())
