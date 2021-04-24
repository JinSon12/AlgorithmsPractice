class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaString = ""

        # get only alphabet and switch to lowercase
        for char in s:
            if (char.isalnum()):
                alphaString += char.lower()

        # Comparison, compare first with last and so on
        for i in range(0, len(alphaString)//2):
            if(alphaString[i] != alphaString[-i-1]):
                return False

        return True


# Runtime : o(s) or o(n) because we run the for loop o(n) times maximum
