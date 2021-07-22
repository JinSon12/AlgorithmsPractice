class Solution:
    """
    Greedy
    """

    # 99.91% 48ms
    def diStringMatch(self, s: str) -> List[int]:
        res = []
        low = 0
        high = len(s)

        for c in s:
            if c == "I":
                res.append(low)
                low += 1

            else:
                res.append(high)
                high -= 1

        res.append(high)
        return (res)
