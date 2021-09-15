"""
접두사 찾기

Key Insight: 
- bisect_left 를 사용해서 이분 탐색 구현, startswith

- 이분탐색을 사용하여서 NW 에서 빠르게 현재 단어를 검색한다. 
- 이것은 기존의 brute force 탐색이 걸리는 O(n) 시간을 O(log n) 시간으로 빨리 단축시킬 수 있다.
"""

from bisect import bisect_left
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
NW = []
MW = []

for _ in range(N):
    NW.append(input().rstrip())

for _ in range(M):
    MW.append(input().rstrip())


def findPrefix():
    # sort the N alphabetically, so that we can utilize binary search
    # n log n
    NW.sort()
    print(NW)

    counter = 0

    # find words from N that starts with the same character as each word in M
    for word in MW:
        # binary search in N
        wordLen = len(word)

        for nword in NW:
            if word == nword[:wordLen]:
                print(word, nword[:wordLen])
                counter += 1
                break

    print(counter)


# 이분탐색을 응용한 버젼
def findPrefix_binarySearch():
    NW.sort()
    # print(NW)

    counter = 0

    for word in MW:
        wordLen = len(word)
        left = 0
        right = N - 1
        mid = right // 2

        while left <= right:
            wordMid = NW[mid]

            if wordMid < word:
                left = mid + 1
                mid = (left + right) // 2

            else:
                right = mid - 1
                mid = (left + right) // 2

            if left < len(NW) and NW[left][:wordLen] == word:
                counter += 1
                break

        # print(word, NW[left], right, mid)
        # left = word 와 가장 가까운 단어
    print(counter)


findPrefix_binarySearch()


"""
모범 답안 

"""
# 접두사 찾기


def solve(corpus, texts):
    corpus = sorted(corpus)
    count = 0
    for text in texts:
        idx = bisect_left(corpus, text)
        # bisect_left 를 사용해서 이분 탐색 구현, startswith
        if idx < len(corpus) and corpus[idx].startswith(text):
            count += 1
    return count


def main():
    stdin = sys.stdin
    N, M = [int(x) for x in stdin.readline().split()]
    corpus = [stdin.readline().strip() for _ in range(N)]
    texts = [stdin.readline().strip() for _ in range(M)]
    print(solve(corpus, texts))


if __name__ == "__main__":
    main()
