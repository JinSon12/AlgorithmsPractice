from collections import defaultdict


class Solution:
    def lengthOfLongestSubstring_ON2(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        counter = 1
        st = set()

        for i in range(len(s)):
            st = set()
            st.add(s[i])
            tempc = 1
            for j in range(i+1, len(s)):
                if s[j] != s[i] and s[j] not in st:
                    tempc += 1
                    st.add(s[j])
                elif s[j] in st:
                    break

            counter = max(counter, tempc)

        return counter

    """
    The goal is to use *** sliding window ***. 
    https://blog.fakecoding.com/archives/algorithm-slidingwindow/ 
    https://velog.io/@kgh732/Python-으로-푸는-Leetcode3.-Longest-Substring-Without-Repeating-Characters
    
    stretch the window as far until a repeated character appears 
    & the starting index of the window is before the index of that repeated character 
    (the previously occuring index of which is saved in the dictionary)

    b/c we have encountered a repeating character, 
    we start counting the length of the window again from 1 
    the starting ind will become the ind after the repeated character 
    (중복된 char 검출 후, 그 다음 인덱스가 start_ind of the sliding window)


    The extra DS dictionary was used to keep track of the indices of characters,
    thus N^2 traversal (which checks the elements that we have already checked) not needed. 

    """
    # 40ms 99.71%

    def lengthOfLongestSubstring_ON(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        d = defaultdict(int)

        win_start = 0
        win_len = 1
        max_len = 1

        for win_end in range(len(s)):
            if s[win_end] in d and win_start <= d[s[win_end]]:
                win_start = d[s[win_end]] + 1
                print(win_end, win_start)

            else:
                win_len = win_end - win_start + 1

            d[s[win_end]] = win_end

            max_len = max(max_len, win_len)

        return max_len

    # Fastest runtime
    def lengthOfLongestSubstring_V3(self, s: str) -> int:
        if s == "":
            return 0
        a = ""
        b = ""
        for v in s:
            if v not in a:
                a += v
            else:
                if len(a) > len(b):
                    b = a
                a = a.split(v)[1]+v
        if len(a) > len(b):
            b = a
        return len(b)
