class Solution:
    def isPalindrome(self, s: str) -> bool:
        alnum = ''.join(chars.lower() for chars in s if chars.isalnum())
        print(alnum[::-1])
        return alnum == alnum[::-1]


stn = Solution()
stn.isPalindrome("ABC123")
