"""
2941. 크로아티아 알파벳 

"""

string = input().split()


def alphabet(string):
    res = 0
    i = 0

    while i < len(string):
        chars = string[i]
        nextnum = i+1

        if chars == "c":
            if nextnum < len(string):
                if string[nextnum] == "=" or string[nextnum] == "-":
                    i += 1

        elif chars == "d":
            if nextnum < len(string):
                if string[nextnum] == "-":
                    i += 1

                elif string[nextnum] == "z" and i+2 < len(string):
                    if string[i+2] == "=":
                        i += 2

        elif chars == "l" or chars == "n":
            if nextnum < len(string):
                if string[nextnum] == "j":
                    i += 1

        elif chars == "s" or chars == "z":
            if nextnum < len(string):
                if string[nextnum] == "=":
                    i += 1

        res += 1
        i += 1

    return res


def alphabet_replacemethod(string):
    pass


print(alphabet(string))
