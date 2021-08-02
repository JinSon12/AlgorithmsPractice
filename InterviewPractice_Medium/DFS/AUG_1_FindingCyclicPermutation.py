# Practice.


lst = "123"
temp = ""
for i in range(len(lst)):
    lst = lst[-1] + lst[:-1]
    print(lst)
