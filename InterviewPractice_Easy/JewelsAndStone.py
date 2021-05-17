# HashMap

import collections


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        # defaultdict initialzed with 0
        freqs = collections.defaultdict(int)
        cnt = 0

        for char in stones:
            freqs[char] += 1

        # for each character in jewels,
        # add the number of freq. of that char in stones to count.
        for char in jewels:
            cnt += freqs[char]

        return cnt
