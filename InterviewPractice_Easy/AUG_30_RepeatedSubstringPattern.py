"""
Repeated Substring Pattern 

https://leetcode.com/problems/repeated-substring-pattern/

"""


class Solution:
    # brute force, slow
    def repeatedSubstringPattern(self, s: str) -> bool:
        if len(s) == 1:
            return False

        d = {}

        for char in s:
            if char not in d:
                d[char] = 1
            else:
                d[char] += 1

        subs = ""
        p = 0
        wlen = 0
        subs = ""
        res = True

        for i in range(len(s)):
            subs += s[i]
            wlen += 1
            # print(subs)

            if len(subs) * 2 > len(s):
                return False

            if len(s) % wlen != 0:
                continue

            while p < len(s)+1-wlen:
                # print(p)
                subst = s[p:p+wlen]
                # print(subst, wlen)
                if subst != subs:
                    res = False
                    break

                p += wlen

            if res == True:
                # print(subs)
                return True

            p = 0
            res = True

        return res

    def repeatedSubstringPattern_v1(self, s):
        N = len(s)
        for i in range(1, N//2+1):
            if N % i == 0 and s[:i] * (N//i) == s:
                return True
        return False
