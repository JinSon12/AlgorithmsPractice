# https://leetcode.com/problems/goat-latin/

import timeit

"""
824. Goat Latin

- String

You are given a string sentence that consist of words separated by spaces. Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.) 
The rules of Goat Latin are as follows:

If a word begins with a vowel ('a', 'e', 'i', 'o', or 'u'), append "ma" to the end of the word.
For example, the word "apple" becomes "applema".

If a word begins with a consonant (i.e., not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1.
For example, the first word gets "a" added to the end, the second word gets "aa" added to the end, and so on.

Return the final sentence representing the conversion from sentence to Goat Latin.


"""


class Solution:
    # in the sample solution, 8ms but actual runtime slower than the original solution below
    # 3.94 * e-05
    def toGoatLatin_fastest(self, s: str) -> str:
        vowels = set(list('aeiouAEIOU'))
        s = s.split(' ')
        ls = len(s)
        for i in range(ls):
            if s[i][0] in vowels:
                s[i] = s[i]+'ma'+'a'*(i+1)
            else:
                s[i] = s[i][1:]+s[i][0]+'ma'+'a'*(i+1)
        return ' '.join(s)

    # 1.28 * e-05
    def toGoatLatin(self, sentence: str) -> str:
        s = sentence.split()

        vowel = set({"a", "e", "i", "o", "u"})

        res = []

        for ind, word in enumerate(s):

            if word[0].lower() in vowel:
                word += "ma"

            else:
                word = word[1:] + word[0] + "ma"

            res.append(word + "a" * (ind + 1))

            return " ".join(res)


stn = Solution()
start = timeit.default_timer()
stn.toGoatLatin_fastest(
    "The quick brown fox jumped over the lazy dog The quick brown fox jumped over the lazy dog The quick brown fox jumped over the lazy dog The quick brown fox jumped over the lazy dog")
stop = timeit.default_timer()
print('Time: ', stop - start)
