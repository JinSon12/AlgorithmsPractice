"""
13419 탕수육 

"""


import sys


def findOrder(s):
    L = repeatTill = len(s)
    p1 = 0
    p2 = 1
    res1 = ""
    res2 = ""

    if L == 1:
        print(s)
        print(s)
        return

    # if the repeated seq. is even in len, then each person needs to memorize L//2 chars.
    if L % 2 == 0:
        repeatTill = L//2

    for _ in range(repeatTill):
        if p1 >= L:
            p1 %= L

        if p2 >= L:
            p2 %= L

        res1 += s[p1]
        res2 += s[p2]

        p1 += 2
        p2 += 2

    print(res1)
    print(res2)
    return


N = int(input())

for _ in range(N):
    s = input()
    findOrder(s)


"""
Shorter, faster concise version 
"""


def faster():
    epoch = int(sys.stdin.readline().rstrip())

    for _ in range(epoch):
        word = sys.stdin.readline().rstrip()
        if len(word) == 1:
            print(word)
            print(word)

        else:
            first = [word for index, word in enumerate(
                word, 1) if index % 2 == 1]
            second = [word for index, word in enumerate(
                word, 1) if index % 2 == 0]

            if len(word) % 2 == 0:
                print(''.join(first))
                print(''.join(second))
            else:
                print(''.join(first)+''.join(second))
                print(''.join(second)+''.join(first))
