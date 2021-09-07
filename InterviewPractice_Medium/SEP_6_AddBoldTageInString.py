"""
Add Bold Tag in String 

https://leetcode.com/problems/add-bold-tag-in-string/submissions/

- Key Insight: 
Utilize Merge Interval Idea! 

복습 하기 
다른 방식도 연구하기 
"""


class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        # 예외 처리
        if len(words) == 0:
            return s

        # 인터벌 찾기.
        intervals = []
        for i in range(len(words)):
            wlen = len(words[i])

            for j in range(len(s)):
                if s[j:wlen] == words[i]:
                    intervals.append([j, wlen-1])
                wlen += 1

        # print(intervals)

        if len(intervals) == 0:
            return s

        # 인터벌 합치기.
        intervals.sort(key=lambda x: x[0])

        prevStart = intervals[0][0]
        prevEnd = intervals[0][1]
        mergedIntervals = [[prevStart, prevEnd]]
        prevInd = 0
        for i in range(1, len(intervals)):
            curStart = intervals[i][0]
            curEnd = intervals[i][1]

            if prevStart <= curStart <= prevEnd + 1:
                curEnd = max(prevEnd, curEnd)
                prevEnd = curEnd
                mergedIntervals[prevInd] = [prevStart, curEnd]
            else:
                prevStart = curStart
                prevEnd = curEnd
                mergedIntervals.append([prevStart, prevEnd])
                prevInd += 1

        # print(mergedIntervals)

        # 태그 넣기.
        numAdd = 0
        for i in range(len(mergedIntervals)):
            start = mergedIntervals[i][0] + numAdd
            end = mergedIntervals[i][1] + numAdd

            news = s[:start] + "<b>" + s[start: end + 1] + "</b>" + s[end + 1:]

            s = news
            numAdd += 7

        return s

    def addBoldTag(s, words):
        def find_index(s, word):
            res = []
            for i in range(len(s)-len(word)+1):
                if s[i:i+len(word)] == word:
                    res.append([i, i+len(word)-1])
            return res

        intervals = []
        for word in words:
            cur = find_index(s, word)
            if cur:
                intervals.extend(cur)

        intervals = sorted(intervals)
        intervals.append([1001, 0])
        print(intervals)

        res = []
        prev = intervals[0]

        for i in range(1, len(intervals)):
            if intervals[i][0] > prev[1]:
                res.append(prev)
                prev = intervals[i]
            else:
                prev = [prev[0], max(prev[1], intervals[i][1])]

        s = list(s)
        for r in res[::-1]:
            s[r[0]] = "<b>"+s[r[0]]
            s[r[1]] = s[r[1]]+"</b>"

        return "".join(s).replace("</b><b>", "")

    def addBoldTag_v3(s, words):
        # Initialize a list of booleans for each character in s.
        bold = [False for _ in range(len(s))]

        # Iterate through the dictionary, marking words to be bolded as True.
        for word in words:
            # Mark every occurrence of the word as True.
            start = s.find(word)
            while start != -1:
                for i in range(start, len(word) + start):
                    bold[i] = True
                start = s.find(word, start + 1)

        # Initialize the output list of strings.
        output = []

        # Traverse the input string, building the output list.
        i = 0
        while i < len(s):
            # If the current character is to be bolded...
            if bold[i]:
                # Insert a bold tag.
                output.append("<b>")
                # Append characters to be bolded.
                while i < len(s) and bold[i]:
                    output.append(s[i])
                    i += 1
                # Insert the end tag.
                output.append("</b>")
            # Otherwise, just append the character.
            else:
                output.append(s[i])
                i += 1

        # Join the output list and return it.
        return "".join(output)
