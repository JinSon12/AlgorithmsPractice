"""
https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/


"""

from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        cnt = 0
        smap = {}
        tmap = {}

        # one map and reduce cnt as we go
        for c in s:
            if c not in smap:
                smap[c] = 1
            else:
                smap[c] += 1

        for c in t:
            if c not in tmap:
                tmap[c] = 1
            else:
                tmap[c] += 1

        for tchar, tfreq in tmap.items():
            s_freq = 0
            if tchar in smap:
                s_freq = smap[tchar]

            if tfreq > s_freq:
                cnt += tfreq - s_freq

        return cnt

    """
    decrease count for freq count of t 
    if s char is present in t 

    what is remaining in the freq count of t 
    would be the chars that needs to be replaced 
    """
    def minSteps_more_optimized(s, t):
        tmap = {}

        for char in t:
            if char not in tmap:
                tmap[char] = 0
            tmap[char] += 1

        for schar in s:
            if schar in tmap:
                tmap[schar] -= 1

        cnt = 0
        for val in tmap.values():
            if val > 0:
                cnt += 1

        return cnt

    def minSteps_counter(s, t):
        tc = Counter(t)
        sc = Counter(s)

        res = 0
        for s_char, freq in sc.items():
            # s_char 의 freq 이 tc 에 있는 것 보다 많으면
            # 즉, tc 에는 s_char 의 숫자가 모자란다
            # 얼마만큼? s_char 만큼 모자란다.
            if freq > tc[s_char]:
                res += freq - tc[s_char]

        return res


stn = Solution()
print(stn.minSteps("bab", "aba"))
