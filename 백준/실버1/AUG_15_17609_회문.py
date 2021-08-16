"""
17609. 회문 Palindrome 

Key Insight : 
Two approaches: 

- Selective Recursion, Time: O(n), Space: O(1)
  - recur again but with skipping either left or right index. 

- List Slicing, Time: O(n), Space: O(n), but much faster than selective recursion
  due to list slicing, which is internally implemented using C in python 
  - similar to selective recursion, but uses extra memory space to save the sliced result. 

"""


def v2_listSlicing():
    def isValidPalindrome(s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                # almost palindrome
                # alternatively, can use list slicing.
                ns_l = s[left + 1: right + 1]
                ns_r = s[left: right - 1]

                if ns_l == ns_l[::-1] or ns_r == ns_r[::-1]:
                    return 1

                # no palindrome
                else:
                    return 2

        return 0

    N = int(input())

    for _ in range(N):
        s = input()
        print(isValidPalindrome(s))

    # print(isValidPalindrome("summuus"))


def v1_selectiveRecursion():
    def removeOne(ns, l, r):
        left, right = l, r

        while left < right:
            if ns[left] == ns[right]:
                left += 1
                right -= 1

            else:
                return False

        return True

    def isValidPalindrome(s):
        left, right = 0, len(s) - 1

        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1

            else:
                # almost palindrome
                # alternatively, can use list slicing.
                if removeOne(s, left + 1, right) or removeOne(s, left, right - 1):
                    return 1

                # no palindrome
                else:
                    return 2

        return 0

    N = int(input())

    for _ in range(N):
        s = input()
        print(isValidPalindrome(s))
