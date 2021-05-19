class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        res = [""]*len(indices)

        for i, n in enumerate(indices):
            res[n] = s[i]

        return "".join(res)
