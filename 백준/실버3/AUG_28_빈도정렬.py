"""
빈도 정렬 

- dictionary 사용
- K (num): V (freq, ind, num)
- v 만 빼내서 정렬 

Important: 
The important difference is that tuples are immutable. 
Tuples are also comparable and hashable, 
so we can sort lists of them and use tuples as key values in Python dictionaries.

파이썬 mutable 객체 : list, dictionary 
immutable 객체: int, string, tuple 이 있다. (이들은 값이 변경될 때, 객체가 변한다. 즉, 기존 객체는 변하지 않고, 새로운 객체가 생성된다; 따라서 주소값도 새로이 받는다)
"""

N, C = map(int, input().split())
nums = list(map(int, input().split()))


def freqSort(nums):
    d = {}
    res = []

    for ind, num in enumerate(nums):
        if num not in d:
            d[num] = [1, ind, num]
        else:
            d[num][0] += 1

    items = list(d.values())

    items.sort(key=lambda x: (-x[0], x[1]))

    for i in items:
        freq, _, item = i
        res += [item] * freq

    print(*res)


# 백준
# https://www.acmicpc.net/source/32067733
def freqSort_v2(L):
    data, dic = [], {}
    for l in L:
        if l not in dic:
            data.append(l)
            dic[l] = 0
        dic[l] += 1
    result = []
    for i, d in enumerate(data):
        result.append([dic[d], N-i, d])
    result.sort(reverse=True)
    for r in result:
        print(f"{r[2]} "*r[0], end='')

# 복습해보기.


def freqSort_v3(arr):
    res = []

    freq = {}
    for i in arr:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1

    res = sorted(freq.items(), key=(lambda x: x[1]), reverse=True)  # 이 로직.

    for i in range(len(res)):
        for j in range(res[i][1]):
            print(res[i][0], end=' ')


freqSort(nums)
