# https://leetcode.com/problems/most-common-word/


"""
819. Most Common Word


"""

from collections import Counter
import re


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # regex 에서 ^ 은 not, \w = word, \s whitespace
        nopunc = re.sub(r'[^\w\s]', ' ', paragraph)

        split = nopunc.split(" ")
        cleanse = []
        banned = set(banned)

        for word in split:
            if word.isalpha() and word.lower() not in banned:
                cleanse.append(word.lower())

        count = Counter(cleanse)
        print(count)

        res = 0
        val = ""
        for el in count:
            temp = res
            res = max(res, count[el])
            if temp != res:
                val = el

        return val

    # Fastest Solution, 12ms
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:

        paragraph = re.sub(r'[^\w\s]', ' ', paragraph)
        # we have to remove all punctuation marks

        print(paragraph)

        #paragraph = paragraph.replace(",", "")
        #paragraph = paragraph.replace(".", "")

        temp = list(paragraph.split())

        lst = []
        for i in temp:

            lst.append(i.lower())

        s = list(set(lst))

        m = -1
        ans = ""

        for i in s:

            if not i in banned:

                count = lst.count(i)

                if count > m:

                    m = count
                    ans = i

        return ans

    # concise yet fast solution, 32ms
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        freq = dict()
        banned = set(banned)

        paragraph = re.split("[!?',;.\\s]+", paragraph.lower())
        for x in paragraph:
            if x not in banned:
                if x in freq.keys():
                    freq[x] += 1
                else:
                    freq[x] = 1

        mx = max(freq, key=freq.get)
        print(freq)
        return mx.lower()

    # more concise solution, 32ms
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph)
                 .lower().split()
                 if word not in banned]

        counts = Counter(words)
        return counts.most_common(1)[0][0]
