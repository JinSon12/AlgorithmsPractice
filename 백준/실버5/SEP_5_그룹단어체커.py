"""
https://www.acmicpc.net/problem/1316

그룹 단어 체커 

"""
N = int(input())


def checkGroupWord(word):
    d = {}

    for i in range(len(word)):
        if word[i] not in d:
            d[word[i]] = i
        else:
            if d[word[i]] == i - 1:
                d[word[i]] = i
            else:
                return 0

    return 1


def checkWords():
    counter = 0
    for _ in range(N):
        word = input()
        counter += checkGroupWord(word)

    print(counter)
    return


# faster, using list slicing
def checkWords_2():
    N = int(input())
    result = N
    for _ in range(N):
        string = input().strip()
        for i in range(len(string)-1):

            if string[i] == string[i+1]:
                continue
            if string[i] in string[i+1:]:
                result -= 1
                break


print(result)

checkWords()
