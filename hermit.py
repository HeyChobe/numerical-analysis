from sympy import Symbol, init_printing
from math import pi

x = Symbol("x")

def lagrangePol(n, xs, ys):
    p = 0
    for k in range(0, n+1):
        p += ys[k] * lagrangeL(n, xs, k)
    return p    


def lagrangeL(n, xs, k):
    L = 1
    for i in range(0, n+1):
        if (i != k):
            L *=(x - xs[i] )/(xs[k] - xs[i])
    return L

xs = [2,5]
ys = [4,1]

pol = lagrangePol(1, xs, ys)

pol.expand()
init_printing()