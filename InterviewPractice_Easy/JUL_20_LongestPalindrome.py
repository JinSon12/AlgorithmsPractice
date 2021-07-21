from collections import deque


class Solution:
    # saves the palindrome created.
    # HOWEVER, slower on getting the number itself.
    def longestPalindrome(self, s: str) -> int:
        d = {}
        odd_num_char = ""
        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        for k in d:
            if d[k] % 2 == 1:
                odd_num_char = k
                break

        print(odd_num_char)

        # key => value to sort by (function reference ok)
        sortedKeys = sorted(d, key=d.get, reverse=True)

        occur = 0
        dq = deque([])

        if len(odd_num_char) > 0:
            dq.append(odd_num_char)

        for k in sortedKeys:
            occur = d[k]
            i = 1
            while (i <= occur // 2):
                dq.appendleft(k)
                dq.append(k)
                i += 1

        print(dq)
        return (len(dq))

    # counting the # of occurences more mathematically.
    # faster than v1
    # 28ms, 91.62% time
    def longestPalindrome_v2(self, s: str) -> int:
        d = {}
        odd_num_char = 0

        if len(s) == 1:
            return 1

        for i in s:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        occur = 0
        for k in d.keys():
            if (d[k] % 2 == 0):
                occur += d[k]
            else:
                occur += d[k] - 1
                odd_num_char = 1

        return (occur + 1 if odd_num_char > 0 else occur)
