"""
DP 
Sliding Window problem 

Key Insight:
- Two approaches 
1) sliding windows (2 length, and 3 length)
2) DP 
"""


class Solution:
    # 260ms (93.64), 14.2mb (83.28%)
    def longestPalindrome_slidingWindow(self, s: str) -> str:
        def palcheck(left, right):
            while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1: right]

        if len(s) < 2 or s == s[::-1]:
            return s

        res = ""
        # make the for loop stop at last ind -2
        for i in range(len(s) - 1):
            # string 도 max 사용 가능. 단, 이 경우에는 반드시 key = len 을 주어야 한다.
            # 아니면 가장 큰 값 (순서)을 가진 ***철자가*** return 된다.
            res = max(res, palcheck(i, i + 1), palcheck(i, i + 2), key=len)

    # 56ms
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or s == s[::-1]:
            return s
        else:

            start = 0
            maxlen = 1

            for i in range(1, len(s)):
                odd = s[i-maxlen-1:i+1]
                even = s[i-maxlen:i+1]

                if i-maxlen-1 >= 0 and odd == odd[::-1] and len(odd) > maxlen:
                    start = i-maxlen-1
                    maxlen = len(odd)

                if i-maxlen >= 0 and even == even[::-1] and len(even) > maxlen:
                    start = i-maxlen
                    maxlen = len(even)

            return s[start:start+maxlen]
