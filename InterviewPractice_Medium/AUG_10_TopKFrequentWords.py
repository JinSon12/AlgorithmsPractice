# https://leetcode.com/problems/top-k-frequent-words/

"""
692. Top K Frequent Words

KEY Insights 
- using dictionary + tuple + reverse sorting 

- heapq

복습 요
"""


from collections import Counter
from typing import List
import heapq as hq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # nlog n due to sort

        d = {}

        if len(words) == 1:
            return words[0]

        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1

        res = []

        ltup = list(d.items())
        # https://leetcode.com/problems/top-k-frequent-words/discuss/923385/One-more-solution-in-Python-Easy
        # '-' is used for sorting in decreasing order, works only for nums
        ltup.sort(key=lambda x: (-x[1], x[0]), reverse=True)

        for _ in range(k):
            el = ltup.pop()
            res.append(el[0])

        return (res)

    # heapq + counter combination
    def topKFrequent_heapq(self, words: List[str], k: int) -> List[str]:
        words_counts = [(-c, w) for w, c in Counter(words).items()]
        hq.heapify(words_counts)
        return [w for _, w in hq.nsmallest(k, words_counts)]
