# https://leetcode.com/problems/verifying-an-alien-dictionary/submissions/

"""
953. Verifying an Alien Dictionary


- Approach 

- Hash indexes of each character for better runtime
- Compare every adjacent word
- If any letter of former word is in higher order, return False
- If current letter of former word is in lower order, forget the rest of word
- If lenght of former word is longer and latter word is substring of former, return False (apple & app etc.)
Return True

"""


class Solution:
    # 36ms, 62.63%
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        dOrd = {order[x]: 0 + x for x in range(len(order))}

        for i in range(1, len(words)):
            curWord = words[i]
            prevWord = words[i-1]

            length = min(len(curWord), len(prevWord))

            # if the two words are same up until the shorter word's length,
            # return if the shorter word is not coming before the longer word
            if prevWord[:length] == curWord[:length]:
                if len(prevWord) != length:
                    return False

            for char in range(length):
                curWordChar = curWord[char]
                prevWordChar = prevWord[char]

                if curWordChar != prevWordChar:
                    # if the prevWord's char has higher order, return false (= not lexicographically sorted)
                    if dOrd[curWordChar] < dOrd[prevWordChar]:
                        return False

                    else:
                        # break, coz we already verified that the two words are in order
                        # (meaning no need to check the rest of the two words)
                        break

        return True

    # 28ms
    def isAlienSorted_MoreConcise(self, words: List[str], order: str) -> bool:
        decipher = dict()
        for i, x in enumerate(order):
            decipher[x] = i

        for i in range(1, len(words)):
            for j in range(len(words[i-1])):
                if j == len(words[i]) or decipher[words[i-1][j]] > decipher[words[i][j]]:
                    return False
                if decipher[words[i-1][j]] < decipher[words[i][j]]:
                    break

        return True

    def isAlienSorted_zip(self, words, order):
        ind = {c: i for i, c in enumerate(order)}

        for a, b in zip(words, words[1:]):
            if len(a) > len(b) and a[:len(b)] == b:
                return False
            for s1, s2 in zip(a, b):
                if ind[s1] < ind[s2]:
                    break
                elif ind[s1] > ind[s2]:
                    return False
        return True

    def isAlienSorted_zip_moreConcise(self, words, order):
        m = {c: i for i, c in enumerate(order)}
        words = [[m[c] for c in w] for w in words]
        return all(w1 <= w2 for w1, w2 in zip(words, words[1:]))
