"""
2941. 크로아티아 알파벳 

"""

string = input()


def alphabet(string):
    chars = set({"c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="})

    res = 0
    i = 0

    while i < len(string):
        chars = string[i]
        nextnum = i+1

        if chars == "c" and nextnum < len(string):
            if string[nextnum] == "=" or string[nextnum] == "-":
                i += 1

        elif chars == "d" and nextnum < len(string):
            if string[nextnum] == "-":
                i += 1

            elif string[nextnum] == "z" and i+2 < len(string) and string[i+2] == "=":
                i += 2

        elif chars == "l" or chars == "n" and nextnum < len(string):
            if string[nextnum] == "j":
                i += 1

        elif chars == "s" or chars == "z" and nextnum < len(string):
            if string[nextnum] == "=":
                i += 1

        res += 1

        i += 1

    return res


def alphabet_replacemethod(string):
    pass


print(alphabet(string))
