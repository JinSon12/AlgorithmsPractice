"""
Find All Anagrams in String

https://leetcode.com/problems/find-all-anagrams-in-a-string/

https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/92007/Sliding-Window-algorithm-template-to-solve-all-the-Leetcode-substring-search-problem.

"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        word = [0] * 26

        for char in p:
            pos = ord(char) - 97
            word[pos] += 1

        L = len(p)
        start = 0

        temp = [0] * 26
        res = []
        while start < len(s):
            char = s[start]
            pos = ord(char) - 97

            temp[pos] += 1

            if temp == word:
                res.append(start - L + 1)

            # 이전 연습했던 permutation in string 의 코드보다 훨씬 더 간결하다.
            if start + 1 >= L:
                prevChar = s[start - L + 1]
                prev_pos = ord(prevChar) - 97

                temp[prev_pos] -= 1

            start += 1

        return res

    def findAnagrams_v2(self, s: str, p: str) -> List[int]:
        k = len(p)
        dic1 = [0]*26
        dic2 = [0]*26
        ans = []

        for ch in p:
            dic1[ord(ch)-ord("a")] += 1

        for ch in s[:k-1]:
            dic2[ord(ch)-ord("a")] += 1

        for i, ch in enumerate(s[k-1:]):
            dic2[ord(ch)-ord("a")] += 1

            if dic1 == dic2:
                ans.append(i)

            dic2[ord(s[i])-ord("a")] -= 1

        return ans
