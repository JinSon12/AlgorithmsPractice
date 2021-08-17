"""
1157. 단어 공부 

"""
from collections import Counter


def countLetters_counter(s):
    if len(s) == 1:
        print(s.upper())
        return

    counter = Counter(s.lower())

    res = counter.most_common(2)

    if res[0][1] == res[1][1]:
        print("?")
    else:
        print(res[0][0].upper())


def countLetters_count(s):
    s = s.lower()

    uniq_chars = set(s)
    counter = []

    for c in uniq_chars:
        counter.append([s.count(c), c])

    count = 0
    maxOccur = max(counter)
    for el in counter:
        if el[0] == maxOccur[0]:
            count += 1

    if count > 1:
        print("?")

    else:
        print(maxOccur[1].upper())


def countLetters_count_v2():
    string = input().lower()
    alphabet = list(set(string))

    cnt = [string.count(i) for i in alphabet]
    highest = max(cnt)

    if cnt.count(highest) != 1:
        print("?")

    else:
        print(cnt)
        index = cnt.index(highest)
        print(index)
        print(alphabet[index].upper())


# countLetters_count(input())
countLetters_count_v2()
