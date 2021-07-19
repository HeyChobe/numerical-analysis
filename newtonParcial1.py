from math import cos, sin

def f(x):
    return x**4 - 16*x**3 + 78*x**2 - 412*x + 624

def f1(p0,h):
    return (f(p0+h)-f(p0))/h

def newton(p0, TOL, Nmax):
    h=10**-4
    p = 0
    print("{0:} \t {1:} \t\t\t {2:} \t\t\t {3:}".format("i","p0","p","ERROR"))
    for i in range(0,Nmax):
        p = p0 - f(p0)/f1(p0,h)
        print("{0:d} \t {1:.15f} \t {2:.15f} \t {3:.15f}".format(i,p0,p,abs(p-p0)))
        if (abs(p-p0)<TOL):
            break
        p0=p

newton(-6,10**-6,12)
