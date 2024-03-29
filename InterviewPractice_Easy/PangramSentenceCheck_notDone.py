# 1832. Check if the Sentence Is Pangram
# https://leetcode.com/problems/check-if-the-sentence-is-pangram/

# 87.03% faster, 91.35 less storage.
class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        alphabet = collections.defaultdict(list)

        for i in sentence:
            alphabet[i].append(i)

        if (len(alphabet) < 26):
            return False
        else:
            return True

    def checkIfPangram2(self, sentence: str) -> bool:
        alphabet = 'abcdefghijklmnopqrstuvwxyasdadasz'
        return set(sentence) == set(alphabet)

    def checkIfPangram3(self, sentence: str) -> bool:
        return len(set(sentence)) == 26
