def addNums(a, b):
    ans = a + b
    print(ans)


''' this is a multiplication function'''


def multiplication(a, b):
    ans = a * b
    print(ans)


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def linearSearch(myvals, n):
    for i in myvals:
        if i == n:
            return "Found"
    return "Not Found"
