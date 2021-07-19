from math import factorial, atan, pi, asin, sin, log


def combination(m, n):
    return factorial(m) // (factorial(n) * factorial(m - n))


def f(x):
    return log(x)


def derivation(x, n, h):
    sum = 0

    for i in range(0, n+1):
        sum += combination(n, i)*f(x+(n-i)*h) * (-1)**i

    print(sum/h**n)

def centralDiff(x,n,h):
    sum = 0

    for i in range(0, n+1):
        sum += combination(n, i)*f(x- (n/2)*h +(n-i)*h) * (-1)**i

    print(sum/h**n)

derivation(1, 4, 0.0001)
centralDiff(1, 4, 0.0001)
