"""
https://www.acmicpc.net/problem/1259

팰린드롬 수. 

"""


def isNumPalindrome(s):
    if len(s) == 1:
        print("yes")
        return

    left = 0
    right = len(s)-1
    while left < right:
        if s[left] == s[right]:
            left += 1
            right -= 1
        else:
            print("no")
            return
    print("yes")


def isNumPalindrome2(s):
    rev = s[::-1]

    if rev == s:
        print("yes")
    else:
        print("no")


inp = input()
while inp != "0":
    isNumPalindrome2(inp)
    inp = input()
