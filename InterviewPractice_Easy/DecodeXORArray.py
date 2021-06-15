# https://leetcode.com/problems/decode-xored-array/submissions/


class Solution:
    # faster than 99.91, less mem than 61.63%
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for i in range(len(encoded)):
            result.append(encoded[i] ^ result[i])

        return result
