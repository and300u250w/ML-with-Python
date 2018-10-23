# # Fibonacci


# def fib(x):
#     if x <= 1:
#         return x
#     else:
#         return fib(x-1) + fib(x-2)


# print(fib(9))

# # Factorial


# def fac(x):
#     if x == 1:
#         return x
#     else:
#         return x*fac(x-1)


# print(fac(5))

# # Factorial #2


# def fac2(x):
#     b = 1
#     for i in range(1, x+1):
#         b *= i
#     return b


# print(fac2(5))


def multiply(x):
    return (x*x)


def add(x):
    return (x+x)


funcs = [multiply, add]
for i in range(5):
    value = list(map(lambda x: x(i), funcs))
    print(value)


numbers = [2, 3, 4]
print(numbers)


def fib(n):
    a, b = 1, 1
    for i in range(n-1):
        a, b = b, a+b
    return a


print(fib(6))

import timeit

x = timeit.timeit('"-".join(map(str, range=(100)))', number=100)
print(x)
