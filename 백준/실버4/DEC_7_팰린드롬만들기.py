""" 
https://www.acmicpc.net/problem/1213
"""

inp = input()


def createPalindrome(string):
    charCounter = [0 for _ in range(26)]
    oddCounter = 0

    for char in string:
        charCounter[ord(char)-65] += 1
        # print(char, ord(char), ord(char) - 65)

    oddAlphabet = ""
    alphabet = ""
    for i in range(len(charCounter)):
        charCnt = charCounter[i]
        char = chr(i + 65)
        if charCnt % 2 != 0:
            oddCounter += 1
            oddAlphabet += char

        if oddCounter > 1:
            print("I'm Sorry Hansoo")
            return

        alphabet += char * (charCnt // 2)

    print(alphabet + oddAlphabet + alphabet[::-1])


createPalindrome(inp)
