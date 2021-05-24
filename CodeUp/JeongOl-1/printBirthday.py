# example input: 781201-1273845
# example output: 1978/12/01 M

inp = input()
jumin = inp.split("-")

bday = jumin[0]
year = f'19{bday[0]}{bday[1]}/{bday[2]}{bday[3]}/{bday[4]}{bday[5]}'
gender = jumin[1][0]


print(year, "M" if gender == "1" else "F")
