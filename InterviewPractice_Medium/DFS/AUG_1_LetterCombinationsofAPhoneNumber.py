from typing import List


class Solution:
    # 24ms,
    def letterCombinations_recursive(self, digits: str) -> List[str]:
        def dfs(ind, path):

            # dfs 종료 조건
            if len(path) == len(digits):
                res.append(path)
                return

            for i in range(ind, len(digits)):
                for j in d[digits[i]]:
                    dfs(i + 1, path + j)

        if not digits:
            return ""

        res = []

        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        dfs(0, "")  # start with 0th ind of digits, and empty result

        return res

    # faster solution, 12ms
    def letterCombinations_iterative(self, digits: str):
        if not digits:
            return []

        d = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
             "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        output = [""]

        for i in digits:
            temp = []
            for j in d[i]:
                for k in output:
                    temp.append(k + j)
            output = temp

        return output


stn = Solution()
print(stn.letterCombinations_iterative("23"))
