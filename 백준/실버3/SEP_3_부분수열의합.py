"""

부분 수열의 합 

Bruteforce + backtracking (백트래킹)

Key Insight: 
- 연속된 수열의 합이 아니다. (즉, 1번 인덱스와 3번 인덱스가 혼합되어서 한 부분배열을 이룰 수도 있다)
- 따라서, prefix sum 은 사용할 수 없다. 

- 즉 DFS 사용해야 한다. 

복습
"""


# prefix sum - 조건 : 부분수열은 연속되어야 한다
# ex) [100, 100, 100, -100], k = 0 일때 답은 1.
def countTarget(nums, k):
    ps = {0: 1}
    prev = 0
    total = 0

    for i in range(len(nums)):
        cur = prev + nums[i]
        target = cur - k

        if target in ps:
            total += ps[total]

        ps[cur] = ps.get(cur, 0) + 1
        prev = cur

    return total


def countTarget_dfs(nums, k):
    res = []
    global count
    count = 0

    def dfs(pos, val, pathSoFar):
        global count

        if pos >= len(nums):
            if val == k:
                print(pathSoFar)
                res.append(pathSoFar[:])
                count += 1
            return

        dfs(pos + 1, val + nums[pos],
            pathSoFar + [nums[pos]])
        dfs(pos + 1, val, pathSoFar)

    dfs(0, 0, [])

    return count


print(countTarget_dfs([1, -1, 1, 2], 1))
