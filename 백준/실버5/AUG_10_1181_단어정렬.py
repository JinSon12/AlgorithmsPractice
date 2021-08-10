"""
13
but
i
wont
hesitate
no
more
no
more
it
cannot
wait
im
yours

"""

# import sys
# input = sys.stdin.readline

num = int(input())

words_set = set()

for _ in range(num):
    words_set.add(str(input()))

# print(words_set)

words = list(words_set)
# ["but", "i", ...]
# print(words)

# =====

words.sort(key=lambda x: (len(x), x))

for word in words:
    print(word)
