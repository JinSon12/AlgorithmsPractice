import math


class Solution(object):
    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        self.res = []

        def dfs(items, n, start):
            if n <= 1 and len(items) > 1:
                self.res.append(items[:])
                return

            till = int(math.sqrt(n)) + 1
            for i in range(start, int(math.sqrt(n))+1):
                if n % i == 0:
                    items.append(i)
                    dfs(items, n//i, i)
                    items.pop()

        dfs([], n, 2)
        return self.res

    # 92ms, 74%
    def getFactors_faster(self, n: int) -> List[List[int]]:
        if n == 1:
            return []

        res = []

        print(int(math.sqrt(n)))

        def dfs(items_soFar, n, start):
            if len(items_soFar) > 0:          # 종료 조건.
                res.append(items_soFar + [n])

            for i in range(start, int(math.sqrt(n)) + 1):
                # print(i, n, items_soFar)
                if n % i == 0:
                    dfs(items_soFar + [i], n // i, i)

        dfs([], n, 2)
        return res


stn = Solution()
stn.getFactors(12)
