class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        ls = list(s)
        left = 0
        right = len(s) - 1

        while left <= right:
            if not ls[left].isalpha():
                left += 1
            if not ls[right].isalpha():
                right -= 1
            elif ls[left].isalpha() and ls[right].isalpha():
                ls[left], ls[right] = ls[right], ls[left]
                left += 1
                right -= 1

        return "".join(ls)
