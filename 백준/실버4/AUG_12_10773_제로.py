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


def faster():
    from sys import stdin
    input()

    l = []
    for i in map(int, stdin):
        l.append(i) if i else l.pop()

    print(sum(l))
