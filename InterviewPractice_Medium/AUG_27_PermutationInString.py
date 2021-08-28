"""
https://leetcode.com/problems/permutation-in-string/

Permutation In String 


"""

from collections import defaultdict


class Solution:

    # very slow, O(n^2)
    def checkInclusion_v1(self, s1: str, s2: str) -> bool:
        win_start = 0
        win_len = len(s1)
        # win_end = win_start + win_len
        sorteds1 = (sorted(list(s1)))

        # print(sorteds1)
        for i in range(len(s2) - win_len + 1):
            chars = s2[i:i + win_len]
            listChars = sorted(list(chars))
            # print(listChars, sorteds1)

            if sorteds1 == listChars:
                return True

        return False

    # single pass O(n) sliding window
    # 76ms, 50%
    def checkInclusion_v2(self, s1: str, s2: str) -> bool:
        win_start = 0
        win_len = len(s1)
        win_end = win_start + win_len

        s1d = [0] * 26
        s2d = [0] * 26

        for char in s1:
            s1d[ord(char)-97] += 1

        # subtract from the hashs1
        # if elements in hashs1 == 0
        while win_start < len(s2):
            # add char to s2d hash
            char_to_add = ord(s2[win_start]) - 97
            s2d[char_to_add] += 1

            # print(s1d, s2d)

            # check the equality, if equal, found permutation (anagram)
            if s1d == s2d:
                return True

            # remove the previous character (chars that are not in the sliding w.)
            if win_start - win_len + 1 < len(s2) and win_start - win_len + 1 >= 0:
                char_to_remove = ord(s2[win_start-win_len + 1]) - 97
                # print(char_to_remove)
                s2d[char_to_remove] -= 1

            # print(s1d, s2d)

            win_start += 1
            win_end = win_start + win_len

        return False

    # using dictionary + enumerate instead of array
    # O(n)
    def checkInclusion_v3_fastest(self, s1: str, s2: str) -> bool:
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        s1_chars = {char: 0 for char in alphabet}
        for s1_char in s1:
            s1_chars[s1_char] += 1

        current_counts = {char: 0 for char in alphabet}
        for idx, s2_char in enumerate(s2):
            current_counts[s2_char] += 1
            if idx >= len(s1):
                current_counts[s2[idx - len(s1)]] -= 1

            if current_counts == s1_chars:
                return True

        return False
