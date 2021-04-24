class Solution:
    def isPalindrome(self, s: str) -> bool:
        alphaStr: Deque = collections.deque()

        for char in s:
            if char.isalnum():
                alphaStr.append(char.lower())

        while len(alphaStr) > 1:
            if alphaStr.popleft() != alphaStr.pop():
                return False

        return True

# Runtime O(n) but, at the same time, when we pop(0) in list, it takes O(n)
# as we have to shift elements to the left when we remove the first element.
# whereas with popleft() = o(1)

# HOWEVER, this uses up a lot of memory, because Deque is a structure ?
