def factorial(n):
    if n == 0:
        return 1
    if n > 1:
        return n * factorial(n-1)
    if n == 1:
        return 1
n = 4
print(factorial(n))