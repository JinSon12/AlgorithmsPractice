def hello():
    print("Hello Python")


hello()
hello()
hello()


def hello2(name):
    print("Hello ", name)


hello2("gul")
hello2("ggul")


def square(a):
    c = a * a
    return c


print(square(5))


def triangle(a, h):
    area = a * h / 2
    return area


areaTriangle = triangle(2, 5)
print(areaTriangle)


# calculate sum of 1 to n
def sum_func(n):
    result = 0
    for x in range(1, n+1):
        result += x
    return result


print(sum_func(10))

# calculate n factorials


def factorial(n):
    fact = 1
    for x in range(1, n+1):
        fact *= x
    return fact


print(factorial(5))
