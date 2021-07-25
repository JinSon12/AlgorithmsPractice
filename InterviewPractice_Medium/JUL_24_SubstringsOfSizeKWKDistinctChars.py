# Substrings of size K with K distinct chars

"""
Given a string s and an int k, return all unique substrings of s of size k with k distinct characters.

Example 1:

Input: s = "abcabc", k = 3
Output: ["abc", "bca", "cab"]
Example 2:

Input: s = "abacab", k = 3
Output: ["bac", "cab"]
Example 3:

Input: s = "awaglknagawunagwkwagl", k = 4
Output: ["wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag"]
Explanation: 
Substrings in order are: "wagl", "aglk", "glkn", "lkna", "knag", "gawu", "awun", "wuna", "unag", "nagw", "agwk", "kwag", "wagl" 
"wagl" is repeated twice, but is included in the output once.
Constraints:

The input string consists of only lowercase English letters [a-z]
0 ≤ k ≤ 26

"""
import timeit


def substringk(s, k):
    # edge case
    if s == "" or k == 0:
        return None

    used = {}
    res = set()

    start, end = 0, 0
    string = ""

    for end, c in enumerate(s):
        # if i of used[c] >= start, this means that there is a repeating character c in the window.
        if c in used and start <= used[c]:
            start = used[c] + 1
            string = s[start]

        string += c
        used[c] = end

        if end - start + 1 == k:
            start += 1
            res.add(string)
            string = string[1:]

    return res


# The idea is to maintain a window and every time the window size is reached, we just add the substring to the dictionary
# Check for the condition that it has unique characters before adding them to the dictionary using sets
# Elegant solution, but slower
def generate_substr_V2(s, k):
    if not s or k == 0:
        return None

    result = {}

    for i in range(len(s)):
        if len(s)-i < k:
            break
        a = set(s[i:i+k])     # unique 한 char 의 갯수를 set을 통해서 세고
        if len(a) == k:       # set 의 길이가 k 이면, (즉 unique 한 chars 가 k 개 있다면)
            result[s[i:i + k]] = 1

    return result.keys()


start = timeit.default_timer()
print(generate_substr_V2('awaglknagawunagwkwagl', 4))
stop = timeit.default_timer()
print('Time: for 1', stop - start)

start = timeit.default_timer()
print(substringk("awaglknagawunagwkwagl", 4))
stop = timeit.default_timer()
print('Time: for 2', stop - start)

# res = substringk("awaglknagawunagwkwagl", 4)
# seta = set(["wagl", "aglk", "glkn", "lkna", "knag", "gawu",
#             "awun", "wuna", "unag", "nagw", "agwk", "kwag"])

# if res == seta:
#     print("yes")
