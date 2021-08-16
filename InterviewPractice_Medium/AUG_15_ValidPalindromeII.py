
"""
Valid Palindrome II 


"""


class Solution:
    # brute force solution - Timeout
    def validPalindrome(self, s: str) -> bool:
        def palindromeCheck(ns):
            left, right = 0, len(ns) - 1

            while left <= right:
                if ns[left] == ns[right]:
                    # print(ns[left], ns[right])
                    left += 1
                    right -= 1

                else:
                    return False

            return True

        # first check if the string is palindrome or not.
        # if not, proceed, if it is return True
        if palindromeCheck(s):
            return True

        for i in range(len(s)):
            ns = s[:i] + s[i+1:]

            res = palindromeCheck(ns)

            if res:
                return True

    # 160 ~ 168ms,
    # O(len(s)), space: O(1)
    def validPalindrome_v2(self, s: str) -> bool:
        # check one more time,
        # if there is still an unmatching string, return False.
        def removeOne(ns, l, r):
            while l <= r:
                if ns[l] == ns[r]:
                    l += 1
                    r -= 1

                else:
                    return False

            return True

        def palindromeCheck(ns):
            left, right = 0, len(ns) - 1

            while left <= right:
                if ns[left] == ns[right]:
                    left += 1
                    right -= 1

                else:

                    if removeOne(ns, left + 1, right) or removeOne(ns, left, right - 1):
                        return True

                    else:
                        return False

            return True

        # first check if the string is palindrome or not.
        # if not, proceed, if it is return True
        if palindromeCheck(s):
            return True

    # O(len(s)), space: O(len(s)) - due to list slicing
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Time: O(n)
        # Space: O(n)
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True

    # concise, fastest,
    # O(len(s)), space: O(len(s))
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]:
            return True

        left = 0
        right = len(s) - 1

        while s[left] == s[right]:
            left += 1
            right -= 1

        # 여기서부터 s[left] != s[right]
        new_s = s[left+1:right+1]   # left + 1, right
        if new_s == new_s[::-1]:
            return True

        new_s = s[left:right]       # left, right - 1
        if new_s == new_s[::-1]:
            return True

        return False
