"""
통계학

첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.

둘째 줄에는 중앙값을 출력한다.

셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.

넷째 줄에는 범위를 출력한다.

"""
import sys
import collections

input = sys.stdin.readline

N = int(input())


def findValues(nums):
    L = len(nums)
    # 산술평균
    sumval = sum(nums)
    avg = round(sumval / N)

    nums.sort()

    # 최빈값
    d = {}
    keys = []
    for n in nums:
        if n not in d:
            d[n] = 1
            keys.append(n)
        else:
            d[n] += 1

    maxKey = 0
    sitems = sorted(d.items(), key=lambda x: (-x[1], x[0]))
    if len(sitems) > 1 and sitems[0][1] == sitems[1][1]:
        maxKey = sitems[1][0]
    else:
        maxKey = sitems[0][0]

    # 범위
    beomwee = nums[L-1] - nums[0]

    # 중앙값
    median_ind = L // 2
    median = nums[median_ind]

    print(avg)
    print(median)
    print(maxKey)
    print(beomwee)


nums = []
for _ in range(N):
    nums.append(int(input()))


findValues(nums)


def findValues_v2():
    n, *m = map(int, open(0))
    m.sort()
    q = collections.Counter(m).most_common(2)*2
    print(*(round(sum(m)/n), m[n//2], q[q[0][1] == q[1][1]][0], m[-1]-m[0]))
