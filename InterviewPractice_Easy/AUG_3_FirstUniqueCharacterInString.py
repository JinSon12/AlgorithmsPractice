class Solution:
    def firstUniqChar(self, s: str) -> int:
        d = {}
        ind = {}

        for i in range(len(s)):
            c = s[i]
            if c not in d:
                d[c] = 1
                ind[c] = i
            else:
                d[c] += 1

        for k, v in d.items():
            if v == 1:
                return ind[k]

        return -1

    def firstUniqChar_v2(self, s: str) -> int:
        dic = {}
        for ch in s:
            dic[ch] = dic.get(ch, 0) + 1
        idx = 0
        for ch in s:
            if dic[ch] == 1:
                return idx
            idx += 1
        return -1

    # interesting way to solve
    def firstUniqChar_v3(self, s: str) -> int:
        count = -1
        yolo = list(dict.fromkeys(s))
        for i in yolo:
            if s.count(i) == 1:
                count += s.index(i)+1
                break
        return count
