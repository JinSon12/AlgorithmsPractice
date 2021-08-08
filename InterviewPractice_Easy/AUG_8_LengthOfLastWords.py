# https://leetcode.com/problems/length-of-last-word/

"""
58. Length of Last Word

Input: s = "Hello World"
Output: 5

# https://stackoverflow.com/questions/62013468/is-there-a-difference-between-split-vs-split

split(), split(" ")
는 다르다. 

hellow    world 
는 split 의 경우 hellow, world
split(" ") 의 경우, hellow, "", "", "", "world" 가 될 것.
"""


class Solution:
    # 28ms, 78%
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()

        return len(s[-1])

    # 12ms, more concise
    def lengthOfLastWord(self, s: str) -> int:
        # strip removes trailing white space.
        # https://www.w3schools.com/python/ref_string_strip.asp
        """
        txt = "     banana     "

        x = txt.strip()

        print("of all fruits", x, "is my favorite")

        """
        return len(s.strip(" ").split(" ")[-1])
