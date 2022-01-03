""" 
명심할 것 
- 문자열 문제에서는 (다른 문제들과 마찮가지로) 여러가지 입력 케이스에 대해서 생각하기. 
- constraint 를 항상 clarify 하기. communication 은 중요하다. 

"""

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
            # 중복된 character
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

    # Trial 1 - Wrong
    # JAN 2 2022
    # failing tc - s = "dvdf"
    def lengthOfLongestSubstring_JAN2_2022_T1(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        charsEnc = set()
        p1 = 0
        p2 = p1 + 1
        charsEnc.add(s[p1])
        length = 0
        #   ^  문제 생김.
        while p2 < len(s):  # dvdf
            if s[p2] in charsEnc:
                charsEnc = set()
                p1 = p2  # d
                charsEnc.add(s[p1])  # d 에서 부터 문제가 생긴다.
                """ 
                d 에서부터 문제가 생긴다. 
                왜냐하면, set 을 초기화 하는 과정에서 이전에 있던 글자들이 없어진다. 
                - dvd 까지 set 에 있지만, 
                - p1 을 초기화된 set 에 넣는 과정에서 이전의 글자들이 모두 사라진다. 
                  따라서, set 에는 d 밖에 남지 않게 되고, 최종적으로 df 만 찾게 되어서 결과값이 다르게 나온다. 
                
                => 중복된 철자의 ind 만 이전 ind 에서 p2 로 업데이트 하면 된다. 
                => 글자와 연관된 ind 를 빠르게 찾을 수 있는 것 => dictionary / array 
                하지만, array 를 사용할 경우 ind 번호와 char 의 관계를 표현하는 것이 더 복잡할 것. 
                따라서 간편하게 dictionary 를 사용한다. 

                k = letter, v = ind 
                """
            else:
                charsEnc.add(s[p2])

            p2 += 1
            length = max(length, p2 - p1)

        return length

    """ 
    T1 에서 알수 있듯이 
    dictionary 를 사용하여 이때까지 발견한 철자의 ind 를 저장한다 
    k : letter, v: ind 
    # dvdf 
    Conditions 
    1) found repeating char :
        - if char in visitedChar: 
            p1 = visitedChar[char] + 1  # p1 을 중복된 ind 다음 ind 로 옮겨준다. 
                                        # 이 경우에서는 d (ind = 0, ind = 2) 로 중복을 발견했기 때문에
                                        # ind = 0 에 있는 p1 을 중복된 철자 다음 철자로 옮겨 주면 된다. 
                                        # 중요한 점 **** 
                                        # 우리는 p1 ind 이전의 철자들은 관심이 없다. 따라서, 
                                        # if 조건문이 if char in visitedChar -> 
                                        # if char in visitedChar and visitedChar[char] >= p1: 
                                        # 이면, 즉 p1 이후에 있는 철자에서 반복된 것이 있다면, 

            visitedChar[char] = p2  # p2 를 새로운 ind 로 업데이트 해준다. 
    
    2) non repeating char : 
        - p1 은 그대로 있고, 
        - p2 만 꾸준히 움직이면 된다 (사실 p2 는 위 두 조건에 관계없이 계속 움직인다.) -> for loop 을 써도 상관이 없다. 
    """

    def lengthOfLongestSubstring_JAN2_2022_T2(self, s: str) -> int:
        #    1
        # "tmmzuxt" 5
        # len(s) == 1 or len(s) == 0
        if len(s) < 2:
            return len(s)

        p1 = 0
        p2 = p1 + 1
        visitedChars = {s[p1]: 0}  # t: 0, m: 1 -> 2
        length = 0
        winLength = 1

        while p2 < len(s):
            char = s[p2]  # m, m, z, u, x, t

            # if repeating char
            # 새롭게 길이를 저장할 준비를 한다.
            if char in visitedChars and visitedChars[char] >= p1:
                p1 = visitedChars[char] + 1  # at 2nd m, p1 = 2

            # p1 과 p2 사이의 철자 중 반복되지 않는 철자의 경우 윈도우 길이를 하나 더 추가한다.
            else:
                winLength = p2 - p1 + 1  # 1-0+1 = 2, 3-2+1 = 2, 3, 4

            visitedChars[char] = p2
            p2 += 1  # 2, 3, 4, 5
            # 이 값이 업데이트 되는 경우는 winLength 가 변할 때 인데, 그 경우는 반복되지 않은 철자를 만났을 때이다.
            length = max(length, winLength)
            # 0 -> 2, 2, 2, 3, 4
        return length
