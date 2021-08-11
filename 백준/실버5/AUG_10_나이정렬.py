
"""
3
21 Junkyu
21 Dohyun
20 Sunyoung

"""

import sys
input = sys.stdin.readline

num = int(input())

users = []

for _ in range(num):
    users.append(list(input().split()))

# print(users)


# ======

users.sort(key=lambda x: int(x[0]))

for user in users:
    print(user[0], user[1])
